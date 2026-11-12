#!/usr/bin/env python3
"""Requirements extraction and verification tool for pytkwrap.

Static analysis only (``ast``); it never imports GTK or pytkwrap, so it is fast,
safe to run without a display, and unaffected by work-in-progress import errors.

Subcommands
-----------
facts PACKAGE [PACKAGE ...]
    Print the facts needed to write requirements for a source package (for
    example ``gtk3/font``): exports, class bases, default sizes, attributes,
    properties, signals, ordered ``do_set_properties()`` steps, constructor steps,
    public method bodies, and matching test node IDs.
draft PACKAGE --prefix FNT
    Generate a skeleton requirements document in the project format.  Rationales
    and value-method behavior are marked TBD for human review.
check
    Validate every requirements document: labels, headings, cross-references,
    fields, cited tests, ID gaps, export coverage, code/doc drift for signals and
    property keys, and ``.py``/``.pyi`` stub consistency.  Exits 1 on errors.

Configuration is read from ``[tool.reqtool]`` in ``pyproject.toml`` (optional)::

    [tool.reqtool]
    exclude = ["src/pytkwrap/gtk3/dialog/databaseselectdialog.py"]

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
import argparse
import ast
import datetime
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "pytkwrap"
TESTS = ROOT / "tests"
DOCS = ROOT / "docs" / "requirements"

REQUIRED_FIELDS = (
    "Description",
    "Rationale",
    "Traces to",
    "Status",
    "Version",
    "History",
    "Tests",
)
FORBIDDEN_FIELDS = ("Issues",)
VALID_STATUS = {"Active", "Planned", "Deleted", "Superseded"}
VALUE_METHODS = ("do_get_value", "do_set_value")
PYTKWRAP_NAME = re.compile(r"(GTK3|PyTkWrap)\w*$|\w*Mixin$")
MODULE = "<module>"  # key for module-level test functions
DIC_KEY = re.compile(r"self\.dic_(properties|attributes)\[['\"](\w+)['\"]\]")
BOILERPLATE = re.compile(
    r"super\(\)\.__init__\(\*\*kwargs\)$"
    r"|self\.dic_(attributes|properties|handler_id)\.update\(\{?_?\w*.*self\._GTK"
)


# --------------------------------------------------------------------------- #
# Configuration                                                               #
# --------------------------------------------------------------------------- #
def load_config() -> dict:
    """Return the ``[tool.reqtool]`` table from pyproject.toml, if available."""
    try:
        # Standard Library Imports
        import tomllib  # pylint: disable=import-outside-toplevel
    except ModuleNotFoundError:  # Python 3.10
        return {}
    with (ROOT / "pyproject.toml").open("rb") as _file:
        return tomllib.load(_file).get("tool", {}).get("reqtool", {})


def excluded(path: Path, config: dict) -> bool:
    """Return True if the path is excluded by configuration."""
    rel = path.relative_to(ROOT).as_posix()
    return any(
        rel == _ex or rel.startswith(_ex.rstrip("/") + "/")
        for _ex in config.get("exclude", [])
    )


# --------------------------------------------------------------------------- #
# Source facts                                                                #
# --------------------------------------------------------------------------- #
@dataclass
class Step:
    """One ordered statement in do_set_properties() or __init__()."""

    text: str
    guard: str = ""


@dataclass
class MethodFacts:
    """A public method or property."""

    name: str
    signature: str
    summary: str
    source: str
    is_property: bool = False


@dataclass
class ClassFacts:  # pylint: disable=too-many-instance-attributes
    """Facts extracted from one class definition."""

    name: str
    module: str
    lineno: int
    bases: list[str]
    summary: str
    defaults: dict[str, str] = field(default_factory=dict)
    attributes: dict[str, str] = field(default_factory=dict)
    properties: dict[str, str] = field(default_factory=dict)
    signals: list[str] = field(default_factory=list)
    gobject_signals: list[str] = field(default_factory=list)
    set_properties: list[Step] | None = None
    init_params: list[str] = field(default_factory=list)
    init_steps: list[Step] = field(default_factory=list)
    methods: list[MethodFacts] = field(default_factory=list)

    @property
    def is_mixin(self) -> bool:
        """Return True if this is a pytkwrap mixin rather than a wrapper."""
        return self.name.endswith("Mixin")

    @property
    def native(self) -> str | None:
        """Return the native GTK/GObject base class, if any."""
        for _base in self.bases:
            if _base.split(".")[0] in {"Gtk", "Gdk", "GObject", "Gio", "Pango"}:
                return _base
        return None

    @property
    def pytkwrap_bases(self) -> list[str]:
        """Return the pytkwrap mixin bases."""
        return [_b for _b in self.bases if _b != self.native]


@dataclass
class PackageFacts:
    """Facts for one source package (directory) or module."""

    name: str
    path: str
    exports: list[str]
    classes: list[ClassFacts]
    functions: list[MethodFacts]


def _render(node: ast.AST) -> str:
    """Unparse a node, shortening self.dic_properties["key"] to key."""
    return DIC_KEY.sub(r"\2", _dq(ast.unparse(node)))


def _dq(text: str) -> str:
    """Use double quotes for simple string literals, matching project style."""
    return re.sub(r"'([^'\"\\]*)'", r'"\1"', text)


def _guard(test: ast.expr) -> str:
    return f"if {_render(test)}"


def _steps(body: list[ast.stmt], guard: str = "") -> list[Step]:
    """Flatten a method body into ordered, human-readable steps."""
    steps: list[Step] = []
    for stmt in body:
        if isinstance(stmt, ast.If):
            steps += _steps(stmt.body, _join(guard, _guard(stmt.test)))
            if stmt.orelse:
                steps += _steps(
                    stmt.orelse, _join(guard, f"not ({_render(stmt.test)})")
                )
        elif isinstance(stmt, ast.For) and isinstance(stmt.iter, (ast.List, ast.Tuple)):
            names = [_e.value for _e in stmt.iter.elts if isinstance(_e, ast.Constant)]
            body_src = ast.unparse(stmt.body[0]) if stmt.body else ""
            if "set_property" in body_src and names:
                for _n in names:
                    steps.append(
                        Step(f'set_property("{_n.replace("_", "-")}", {_n})', guard)
                    )
            else:
                steps.append(Step(_render(stmt).splitlines()[0] + " ...", guard))
        elif isinstance(stmt, (ast.Try, ast.With)):
            steps.append(Step(_render(stmt).splitlines()[0] + " ...", guard))
        elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
            continue  # docstring
        elif BOILERPLATE.match(ast.unparse(stmt)):
            continue  # standard mixin bookkeeping, captured from class constants
        elif (
            isinstance(stmt, ast.Assign)
            and len(stmt.targets) == 1
            and DIC_KEY.fullmatch(ast.unparse(stmt.targets[0]))
        ):
            target = DIC_KEY.sub(r'dic_\1["\2"]', ast.unparse(stmt.targets[0]))
            steps.append(Step(f"{target} = {_render(stmt.value)}", guard))
        else:
            steps.append(
                Step(" ".join(_l.strip() for _l in _render(stmt).splitlines()), guard)
            )
    return steps


def _join(a: str, b: str) -> str:
    return f"{a} and {b.removeprefix('if ')}" if a else b


def _class_constant(node: ast.Assign | ast.AnnAssign, facts: ClassFacts) -> None:
    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
    value = node.value
    for target in targets:
        if not isinstance(target, ast.Name) or value is None:
            continue
        name = target.id
        if name in {"_DEFAULT_HEIGHT", "_DEFAULT_WIDTH", "_DEFAULT_TOOLTIP"}:
            facts.defaults[name] = _dq(ast.unparse(value))
        elif isinstance(value, ast.Call):
            func = ast.unparse(value.func)
            kws = {
                _k.arg: _dq(ast.unparse(_k.value)) for _k in value.keywords if _k.arg
            }
            if func.endswith("Properties"):
                facts.properties.update(kws)
            elif func.endswith("Attributes"):
                facts.attributes.update(kws)
        elif "SIGNALS" in name and isinstance(value, (ast.List, ast.Tuple)):
            facts.signals += [
                _e.value for _e in value.elts if isinstance(_e, ast.Constant)
            ]


def _method(node: ast.FunctionDef) -> MethodFacts:
    doc = ast.get_docstring(node) or ""
    is_prop = any(ast.unparse(_d) == "property" for _d in node.decorator_list)
    sig = f"{node.name}({ast.unparse(node.args)})"
    if node.returns is not None:
        sig += f" -> {ast.unparse(node.returns)}"
    body = [
        _s
        for _s in node.body
        if not (isinstance(_s, ast.Expr) and isinstance(_s.value, ast.Constant))
    ]
    src = "\n".join(ast.unparse(_s) for _s in body)
    return MethodFacts(node.name, sig, doc.splitlines()[0] if doc else "", src, is_prop)


def parse_module(path: Path) -> tuple[list[ClassFacts], list[MethodFacts], list[str]]:
    """Return the classes, public functions, and __all__ of a module."""
    text = path.read_text()
    tree = ast.parse(text)
    rel = path.relative_to(ROOT).as_posix()
    classes: list[ClassFacts] = []
    functions: list[MethodFacts] = []
    exports: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(_t, ast.Name) and _t.id == "__all__" for _t in node.targets
        ):
            if isinstance(node.value, (ast.List, ast.Tuple)):
                exports = [
                    _e.value for _e in node.value.elts if isinstance(_e, ast.Constant)
                ]
        elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            functions.append(_method(node))
        elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
            doc = ast.get_docstring(node) or ""
            facts = ClassFacts(
                node.name,
                rel,
                node.lineno,
                [ast.unparse(_b) for _b in node.bases],
                doc.splitlines()[0] if doc else "",
            )
            for item in node.body:
                if isinstance(item, (ast.Assign, ast.AnnAssign)):
                    _class_constant(item, facts)
                elif isinstance(item, ast.FunctionDef):
                    decorators = [ast.unparse(_d) for _d in item.decorator_list]
                    if any(_d.endswith("Signal") for _d in decorators):
                        facts.gobject_signals.append(item.name.replace("_", "-"))
                    elif item.name == "do_set_properties":
                        facts.set_properties = _steps(item.body)
                    elif item.name == "__init__":
                        facts.init_params = [
                            ast.unparse(_a)
                            + (f" = {ast.unparse(_d)}" if _d is not None else "")
                            for _a, _d in _with_defaults(item.args)
                            if _a.arg != "self"
                        ]
                        facts.init_steps = _steps(item.body)
                    elif not item.name.startswith("_"):
                        facts.methods.append(_method(item))
            classes.append(facts)
    return classes, functions, exports


def _with_defaults(args: ast.arguments) -> list[tuple[ast.arg, ast.expr | None]]:
    positional = args.posonlyargs + args.args
    defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    pairs = list(zip(positional, defaults, strict=True))
    pairs += list(zip(args.kwonlyargs, args.kw_defaults, strict=True))
    if args.vararg:
        args.vararg.arg = "*" + args.vararg.arg
        pairs.append((args.vararg, None))
    if args.kwarg:
        args.kwarg.arg = "**" + args.kwarg.arg
        pairs.append((args.kwarg, None))
    return pairs


def resolve_package(spec: str) -> Path:
    """Resolve 'font', 'gtk3/font', 'src/pytkwrap/gtk3/font', or a module path."""
    for candidate in (Path(spec), ROOT / spec, SRC / spec, SRC / "gtk3" / spec):
        for _c in (candidate, candidate.with_suffix(".py")):
            if _c.exists():
                return _c.resolve()
    raise SystemExit(f"reqtool: cannot find package or module '{spec}'")


def package_facts(spec: str, config: dict) -> PackageFacts:
    """Collect facts for every module in a package (or for one module)."""
    path = resolve_package(spec)
    modules = [path] if path.is_file() else sorted(path.glob("*.py"))
    classes: list[ClassFacts] = []
    functions: list[MethodFacts] = []
    exports: list[str] = []
    for module in modules:
        if excluded(module, config):
            continue
        _cls, _fun, _exp = parse_module(module)
        if module.name == "__init__.py":
            exports = _exp
        else:
            classes += _cls
            functions += _fun
    name = path.relative_to(SRC).with_suffix("").as_posix()
    return PackageFacts(
        name, path.relative_to(ROOT).as_posix(), exports, classes, functions
    )


# --------------------------------------------------------------------------- #
# Test facts                                                                  #
# --------------------------------------------------------------------------- #
@dataclass
class TestClass:
    """A test class and the test methods it defines."""

    name: str
    bases: list[str]
    methods: list[str]
    widget_class: str | None


def _test_classes(path: Path) -> dict[str, TestClass]:
    found: dict[str, TestClass] = {}
    try:
        tree = ast.parse(path.read_text())
    except (OSError, SyntaxError):
        return found
    functions = [
        _n.name
        for _n in tree.body
        if isinstance(_n, ast.FunctionDef) and _n.name.startswith("test_")
    ]
    found[MODULE] = TestClass(MODULE, [], functions, None)
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        widget = None
        for item in node.body:
            if isinstance(item, ast.Assign) and any(
                isinstance(_t, ast.Name) and _t.id == "widget_class"
                for _t in item.targets
            ):
                widget = ast.unparse(item.value)
        methods = [
            _i.name
            for _i in node.body
            if isinstance(_i, ast.FunctionDef) and _i.name.startswith("test_")
        ]
        found[node.name] = TestClass(
            node.name,
            [ast.unparse(_b).split(".")[-1] for _b in node.bases],
            methods,
            widget,
        )
    return found


class TestIndex:
    """Static index of test classes, including methods inherited from conftest bases."""

    def __init__(self) -> None:
        # Base test classes may live in conftest.py or in any test module that a
        # conftest imports, so index every test module (local classes win).
        self.shared: dict[str, TestClass] = {}
        for module in sorted(TESTS.rglob("*.py")):
            for name, info in _test_classes(module).items():
                if name != MODULE:
                    self.shared.setdefault(name, info)
        self._files: dict[Path, dict[str, TestClass]] = {}

    def file(self, path: Path) -> dict[str, TestClass]:
        """Return the test classes in a test file."""
        if path not in self._files:
            self._files[path] = _test_classes(path)
        return self._files[path]

    def methods(self, path: Path, cls: str) -> set[str] | None:
        """Return all test methods of a class (own and inherited), or None if
        unknown."""
        local = self.file(path)
        seen: set[str] = set()
        out: set[str] = set()
        todo = [cls]
        while todo:
            name = todo.pop()
            if name in seen:
                continue
            seen.add(name)
            info = local.get(name) or self.shared.get(name)
            if info is None:
                if name == cls:
                    return None
                continue
            out.update(info.methods)
            todo += info.bases
        return out

    def own_methods(self, node: str) -> list[str]:
        """Return the test methods defined directly on a test class node ID."""
        file, cls = node.split("::")[:2]
        info = self.file(ROOT / file).get(cls)
        return sorted(info.methods) if info else []

    def node_ids(self, wrapper: str, module: str) -> list[str]:
        """Return node IDs of the test class that targets a wrapper class."""
        rel_dir = Path(module).parent.relative_to("src/pytkwrap")
        path = TESTS / rel_dir / f"test_{Path(module).stem}.py"
        for name, info in self.file(path).items():
            if (
                name != MODULE
                and info.widget_class == wrapper
                or name in {f"Test{wrapper}", f"Test{wrapper.removeprefix('GTK3')}"}
            ):
                rel = path.relative_to(ROOT).as_posix()
                return sorted(
                    f"{rel}::{name}::{_m}" for _m in (self.methods(path, name) or set())
                )
        return []


# --------------------------------------------------------------------------- #
# facts                                                                       #
# --------------------------------------------------------------------------- #
def format_facts(pkg: PackageFacts, tests: TestIndex) -> str:
    """Render package facts as compact Markdown."""
    out = [
        f"# {pkg.name}  ({pkg.path})",
        "",
        f"Exports (__all__): {', '.join(pkg.exports) or '(none)'}",
    ]
    for fn in pkg.functions:
        out += [
            "",
            f"## function {fn.signature}",
            f"  {fn.summary}",
            _indent(fn.source),
        ]
    for cls in pkg.classes:
        out += [
            "",
            f"## {cls.name}({', '.join(cls.bases)})  [{cls.module}:{cls.lineno}]",
        ]
        if cls.summary:
            out.append(f"  {cls.summary}")
        for label, data in (
            ("defaults", cls.defaults),
            ("attributes", cls.attributes),
            ("properties", cls.properties),
        ):
            if data:
                out.append(
                    f"  {label}: " + ", ".join(f"{_k}={_v}" for _k, _v in data.items())
                )
        if cls.signals:
            out.append(f"  signals: {', '.join(cls.signals)}")
        if cls.gobject_signals:
            out.append(f"  GObject.Signal defined: {', '.join(cls.gobject_signals)}")
        if cls.init_params or cls.init_steps:
            out.append(f"  __init__({', '.join(cls.init_params)}):")
            out += [
                f"    - {_s.text}" + (f"   [{_s.guard}]" if _s.guard else "")
                for _s in cls.init_steps
            ]
        if cls.set_properties is not None:
            out.append("  do_set_properties:")
            out += [
                f"    - {_s.text}" + (f"   [{_s.guard}]" if _s.guard else "")
                for _s in cls.set_properties
            ]
        for meth in cls.methods:
            kind = "property" if meth.is_property else "method"
            out.append(f"  {kind} {meth.signature}: {meth.summary}")
            out.append(_indent(meth.source, 6))
        if not cls.is_mixin and cls.native:
            ids = tests.node_ids(cls.name, cls.module)
            test_class = (
                ids[0].rsplit("::", 1)[0] if ids else "(no matching test class found)"
            )
            own = tests.own_methods(test_class) if ids else []
            out.append(f"  tests: {test_class}  ({len(ids) - len(own)} inherited)")
            if own:
                out.append(f"    {' '.join(own)}")
    return "\n".join(out)


def _indent(text: str, spaces: int = 4) -> str:
    return "\n".join(" " * spaces + _l for _l in text.splitlines())


# --------------------------------------------------------------------------- #
# draft                                                                       #
# --------------------------------------------------------------------------- #
class Drafter:
    """Build skeleton requirements in the project's RST format."""

    def __init__(self, prefix: str, start: int, date: str, tests: TestIndex) -> None:
        self.prefix = prefix
        self.number = start
        self.date = date
        self.tests = tests
        self.chunks: list[str] = []

    def req(
        self,
        description: str,
        traces: list[str],
        tests: list[str],
        rationale: str = "TBD",
        note: str = "",
    ) -> None:
        """Append one requirement."""
        rid = f"PTW-GTK3-{self.prefix}-{self.number:03d}"
        self.number += 1
        desc = _wrap(description, 14)
        trace = _wrap(", ".join(f":ref:`{_t}`" for _t in traces), 14)
        test_lines = (
            "\n".join(
                ("" if _i == 0 else " " * 14) + f"``{_t}``"
                for _i, _t in enumerate(tests)
            )
            or "TBD"
        )
        rationale = _wrap(rationale, 14)
        self.chunks.append(
            f".. _{rid}:\n\n{rid}\n{'-' * len(rid)}\n\n"
            f":Description: {desc}\n"
            f":Rationale:   {rationale}\n"
            f":Traces to:   {trace}\n"
            ":Status:      Active\n"
            ":Version:     0.1.0\n"
            f":History:     0.1.0 ({self.date}) - Initial baseline.\n"
            f":Tests:       {test_lines}\n\n"
            + (".. " + note.replace("\n", "\n   ") + "\n\n" if note else "")
            + "----\n\n"
        )

    def section(self, title: str) -> None:
        """Append a section heading."""
        self.chunks.append(f"{title}\n{'=' * len(title)}\n\n")


def _wrap(text: str, indent: int, width: int = 72) -> str:
    """Wrap text for an RST field body, preserving bullet lists."""
    lines: list[str] = []
    for para in text.split("\n"):
        words, line = para.split(" "), ""
        for word in words:
            if line and len(line) + 1 + len(word) > width - indent:
                lines.append(line)
                line = ("  " if para.startswith("- ") else "") + word
            else:
                line = f"{line} {word}" if line else word
        lines.append(line)
    sep = "\n" + " " * indent
    return sep.join(lines).replace(sep + "\n", "\n\n")


def _pick(ids: list[str], *patterns: str) -> list[str]:
    return [
        _i
        for _i in ids
        if any(re.search(_p, _i.rsplit("::", 1)[-1]) for _p in patterns)
    ]


def draft(  # pylint: disable=too-many-locals
    pkg: PackageFacts, prefix: str, start: int, label: str, tests: TestIndex
) -> str:
    """Generate a skeleton requirements document for a package."""
    date = datetime.date.today().isoformat()
    d = Drafter(prefix, start, date, tests)
    title = pkg.name.split("/")[-1].capitalize()
    by_name = {_c.name: _c for _c in pkg.classes}
    if pkg.exports:
        d.section("Package")
        d.req(
            f"The ``pytkwrap.{pkg.name.replace('/', '.')}`` package **SHALL** export "
            + _join_names(sorted(pkg.exports))
            + " through ``__all__``. Sub-modules of the package **SHALL** import "
            "sibling modules directly and **SHALL NOT** import through the package "
            "``__init__.py``.",
            ["PTW-SR-W-001"],
            [],
            "A single public import location simplifies application code, while "
            "direct sibling imports avoid circular imports during package "
            "initialization.",
        )
    for fn in pkg.functions:
        d.section(fn.name)
        d.req(f"``{fn.signature}`` **SHALL** TBD. ({fn.summary})", ["PTW-SR-W-001"], [])
    for cls in [_c for _c in pkg.classes if not _c.is_mixin]:
        mixin = by_name.get(next(iter(cls.pytkwrap_bases), ""))
        ids = tests.node_ids(cls.name, cls.module)
        d.section(cls.name)
        owners = [_c for _c in (mixin, cls) if _c is not None]
        mixin_base = ", ".join(
            f"``{_b}``" for _b in (mixin.pytkwrap_bases if mixin else [])
        )
        desc = (
            f"The ``{cls.name}`` class **SHALL** combine ``{cls.native}`` and "
            f"``{', '.join(cls.pytkwrap_bases)}``"
            + (f", which derives from {mixin_base}" if mixin_base else "")
            + "."
        )
        params = ", ".join(f"``{_p}``" for _p in cls.init_params) or "no parameters"
        desc += (
            f" ``{cls.name}.__init__()`` **SHALL** accept {params} and **SHALL**:\n\n"
        )
        desc += "\n".join(f"- {_step_text(_s)}" for _s in cls.init_steps)
        d.req(
            desc,
            ["PTW-GTK3-W-001", "PTW-GTK3-W-017", "PTW-GTK3-W-018"],
            _pick(ids, r"^test_init"),
        )
        for owner in owners:
            _draft_owner(d, owner, ids)
    heading = f"GTK3 Layer — {title} Requirements"
    rule = "=" * len(heading)
    header = (
        f".. _{label}:\n\n{rule}\n{heading}\n{rule}\n\n"
        "This document defines the software requirements for the wrappers in the "
        f"``pytkwrap.{pkg.name.replace('/', '.')}`` package.\n\n"
        "All requirements in this document trace to one or more system "
        "requirements defined in :ref:`system_requirements` and to GTK3 layer "
        "widget requirements defined in :ref:`gtk3_widgets`.\n\n"
        ".. contents:: Contents\n   :local:\n   :depth: 1\n\n----\n\n"
    )
    body = "".join(d.chunks).rstrip()
    return header + body.removesuffix("----").rstrip() + "\n"


def _join_names(names: list[str]) -> str:
    quoted = [f"``{_n}``" for _n in names]
    return (
        quoted[0]
        if len(quoted) == 1
        else ", ".join(quoted[:-1]) + ", and " + quoted[-1]
    )


def _step_text(step: Step) -> str:
    text = f"``{step.text.removeprefix('self.')}``"
    return f"{text} only {step.guard}" if step.guard else text


def _draft_owner(d: Drafter, cls: ClassFacts, ids: list[str]) -> None:
    owner = f"``{cls.name}``"
    if cls.defaults or cls.attributes or cls.signals or cls.gobject_signals:
        parts = []
        if cls.defaults:
            parts.append(
                "**SHALL** define "
                + ", ".join(f"``{_k}`` as ``{_v}``" for _k, _v in cls.defaults.items())
            )
        if cls.attributes:
            parts.append(
                "**SHALL** set "
                + ", ".join(
                    f'``dic_attributes["{_k}"]`` to ``{_v}``'
                    for _k, _v in cls.attributes.items()
                )
            )
        if cls.signals:
            parts.append(
                "**SHALL** pre-register "
                + _join_names([f'"{_s}"' for _s in cls.signals]).replace('``"', '``"')
                + " in ``dic_handler_id`` with a value of ``-1``"
            )
        if cls.gobject_signals:
            parts.append(
                "**SHALL** define the custom ``GObject.Signal`` "
                + _join_names(cls.gobject_signals)
            )
        d.req(
            f"{owner} " + "; ".join(parts) + ".",
            ["PTW-SR-W-005", "PTW-GTK3-W-003", "PTW-GTK3-W-019"],
            _pick(ids, r"^test_init$", r"^test_do_set_attributes"),
        )
    if cls.properties or cls.set_properties:
        desc = ""
        if cls.properties:
            desc += (
                f"``{cls.name}.__init__()`` **SHALL** add the following "
                "properties to ``dic_properties``:\n\n"
            )
            desc += (
                "\n".join(f"- ``{_k}``: ``{_v}``" for _k, _v in cls.properties.items())
                + "\n\n"
            )
        if cls.set_properties:
            desc += f"``{cls.name}.do_set_properties()`` **SHALL**, in order:\n\n"
            desc += "\n".join(f"- {_step_text(_s)}" for _s in cls.set_properties)
        d.req(
            desc.strip(),
            ["PTW-SR-W-003", "PTW-SR-W-004", "PTW-GTK3-X-013"],
            _pick(
                ids, r"^test_do_set_properties$", r"^test_do_set_properties_default$"
            ),
        )
    for meth in cls.methods:
        if meth.name == "do_get_value":
            traces, pats = ["PTW-SR-W-006"], (r"^test_do_get_value",)
        elif meth.name == "do_set_value":
            traces, pats = ["PTW-SR-W-007", "PTW-COM-X-008"], (
                r"^test_do_set_value",
                r"^test_do_update$",
                r"^test_on_changed",
            )
        else:
            traces, pats = ["PTW-SR-W-002"], (rf"{meth.name.removeprefix('do_')}",)
        kind = "read-only property" if meth.is_property else "method"
        d.req(
            f"The ``{cls.name}.{meth.name}()`` {kind} **SHALL** TBD. "
            f"({meth.summary or 'no docstring'})",
            traces,
            _pick(ids, *pats),
            note="TODO: describe the behavior. Implementation for reference "
            "(this comment does not render):\n\n"
            + f"def {meth.signature}:\n"
            + _indent(meth.source),
        )


# --------------------------------------------------------------------------- #
# check                                                                       #
# --------------------------------------------------------------------------- #
@dataclass
class Finding:
    """One check result."""

    code: str
    location: str
    message: str

    @property
    def is_error(self) -> bool:
        """Return True for error-level findings."""
        return self.code.startswith("E")


REQ_BLOCK = re.compile(
    r"^\.\. _(PTW-[A-Z0-9-]+):\n\n(\S+)\n-+\n\n(.*?)(?=^\.\. _PTW-|^-{4,}\s*$|\Z)",
    re.M | re.S,
)
LABEL = re.compile(r"^\.\. _([A-Za-z0-9_-]+):", re.M)
REF = re.compile(r":ref:`(?:[^`<]*<)?([A-Za-z0-9_-]+)>?`")
FIELD = re.compile(r"^:([A-Za-z ]+):", re.M)
TEST_ID = re.compile(r"``(tests/[\w/]+\.py)::(\w+)(?:::(\w+))?``")


def check(  # pylint: disable=too-many-locals,too-many-branches
    config: dict, use_pytest: bool
) -> list[Finding]:
    """Run every documentation and source consistency check."""
    findings: list[Finding] = []
    docs = sorted(DOCS.rglob("*.rst"))
    texts = {_d: _d.read_text() for _d in docs}
    labels: dict[str, Path] = {}
    for doc, text in texts.items():
        for match in LABEL.finditer(text):
            name = match.group(1)
            line = text.count("\n", 0, match.start()) + 1
            if name in labels:
                findings.append(
                    Finding(
                        "E001",
                        f"{_rel(doc)}:{line}",
                        f"duplicate label {name} (also {_rel(labels[name])})",
                    )
                )
            labels[name] = doc
    collected = _pytest_ids() if use_pytest else None
    tests = TestIndex()
    series: dict[str, set[int]] = {}
    for doc, text in texts.items():
        for match in REF.finditer(text):
            if match.group(1) not in labels and match.group(1).lower() not in {
                _l.lower() for _l in labels
            }:
                findings.append(
                    Finding(
                        "E003",
                        _loc(doc, text, match.start()),
                        f"unresolved :ref: {match.group(1)}",
                    )
                )
        for block in REQ_BLOCK.finditer(text):
            rid, heading, body = block.groups()
            loc = _loc(doc, text, block.start())
            if heading != rid:
                findings.append(
                    Finding(
                        "E002", loc, f"heading '{heading}' does not match label {rid}"
                    )
                )
            prefix, _, num = rid.rpartition("-")
            if num.isdigit():
                series.setdefault(prefix, set()).add(int(num))
            fields = {_f.strip() for _f in FIELD.findall(body)}
            for missing in [_f for _f in REQUIRED_FIELDS if _f not in fields]:
                findings.append(Finding("E004", loc, f"{rid} missing :{missing}:"))
            for bad in [_f for _f in FORBIDDEN_FIELDS if _f in fields]:
                findings.append(
                    Finding("E004", loc, f"{rid} has forbidden :{bad}: field")
                )
            status = re.search(r"^:Status:\s+(\S+)", body, re.M)
            if status and status.group(1) not in VALID_STATUS:
                findings.append(
                    Finding(
                        "E005", loc, f"{rid} has unknown status '{status.group(1)}'"
                    )
                )
            tests_field = body.split(":Tests:", 1)[-1] if ":Tests:" in body else ""
            for tmatch in TEST_ID.finditer(tests_field):
                findings += _check_test(rid, loc, tmatch, tests, collected)
    for prefix, numbers in series.items():
        gaps = sorted(set(range(1, max(numbers) + 1)) - numbers)
        if gaps:
            findings.append(Finding("W101", prefix, f"ID gaps: {_ranges(gaps)}"))
    findings += _check_coverage(texts, config)
    findings += _check_stubs(config)
    return findings


def _rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _loc(doc: Path, text: str, offset: int) -> str:
    return f"{_rel(doc)}:{text.count(chr(10), 0, offset) + 1}"


def _ranges(numbers: list[int]) -> str:
    out, start = [], numbers[0]
    for prev, cur in zip(numbers, numbers[1:] + [None], strict=True):
        if cur != prev + 1:
            out.append(f"{start:03d}" if start == prev else f"{start:03d}-{prev:03d}")
            start = cur
    return ", ".join(out)


def _pytest_ids() -> set[str]:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "--collect-only",
            "-q",
            "-p",
            "no:cacheprovider",
            "tests",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {_l.strip() for _l in result.stdout.splitlines() if "::" in _l}


def _check_test(
    rid: str, loc: str, match: re.Match, tests: TestIndex, collected: set[str] | None
) -> list[Finding]:
    file, cls, meth = match.groups()
    node = f"{file}::{cls}" + (f"::{meth}" if meth else "")
    path = ROOT / file
    problem = ""
    if not path.exists():
        problem = f"missing test file {file}"
    elif collected is not None:
        if node not in collected and not any(
            _c.startswith((node + "::", node + "[")) for _c in collected
        ):
            problem = f"missing test {node}"
    elif meth is None and cls.startswith("test_"):
        module = tests.file(path).get(MODULE)
        if module is None or cls not in module.methods:
            problem = f"missing test function {node}"
    else:
        methods = tests.methods(path, cls)
        if methods is None:
            problem = f"missing test class {file}::{cls}"
        elif meth and meth not in methods:
            problem = f"missing test {node}"
    return [Finding("E006", loc, f"{rid} cites {problem}")] if problem else []


def _all_source_facts(config: dict) -> list[ClassFacts]:
    classes: list[ClassFacts] = []
    for module in sorted((SRC / "gtk3").rglob("*.py")):
        if module.name != "__init__.py" and not excluded(module, config):
            classes += parse_module(module)[0]
    return classes


def _check_coverage(texts: dict[Path, str], config: dict) -> list[Finding]:
    findings: list[Finding] = []
    req_texts = {_d: _t for _d, _t in texts.items() if "PTW-" in _t}
    by_module: dict[str, list[ClassFacts]] = {}
    for cls in _all_source_facts(config):
        by_module.setdefault(cls.module, []).append(cls)
    for module, classes in by_module.items():
        wrappers = [_c for _c in classes if not _c.is_mixin and _c.native]
        names = [_c.name for _c in classes]
        docs = [_t for _t in req_texts.values() if any(f"``{_n}" in _t for _n in names)]
        for wrapper in wrappers:
            if not any(f"``{wrapper.name}" in _t for _t in docs):
                findings.append(
                    Finding(
                        "W102",
                        f"{module}:{wrapper.lineno}",
                        f"{wrapper.name} is not covered by any requirement",
                    )
                )
        if not docs:
            continue
        joined = "\n".join(docs)
        for cls in classes:
            for sig in cls.signals + cls.gobject_signals:
                if f'"{sig}"' not in joined and f"``{sig}``" not in joined:
                    findings.append(
                        Finding(
                            "W103",
                            f"{module}:{cls.lineno}",
                            f"{cls.name} signal '{sig}' not in its requirements",
                        )
                    )
            for key in list(cls.properties) + list(cls.attributes):
                if f"``{key}``" not in joined and f'"{key}"' not in joined:
                    findings.append(
                        Finding(
                            "W103",
                            f"{module}:{cls.lineno}",
                            f"{cls.name} key '{key}' not in its requirements",
                        )
                    )
    return findings


def _check_stubs(config: dict) -> list[Finding]:
    findings: list[Finding] = []
    defined = {_c.name for _c in _all_source_facts(config)} | _defined_elsewhere()
    for stub in sorted(SRC.rglob("*.pyi")):
        module = stub.with_suffix(".py")
        if not module.exists() or excluded(module, config):
            continue
        real = {_c.name: _c for _c in parse_module(module)[0]}
        try:
            stub_classes = {_c.name: _c for _c in parse_module(stub)[0]}
        except SyntaxError as exc:
            findings.append(Finding("E104", _rel(stub), f"stub does not parse: {exc}"))
            continue
        for name, scls in stub_classes.items():
            loc = f"{_rel(stub)}:{scls.lineno}"
            for base in scls.pytkwrap_bases:
                if PYTKWRAP_NAME.match(base) and base not in defined:
                    findings.append(
                        Finding(
                            "E105",
                            loc,
                            f"{name} base '{base}' is not defined in any .py module",
                        )
                    )
            if name not in real:
                findings.append(
                    Finding(
                        "W104",
                        loc,
                        f"{name} is declared in the stub but not in {module.name}",
                    )
                )
                continue
            if scls.bases != real[name].bases:
                findings.append(
                    Finding(
                        "W104",
                        loc,
                        f"{name} bases {scls.bases} != code {real[name].bases}",
                    )
                )
            if _param_names(scls) != _param_names(real[name]):
                findings.append(
                    Finding(
                        "W104",
                        loc,
                        f"{name}.__init__ params {_param_names(scls)} "
                        f"!= code {_param_names(real[name])}",
                    )
                )
        for name in set(real) - set(stub_classes):
            findings.append(
                Finding("W104", _rel(stub), f"{name} is missing from the stub")
            )
    return findings


def _param_names(cls: ClassFacts) -> list[str]:
    return [re.split(r"[:=]", _p)[0].strip() for _p in cls.init_params]


def _defined_elsewhere() -> set[str]:
    names: set[str] = set()
    for module in SRC.rglob("*.py"):
        try:
            tree = ast.parse(module.read_text())
        except SyntaxError:
            continue
        names |= {_n.name for _n in tree.body if isinstance(_n, ast.ClassDef)}
    return names


# --------------------------------------------------------------------------- #
# CLI                                                                         #
# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:  # pylint: disable=too-many-locals
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="reqtool", description=__doc__.split("\n\n", 1)[0]
    )
    sub = parser.add_subparsers(dest="command", required=True)
    p_facts = sub.add_parser("facts", help="print requirement facts for packages")
    p_facts.add_argument("packages", nargs="+")
    p_facts.add_argument(
        "--json", action="store_true", help="emit JSON instead of Markdown"
    )
    p_draft = sub.add_parser("draft", help="generate a skeleton requirements document")
    p_draft.add_argument("package")
    p_draft.add_argument(
        "--prefix", required=True, help="ID series, e.g. FNT for PTW-GTK3-FNT-001"
    )
    p_draft.add_argument(
        "--start", type=int, default=1, help="first ID number (default 1)"
    )
    p_draft.add_argument("--label", help="document label (default gtk3_<package>)")
    p_draft.add_argument(
        "-o", "--output", type=Path, help="write to a file (refuses to overwrite)"
    )
    p_check = sub.add_parser("check", help="validate requirements documents and stubs")
    p_check.add_argument(
        "--pytest",
        action="store_true",
        help="verify test IDs with pytest --collect-only",
    )
    p_check.add_argument("--errors-only", action="store_true", help="hide warnings")
    p_check.add_argument(
        "--select", help="comma-separated code prefixes to show, e.g. E,W103"
    )
    args = parser.parse_args(argv)
    config = load_config()
    tests = TestIndex()

    if args.command == "facts":
        pkgs = [package_facts(_p, config) for _p in args.packages]
        if args.json:
            print(json.dumps([asdict(_p) for _p in pkgs], indent=2))
        else:
            print("\n\n".join(format_facts(_p, tests) for _p in pkgs))
        return 0

    if args.command == "draft":
        pkg = package_facts(args.package, config)
        label = args.label or "gtk3_" + pkg.name.split("/")[-1]
        text = draft(pkg, args.prefix, args.start, label, tests)
        if args.output:
            if args.output.exists():
                raise SystemExit(
                    f"reqtool: {args.output} exists; refusing to overwrite"
                )
            args.output.write_text(text)
            print(f"wrote {args.output}")
        else:
            print(text)
        return 0

    findings = list(
        {
            (_f.code, _f.location, _f.message): _f for _f in check(config, args.pytest)
        }.values()
    )
    if args.errors_only:
        findings = [_f for _f in findings if _f.is_error]
    if args.select:
        prefixes = tuple(args.select.split(","))
        findings = [_f for _f in findings if _f.code.startswith(prefixes)]
    for finding in sorted(findings, key=lambda _f: (_f.code, _f.location)):
        print(f"{finding.code} {finding.location}: {finding.message}")
    errors = sum(_f.is_error for _f in findings)
    print(f"\n{errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
