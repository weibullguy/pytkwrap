# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons import GTK3BaseButton as GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3BaseButton):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_FILE_CHOOSER_BUTTON_PROPERTIES: Incomplete
    _GTK3_FILE_CHOOSER_BUTTON_SIGNALS: Incomplete
    def __init__(self, label: str = "...") -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> str | None: ...
    def do_set_value(self, value: str | None) -> None: ...
