# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import (
    GTK3CellRendererMixin as GTK3CellRendererMixin,
)

class GTK3CellRendererSpinnerMixin(GTK3CellRendererMixin):
    _GTK3_CELLRENDERERSPINNER_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_get_value(self) -> int: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...

class GTK3CellRendererSpinner(Gtk.CellRendererSpinner, GTK3CellRendererSpinnerMixin):
    def __init__(self) -> None: ...
