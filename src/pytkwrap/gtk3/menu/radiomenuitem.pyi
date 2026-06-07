# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.checkmenuitem import GTK3CheckMenuItem as GTK3CheckMenuItem
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3RadioMenuItem(Gtk.RadioMenuItem, GTK3CheckMenuItem):
    _GTK3_RADIOMENUITEM_PROPERTIES: Incomplete
    _GTK3_RADIOMENUITEM_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
