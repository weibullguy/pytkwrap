# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

class GTK3CellView(Gtk.CellView, GTK3Widget):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_CELLVIEW_PROPERTIES: Incomplete
    def __init__(self, cell_area_context: Gtk.CellAreaContext = None) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
