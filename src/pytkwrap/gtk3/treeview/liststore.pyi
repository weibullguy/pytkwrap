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

class GTK3ListStoreMixin(GTK3GObjectMixin):
    _GTK3_LISTSTORE_ATTRIBUTES: Incomplete
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
        sibling: Gtk.TreeIter | None = None,
        after: bool | None = None,
    ) -> Gtk.TreeIter: ...
    def do_move_row(
        self,
        iter: Gtk.TreeIter,
        position: Gtk.TreeIter | None,
        swap: bool = False,
        after: bool = True,
    ) -> None: ...

class GTK3ListStore(Gtk.ListStore, GTK3ListStoreMixin):
    def __init__(
        self, column_types: list[GObject.GType], n_columns: int, n_rows: int | None
    ) -> None: ...
