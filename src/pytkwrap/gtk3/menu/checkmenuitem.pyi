# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin as GTK3MenuItemMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3CheckMenuItemMixin(GTK3MenuItemMixin):
    _GTK3_CHECKMENUITEM_PROPERTIES: Incomplete
    _GTK3_CHECKMENUITEM_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3CheckMenuItem(Gtk.CheckMenuItem, GTK3CheckMenuItemMixin):
    def __init__(self) -> None: ...
