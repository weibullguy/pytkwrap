# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menushell import GTK3MenuShell as GTK3MenuShell
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3MenuBar(Gtk.MenuBar, GTK3MenuShell):
    _GTK3_MENUBAR_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
