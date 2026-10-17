"""Data structures describing GTK3 menu trees."""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class GTK3MenuShellAttribute:  # pylint: disable=too-many-instance-attributes
    """Attributes supported by menu items, sections, and submenus."""

    action: str | None = None
    action_namespace: str | None = None
    callback: Callable | None = None
    custom: str | None = None
    display_hint: str | None = None
    hidden_when: str | None = None
    icon: str | None = None
    id: str | None = None
    label: str | None = None
    signal: str | None = None
    submenu_action: str | None = None
    target: str | None = None
    text_direction: str | None = None
    translatable: str = "yes"
    use_markup: bool = False


@dataclass
class GTK3MenuShellItem:
    """A leaf item in a GTK3 menu tree."""

    attributes: GTK3MenuShellAttribute


@dataclass
class GTK3MenuShellSection:
    """A section containing menu items or nested submenus."""

    children: list[Node] = field(default_factory=list)
    attributes: GTK3MenuShellAttribute | None = None


@dataclass
class GTK3MenuShellSubmenu:
    """A submenu containing one or more sections."""

    attributes: GTK3MenuShellAttribute
    sections: list[GTK3MenuShellSection] = field(default_factory=list)


@dataclass
class GTK3MenuShellMenu:
    """A top-level menu containing submenus."""

    submenus: list[GTK3MenuShellSubmenu]
    id: str | None = None


Node = GTK3MenuShellItem | GTK3MenuShellSubmenu
