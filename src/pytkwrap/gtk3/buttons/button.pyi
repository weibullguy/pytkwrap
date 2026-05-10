# Standard Library Imports
from collections.abc import Callable as Callable
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.bin import GTK3Bin as GTK3Bin
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    height: int = -1,
    layout: Gtk.ButtonBoxStyle = ...,
    orientation: str = "vertical",
    width: int = -1,
) -> Gtk.ButtonBox: ...

class GTK3Button(Gtk.Button, GTK3Bin):
    _GTK3_BUTTON_PROPERTIES: Incomplete
    _GTK3_BUTTON_SIGNALS: Incomplete
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, label: str = "...") -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
