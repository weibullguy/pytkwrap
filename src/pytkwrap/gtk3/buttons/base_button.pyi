# Standard Library Imports
from collections.abc import Callable as Callable
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    height: int = -1,
    layout: Gtk.ButtonBoxStyle = ...,
    orientation: str = "vertical",
    width: int = -1,
) -> Gtk.HButtonBox | Gtk.VButtonBox: ...

class GTK3BaseButton(Gtk.Button, GTK3BaseDataWidget):
    _GTK3_BASE_BUTTON_PROPERTIES: Incomplete
    _GTK3_BASE_BUTTON_SIGNALS: Incomplete
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, label: str = "...") -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> bool | date | float | int | str | None: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
