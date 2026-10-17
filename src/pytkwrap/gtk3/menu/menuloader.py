"""Load GTK3 menu trees from various file formats."""

# Standard Library Imports
import importlib
import inspect
import sys
from collections.abc import Callable, Mapping
from pathlib import Path
from types import FrameType
from typing import Any, cast

# pytkwrap Package Imports
from pytkwrap.exceptions import MenuError, WrongTypeError, raise_pytkwrap_exception
from pytkwrap.gtk3.menu.models import (
    GTK3MenuShellAttribute,
    GTK3MenuShellItem,
    GTK3MenuShellMenu,
    GTK3MenuShellSection,
    GTK3MenuShellSubmenu,
    Node,
)

_TOML = cast(
    Any,
    importlib.import_module("tomllib" if sys.version_info >= (3, 11) else "tomli"),
)


def _as_mapping(value: object, context: str) -> Mapping[str, object]:
    """Validate and return a TOML table.

    Parameters
    ----------
    value : object
        Value to validate as a mapping with string keys.
    context : str
        Description of the value, used in error messages.

    Returns
    -------
    Mapping[str, object]
        The validated mapping.
    """
    if not isinstance(value, Mapping):
        raise_pytkwrap_exception(
            f"{context} must be a TOML table.",
            error_type=WrongTypeError,
        )

    if not all(isinstance(_key, str) for _key in value):
        raise_pytkwrap_exception(
            f"{context} keys must be strings.",
            error_type=WrongTypeError,
        )

    return {str(_key): _item for _key, _item in value.items()}


def _as_list(value: object, context: str) -> list[object]:
    """Validate and return a TOML array.

    Parameters
    ----------
    value : object
        Value to validate as a list.
    context : str
        Description of the value, used in the error message.

    Returns
    -------
    list[object]
        The validated list.
    """
    if not isinstance(value, list):
        raise_pytkwrap_exception(
            f"{context} must be a TOML array.",
            error_type=WrongTypeError,
        )

    return value


def _optional_string(
    data: Mapping[str, object],
    key: str,
    context: str,
) -> str | None:
    """Read an optional string value from a mapping.

    Parameters
    ----------
    data : Mapping[str, object]
        Mapping containing the value.
    key : str
        Name of the value to retrieve.
    context : str
        Description of the mapping, used in the error message.

    Returns
    -------
    str or None
        The string value, or ``None`` if it is absent or explicitly ``None``.
    """
    value = data.get(key)
    if value is not None and not isinstance(value, str):
        raise_pytkwrap_exception(
            f"{context}.{key} must be a string.",
            error_type=WrongTypeError,
        )

    return value


def _required_mapping(
    data: Mapping[str, object],
    key: str,
    context: str,
) -> Mapping[str, object]:
    """Read and validate a required nested table.

    Parameters
    ----------
    data : Mapping[str, object]
        Mapping containing the required table.
    key : str
        Name of the required table.
    context : str
        Description of the parent mapping, used in error messages.

    Returns
    -------
    Mapping[str, object]
        The validated nested mapping.
    """
    if key not in data:
        raise_pytkwrap_exception(
            f"{context} is missing required table {key!r}.", error_type=MenuError
        )

    return _as_mapping(data[key], f"{context}.{key}")


def _callback_root(name: str, frame: FrameType) -> object | None:
    """Find a callback reference's root object in one stack frame.

    Parameters
    ----------
    name : str
        Dotted callback reference, such as ``on_open`` or ``self.on_open``.
    frame : FrameType
        Frame whose local and global namespaces are searched.

    Returns
    -------
    object or None
        The root object from the frame's locals or globals, or ``None`` if
        it cannot be found.

    Notes
    -----
    A leading ``self`` is looked up only in the frame's local namespace.
    """
    _parts = name.split(".")

    if _parts[0] == "self":
        return frame.f_locals.get("self")

    if _parts[0] in frame.f_locals:
        return frame.f_locals[_parts[0]]

    return frame.f_globals.get(_parts[0])


def _follow_callback_path(name: str, root: object) -> Callable[..., Any] | None:
    """Resolve the attributes following a callback reference's root.

    Parameters
    ----------
    name : str
        Dotted callback reference.
    root : object
        Object corresponding to the first component of ``name``.

    Returns
    -------
    Callable or None
        The resolved callable, or ``None`` if an attribute in the path does
        not exist.
    """
    _value = root

    try:
        for _attribute in name.split(".")[1:]:
            _value = getattr(_value, _attribute)
    except AttributeError:
        return None

    if callable(_value):
        return _value

    raise_pytkwrap_exception(f"Callback reference {name!r} is not callable.")


def _callback_in_frame(
    name: str,
    frame: FrameType,
) -> Callable[..., Any] | None:
    """Resolve a callback reference in one frame.

    Parameters
    ----------
    name : str
        Dotted callback reference.
    frame : FrameType
        Frame whose local and global namespaces are searched.

    Returns
    -------
    Callable or None
        The resolved callable, or ``None`` if its root or an attribute in
        its path is absent.
    """
    _root = _callback_root(name, frame)

    if _root is None:
        return None

    return _follow_callback_path(name, _root)


def _callback_parts(name: str) -> list[str]:
    """Validate and split a dotted callback reference.

    Parameters
    ----------
    name : str
        Callback reference to validate.

    Returns
    -------
    list[str]
        The identifier components of the callback reference.
    """
    _parts = name.split(".")

    if not all(_part.isidentifier() for _part in _parts) or (
        _parts[0] == "self" and len(_parts) == 1
    ):
        raise_pytkwrap_exception(
            f"Invalid callback reference {name!r}.", error_type=MenuError
        )

    return _parts


def _resolve_callback_from_stack(
    name: str,
    frame: FrameType | None,
) -> Callable[..., Any] | None:
    """Search a frame and its callers for a callback reference.

    Parameters
    ----------
    name : str
        Dotted callback reference to resolve.
    frame : FrameType or None
        First frame to search; its callers are searched in turn.

    Returns
    -------
    Callable or None
        The matching callable, or ``None`` if no frame contains it.
    """
    while frame is not None:
        _callback = _callback_in_frame(name, frame)

        if _callback is not None:
            return _callback

        frame = frame.f_back

    return None


def _resolve_callback(name: str) -> Callable[..., Any]:
    """Resolve a callback by searching caller scopes without evaluating code.

    Parameters
    ----------
    name : str
        Dotted callback reference to resolve.

    Returns
    -------
    Callable
        The resolved callback.

    Notes
    -----
    The current frame is excluded from the search. The temporary frame
    reference is deleted before returning to avoid retaining stack frames.
    """
    _callback_parts(name)
    _frame = inspect.currentframe()

    try:
        _caller = _frame.f_back if _frame is not None else None
        _callback = _resolve_callback_from_stack(name, _caller)

        if _callback is None:
            raise_pytkwrap_exception(
                f"Could not resolve callback reference " f"{name!r}.",
                error_type=MenuError,
            )

        return _callback
    finally:
        del _frame


def _attributes_from_data(
    data: Mapping[str, object],
    context: str,
) -> GTK3MenuShellAttribute:
    """Build menu attributes from a validated data mapping.

    Parameters
    ----------
    data : Mapping[str, object]
        Attribute names and values from the menu document.
    context : str
        Location description used in validation error messages.

    Returns
    -------
    GTK3MenuShellAttribute
        The constructed menu attributes.
    """
    _valid_keys = {
        "action",
        "action_namespace",
        "callback",
        "custom",
        "display_hint",
        "hidden_when",
        "icon",
        "id",
        "label",
        "signal",
        "submenu_action",
        "target",
        "text_direction",
        "translatable",
        "use_markup",
    }
    _unknown_keys = data.keys() - _valid_keys
    if _unknown_keys:
        raise_pytkwrap_exception(
            f"{context} has unknown attributes: {sorted(_unknown_keys)}",
            error_type=MenuError,
        )

    _callback_name = _optional_string(data, "callback", context)
    _translatable = data.get("translatable", "yes")
    if not isinstance(_translatable, str):
        raise_pytkwrap_exception(
            f"{context}.translatable must be a string.",
            error_type=WrongTypeError,
        )

    _use_markup = data.get("use_markup", False)
    if not isinstance(_use_markup, bool):
        raise_pytkwrap_exception(
            f"{context}.use_markup must be a boolean.",
            error_type=WrongTypeError,
        )

    return GTK3MenuShellAttribute(
        action=_optional_string(data, "action", context),
        action_namespace=_optional_string(data, "action_namespace", context),
        callback=(
            _resolve_callback(_callback_name) if _callback_name is not None else None
        ),
        custom=_optional_string(data, "custom", context),
        display_hint=_optional_string(data, "display_hint", context),
        hidden_when=_optional_string(data, "hidden_when", context),
        icon=_optional_string(data, "icon", context),
        id=_optional_string(data, "id", context),
        label=_optional_string(data, "label", context),
        signal=_optional_string(data, "signal", context),
        submenu_action=_optional_string(data, "submenu_action", context),
        target=_optional_string(data, "target", context),
        text_direction=_optional_string(data, "text_direction", context),
        translatable=_translatable,
        use_markup=_use_markup,
    )


def _node_from_data(
    data: Mapping[str, object],
    context: str,
) -> Node:
    """Build a menu item or submenu from a data mapping.

    Parameters
    ----------
    data : Mapping[str, object]
        Node data. The mapping must contain an ``attributes`` table; a
        ``sections`` key makes the node a submenu.
    context : str
        Location description used in validation error messages.

    Returns
    -------
    Node
        The constructed item or submenu.
    """
    _attributes = _attributes_from_data(
        _required_mapping(data, "attributes", context),
        f"{context}.attributes",
    )

    if "sections" not in data:
        return GTK3MenuShellItem(attributes=_attributes)

    return GTK3MenuShellSubmenu(
        attributes=_attributes,
        sections=[
            _section_from_data(
                _as_mapping(_section, f"{context}.sections[{_index}]"),
                f"{context}.sections[{_index}]",
            )
            for _index, _section in enumerate(
                _as_list(data["sections"], f"{context}.sections")
            )
        ],
    )


def _section_from_data(
    data: Mapping[str, object],
    context: str,
) -> GTK3MenuShellSection:
    """Build a menu section from a data mapping.

    Parameters
    ----------
    data : Mapping[str, object]
        Section data. ``attributes`` is optional and ``children`` defaults
        to an empty array.
    context : str
        Location description used in validation error messages.

    Returns
    -------
    GTK3MenuShellSection
        The constructed section and its child nodes.
    """
    _raw_attributes = data.get("attributes")
    _attributes: GTK3MenuShellAttribute | None = None

    if _raw_attributes is not None:
        _attributes = _attributes_from_data(
            _as_mapping(_raw_attributes, f"{context}.attributes"),
            f"{context}.attributes",
        )

    _children = _as_list(data.get("children", []), f"{context}.children")

    return GTK3MenuShellSection(
        attributes=_attributes,
        children=[
            _node_from_data(
                _as_mapping(_child, f"{context}.children[{_index}]"),
                f"{context}.children[{_index}]",
            )
            for _index, _child in enumerate(_children)
        ],
    )


def _submenu_from_data(
    data: Mapping[str, object],
    context: str,
) -> GTK3MenuShellSubmenu:
    """Build and validate a submenu from a data mapping.

    Parameters
    ----------
    data : Mapping[str, object]
        Submenu data, including its attributes and sections.
    context : str
        Location description used in validation error messages.

    Returns
    -------
    GTK3MenuShellSubmenu
        The constructed submenu.
    """
    _node = _node_from_data(data, context)

    if not isinstance(_node, GTK3MenuShellSubmenu):
        raise_pytkwrap_exception(
            f"{context} must contain sections to be a submenu.",
            error_type=MenuError,
        )

    return _node


def do_build_menu_from_file(filename: str | Path) -> GTK3MenuShellMenu:
    """Load a GTK3 menu structure from a TOML file.

    Parameters
    ----------
    filename : str | Path
        The path to the TOML file containing a ``[menu]`` table.

    Returns
    -------
    GTK3MenuShellMenu
        The menu object described by the TOML data.

    Notes
    -----
    A node with a ``sections`` key is interpreted as a submenu; other child nodes
    are interpreted as menu items. Callback names are resolved from the calling
    context, so ``on_open`` refers to a callable in its namespace and
    ``self.on_open`` refers to a callable on its ``self`` object. Names are resolved
    without evaluating Python expressions.
    """
    if not isinstance(filename, (str, Path)):
        raise_pytkwrap_exception(
            "filename must be a string or pathlib.Path.",
            error_type=WrongTypeError,
        )

    try:
        with Path(filename).open("rb") as _file:
            _raw_document = _TOML.load(_file)
    except (OSError, ValueError) as exc:
        raise_pytkwrap_exception(
            f"Could not load menu TOML file {filename!s}: {exc}",
            cause=exc,
            error_type=MenuError,
        )

    _document = _as_mapping(_raw_document, "TOML document")

    _menu = _as_mapping(_document.get("menu"), "menu")
    _submenu_data = _as_list(_menu.get("submenus", []), "menu.submenus")

    return GTK3MenuShellMenu(
        id=_optional_string(_menu, "id", "menu"),
        submenus=[
            _submenu_from_data(
                _as_mapping(_submenu, f"menu.submenus[{_index}]"),
                f"menu.submenus[{_index}]",
            )
            for _index, _submenu in enumerate(_submenu_data)
        ],
    )
