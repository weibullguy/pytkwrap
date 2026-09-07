# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3GridMixin(GTK3ContainerMixin):
    _GTK3_GRID_ATTRIBUTES: Incomplete
    _GTK3_GRID_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_build_grid(
        self,
        columns: Sequence[int] | None = None,
        rows: Sequence[int] | None = None,
        siblings: Sequence[Gtk.Widget] | None = None,
        sides: Sequence[Sequence[Gtk.PositionType]] | None = None,
    ) -> None: ...
    def do_populate_grid(
        self,
        widgets: Sequence[Gtk.Widget],
        positions: Sequence[Sequence[int]],
        sizes: Sequence[Sequence[int]],
        siblings: Sequence[Gtk.Widget] | None = None,
        sides: Sequence[Gtk.PositionType] | None = None,
    ) -> None: ...
    def _build_grid_with_column_row_count(
        self, columns: Sequence[int] | None, rows: Sequence[int] | None
    ) -> None: ...
    def _build_grid_with_siblings_and_sides(
        self,
        siblings: Sequence[Gtk.Widget],
        sides: Sequence[Sequence[Gtk.PositionType]],
    ) -> None: ...

class GTK3Grid(Gtk.Grid, GTK3GridMixin):
    def __init__(self) -> None: ...
