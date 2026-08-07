# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.checkmenuitem import (
    GTK3CheckMenuItemMixin as GTK3CheckMenuItemMixin,
)
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3RadioMenuItemMixin(GTK3CheckMenuItemMixin):
    _GTK3_RADIOMENUITEM_PROPERTIES: Incomplete
    _GTK3_RADIOMENUITEM_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3RadioMenuItem(Gtk.RadioMenuItem, GTK3RadioMenuItemMixin):
    def __init__(
        self, group: Gtk.RadioMenuItem | None = None, label: str = ""
    ) -> None: ...
