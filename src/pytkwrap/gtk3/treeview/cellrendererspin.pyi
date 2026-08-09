# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderertext import (
    GTK3CellRendererTextMixin as GTK3CellRendererTextMixin,
)

class GTK3CellRendererSpinMixin(GTK3CellRendererTextMixin):
    _GTK3_CELLRENDERERSPIN_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_get_value(self) -> float: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...

class GTK3CellRendererSpin(Gtk.CellRendererSpin, GTK3CellRendererSpinMixin):
    def __init__(self) -> None: ...
