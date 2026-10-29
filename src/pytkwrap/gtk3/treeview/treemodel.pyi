# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes

class GTK3TreeModelMixin(GTK3GObjectMixin):
    _GTK3_TREEMODEL_ATTRIBUTES: Incomplete
    type: str
    def __init__(self, **kwargs) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object]) -> None: ...
    def do_insert_row(
        self,
        values: list[object],
        position: int | None = None,
        columns: list[int] | None = None,
        parent: Gtk.TreeIter | None = None,
        sibling: Gtk.TreeIter | None = None,
        after: bool | None = None,
    ) -> Gtk.TreeIter | None: ...
    def do_move_row(
        self,
        row: Gtk.TreeIter,
        position: Gtk.TreeIter | None,
        swap: bool = False,
        after: bool = True,
    ) -> None: ...
    def _insert_liststore_row(
        self, values, position, columns, sibling, after
    ) -> Gtk.TreeIter | None: ...
    def _insert_treestore_row(
        self, values, position, columns, parent, sibling, after
    ) -> Gtk.TreeIter | None: ...
