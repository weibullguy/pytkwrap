# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes as PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.button import GTK3Button as GTK3Button
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ToggleButton(Gtk.ToggleButton, GTK3Button):
    _GTK3_TOGGLE_BUTTON_ATTRIBUTES: PyTkWrapAttributes
    _GTK3_TOGGLE_BUTTON_PROPERTIES: Incomplete
    _GTK3_TOGGLE_BUTTON_SIGNALS: Incomplete
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, label: str = "...") -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> bool | date | float | int | object | str | None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
