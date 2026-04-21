# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import clamp as clamp

class GTK3SpinButton(Gtk.SpinButton, GTK3BaseDataWidget):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_SPIN_BUTTON_PROPERTIES: Incomplete
    _GTK3_SPIN_BUTTON_SIGNALS: list[str]
    def __init__(self) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> float: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
