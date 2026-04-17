# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton as GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3SpinButton(Gtk.SpinButton, GTK3BaseButton):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_SPIN_BUTTON_PROPERTIES: Incomplete
    _GTK3_SPIN_BUTTON_SIGNALS: list[str]
    def __init__(self) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> float: ...
    def do_set_value(self, value: float | int | None) -> None: ...
