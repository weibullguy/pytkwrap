# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.combobox import GTK3ComboBox as GTK3ComboBox
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3AppChooserButton(Gtk.AppChooserButton, GTK3ComboBox):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_APP_CHOOSER_BUTTON_PROPERTIES: Incomplete
    _GTK3_APP_CHOOSER_BUTTON_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
