# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer as GTK3CellRenderer
from pytkwrap.gtk3.treeview.cellrenderercombo import (
    GTK3CellRendererCombo as GTK3CellRendererCombo,
)
from pytkwrap.gtk3.treeview.cellrendererpixbuf import (
    GTK3CellRendererPixbuf as GTK3CellRendererPixbuf,
)
from pytkwrap.gtk3.treeview.cellrendererprogress import (
    GTK3CellRendererProgress as GTK3CellRendererProgress,
)
from pytkwrap.gtk3.treeview.cellrendererspin import (
    GTK3CellRendererSpin as GTK3CellRendererSpin,
)
from pytkwrap.gtk3.treeview.cellrendererspinner import (
    GTK3CellRendererSpinner as GTK3CellRendererSpinner,
)
from pytkwrap.gtk3.treeview.cellrenderertext import (
    GTK3CellRendererText as GTK3CellRendererText,
)
from pytkwrap.gtk3.treeview.cellrenderertoggle import (
    GTK3CellRendererToggle as GTK3CellRendererToggle,
)
from pytkwrap.gtk3.treeview.liststore import GTK3ListStore as GTK3ListStore
from pytkwrap.gtk3.treeview.treestore import GTK3TreeStore as GTK3TreeStore
from pytkwrap.gtk3.treeview.treeviewcolumn import (
    GTK3TreeViewColumn as GTK3TreeViewColumn,
)

class GTK3TreeViewMixin(GTK3ContainerMixin):
    _GTK3_TREEVIEW_PROPERTIES: Incomplete
    _GTK3_TREEVIEW_SIGNALS: Incomplete
    attr_map: dict[GTK3CellRenderer, dict[str, int]]
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_add_column(
        self,
        column: GTK3TreeViewColumn | None = None,
        position: int = -1,
        title: str | None = None,
        cell: GTK3CellRenderer | None = None,
        **kwargs,
    ) -> int: ...
    def do_add_row(
        self,
        values: list[object],
        position: int | None = None,
        columns: list[int] | None = None,
        parent: Gtk.TreeIter | None = None,
        sibling: Gtk.TreeIter | None = None,
        after: bool | None = None,
    ) -> Gtk.TreeIter: ...
    def do_collapse_row(self, path: Gtk.TreePath | None = None) -> bool | None: ...
    def do_expand_row(
        self, path: Gtk.TreePath | None = None, open_all: bool = False
    ) -> bool | None: ...
    def do_move_column(
        self, column: GTK3TreeViewColumn, base_column: GTK3TreeViewColumn | None
    ) -> None: ...
    def do_remove_column(self, column: GTK3TreeViewColumn) -> int: ...
    def do_scroll(
        self,
        path: Gtk.TreePath | None,
        column: GTK3TreeViewColumn | None,
        use_align: bool,
        row_align: float,
        col_align: float,
        tree_x: int = -1,
        tree_y: int = -1,
    ) -> None: ...
    @property
    def columns(self) -> list[Gtk.TreeViewColumn]: ...
    @property
    def n_columns(self) -> int: ...
    @property
    def selection(self) -> Gtk.TreeSelection: ...
    @property
    def visible_range(self) -> tuple[Gtk.TreePath, Gtk.TreePath] | None: ...
    @property
    def visible_rect(self) -> Gdk.Rectangle: ...

class GTK3TreeView(Gtk.TreeView, GTK3TreeViewMixin):
    def __init__(self, model: Gtk.TreeModel = None) -> None: ...

def do_construct_treeview(
    column_types: list[GObject.GType],
    renderer_types: list[str],
    attributes: list[dict[str, int]],
    headers: list[str],
    tree: bool = True,
) -> GTK3TreeView: ...
