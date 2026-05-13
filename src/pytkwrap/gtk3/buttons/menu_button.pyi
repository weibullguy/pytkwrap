# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.toggle_button import GTK3ToggleButton as GTK3ToggleButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3MenuButton(Gtk.MenuButton, GTK3ToggleButton):
    _GTK3_MENU_BUTTON_PROPERTIES: Incomplete
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
