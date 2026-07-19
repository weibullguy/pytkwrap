# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes

class GTK3ListStore(Gtk.ListStore, GTK3GObjectMixin):
    _GTK3_LISTSTORE_ATTRIBUTES: Incomplete
    def __init__(self, column_types: list, n_columns: int, n_rows: int) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object]) -> None: ...
