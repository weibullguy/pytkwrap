# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.check_button import GTK3CheckButton as GTK3CheckButton
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3RadioButton(Gtk.RadioButton, GTK3CheckButton):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_RADIO_BUTTON_PROPERTIES: Incomplete
    _GTK3_RADIO_BUTTON_SIGNALS: Incomplete
    def __init__(self, label: str = "...", group=None) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
