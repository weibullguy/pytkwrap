# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.treeview.treemodel import GTK3TreeModelMixin as GTK3TreeModelMixin

class GTK3TreeStore(Gtk.TreeStore, GTK3TreeModelMixin):
    type: str
    def __init__(
        self, column_types: list[GObject.GType] | None, n_columns: int, n_rows: int
    ) -> None: ...
