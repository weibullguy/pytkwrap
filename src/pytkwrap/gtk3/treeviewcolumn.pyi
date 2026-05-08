# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.cellrenderer import GTK3CellRenderer as GTK3CellRenderer
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3TreeViewColumn(Gtk.TreeViewColumn, GTK3GObjectMixin):
    _GTK3_TREEVIEWCOLUMN_PROPERTIES: Incomplete
    _GTK3_TREEVIEWCOLUMN_SIGNALS: Incomplete
    def __init__(
        self,
        title: str = "",
        cell_renderer: GTK3CellRenderer | None = None,
        cell_area: Gtk.CellArea | None = None,
    ) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: GTK3WidgetProperties | dict | list[list | tuple]
    ) -> None: ...
