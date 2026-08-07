# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menushell import GTK3MenuShellMixin as GTK3MenuShellMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3MenuMixin(GTK3MenuShellMixin):
    _GTK3_MENU_PROPERTIES: Incomplete
    _GTK3_MENU_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3Menu(Gtk.Menu, GTK3MenuMixin):
    def __init__(self) -> None: ...
