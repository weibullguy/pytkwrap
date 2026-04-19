# Standard Library Imports
from typing import override

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons import GTK3CheckButton as GTK3CheckButton
from pytkwrap.gtk3.buttons import GTK3SpinButton as GTK3SpinButton
from pytkwrap.gtk3.combo import GTK3ComboBox as GTK3ComboBox
from pytkwrap.gtk3.entry import GTK3Entry as GTK3Entry
from pytkwrap.gtk3.label import GTK3Label as GTK3Label
from pytkwrap.gtk3.textview import GTK3TextView as GTK3TextView
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import FontDescription as FontDescription

class GTK3MatrixView(Gtk.Grid, GTK3BaseDataWidget):
    _GTK3_MATRIXVIEW_PROPERTIES: Incomplete
    _GTK3_MATRIXVIEW_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    @override
    def do_get_value(self) -> None: ...
    @override
    def do_set_value(self, value) -> None: ...
    def do_add_column(self, position: int) -> None: ...
    def do_add_label(
        self,
        angle: float,
        heading: str,
        height: int,
        position: tuple[int, int],
        tooltip: str,
        width: int,
    ) -> None: ...
    def do_add_row(self, position: int) -> None: ...
    def do_add_widget(
        self,
        widget: GTK3CheckButton
        | GTK3ComboBox
        | GTK3Entry
        | GTK3Label
        | GTK3SpinButton
        | GTK3TextView,
        left: int,
        top: int,
        height: int,
        width: int,
    ): ...
    def do_build_matrix(
        self, column_names: list[tuple[str, str]], row_names: list[tuple[str, str]]
    ) -> None: ...
    def do_get_widget(
        self, column: int, row: int
    ) -> (
        GTK3CheckButton
        | GTK3ComboBox
        | GTK3Entry
        | GTK3Label
        | GTK3SpinButton
        | GTK3TextView
        | None
    ): ...
    def do_remove_column(self, position: int) -> None: ...
    def do_remove_row(self, position: int) -> None: ...
    def do_set_column_headings(self, column_names: list[tuple[str, str]]) -> None: ...
    def do_set_row_headings(self, row_names: list[tuple[str, str]]) -> None: ...
    def get_cell_value(
        self, column: int = 0, row: int = 0
    ) -> bool | float | int | str | None: ...
    def set_cell_value(
        self, value: bool | float | int | str | None, column: int = 0, row: int = 0
    ) -> None: ...
