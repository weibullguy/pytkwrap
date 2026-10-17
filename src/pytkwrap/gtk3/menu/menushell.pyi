# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.menu.menubuilder import get_gio_menu_model as get_gio_menu_model
from pytkwrap.gtk3.menu.menubuilder import get_gtk_menu_items as get_gtk_menu_items
from pytkwrap.gtk3.menu.menuloader import (
    do_build_menu_from_file as do_build_menu_from_file,
)
from pytkwrap.gtk3.menu.models import GTK3MenuShellAttribute as GTK3MenuShellAttribute
from pytkwrap.gtk3.menu.models import GTK3MenuShellItem as GTK3MenuShellItem
from pytkwrap.gtk3.menu.models import GTK3MenuShellMenu as GTK3MenuShellMenu
from pytkwrap.gtk3.menu.models import GTK3MenuShellSection as GTK3MenuShellSection
from pytkwrap.gtk3.menu.models import GTK3MenuShellSubmenu as GTK3MenuShellSubmenu
from pytkwrap.gtk3.menu.models import Node as Node

__all__ = [
    "do_build_menu_from_file",
    "get_gio_menu_model",
    "get_gtk_menu_items",
    "GTK3MenuShellAttribute",
    "GTK3MenuShellItem",
    "GTK3MenuShellMenu",
    "GTK3MenuShellSection",
    "GTK3MenuShellSubmenu",
    "Node",
    "GTK3MenuShellMixin",
    "GTK3MenuShell",
]

class GTK3MenuShellMixin(GTK3ContainerMixin):
    _GTK3_MENUSHELL_PROPERTIES: Incomplete
    _GTK3_MENUSHELL_SIGNALS: Incomplete
    menu_id: str | None
    menu_model: Gio.MenuModel | None
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_build_menu(
        self,
        menu: GTK3MenuShellMenu | None = None,
        menu_file: str = "",
        method: str = "gio",
    ): ...
    @staticmethod
    def _resolve_menu(
        menu: GTK3MenuShellMenu | None, menu_file: str, method: str
    ) -> GTK3MenuShellMenu: ...
    def _build_gio_menu(self, menu: GTK3MenuShellMenu) -> None: ...
    def _build_gtk_menu(self, menu: GTK3MenuShellMenu) -> None: ...

class GTK3MenuShell(Gtk.MenuShell, GTK3MenuShellMixin):
    def __init__(self) -> None: ...
