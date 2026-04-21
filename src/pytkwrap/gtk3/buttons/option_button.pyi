# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton as GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3OptionButton(Gtk.RadioButton, GTK3BaseButton):
    _GTK3_OPTION_BUTTON_PROPERTIES: Incomplete
    _GTK3_OPTION_BUTTON_SIGNALS: Incomplete
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, group: Gtk.RadioButton = None, label: str = "") -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> bool: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
