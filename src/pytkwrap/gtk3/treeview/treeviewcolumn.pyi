# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer as GTK3CellRenderer

class GTK3TreeViewColumnMixin(GTK3GObjectMixin):
    _GTK3_TREEVIEWCOLUMN_PROPERTIES: Incomplete
    _GTK3_TREEVIEWCOLUMN_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    @property
    def button(self) -> Gtk.Button | None: ...
    @property
    def treeview(self) -> Gtk.TreeView | None: ...
    @property
    def width(self) -> int: ...
    @property
    def x_offset(self) -> int: ...

class GTK3TreeViewColumn(Gtk.TreeViewColumn, GTK3TreeViewColumnMixin):
    def __init__(
        self,
        title: str = "",
        cell_renderer: GTK3CellRenderer | None = None,
        cell_area: Gtk.CellArea | None = None,
    ) -> None: ...
