# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons import GTK3BaseButton as GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ColorButton(Gtk.ColorButton, GTK3BaseButton, GTK3BaseDataWidget):
    _GTK3_COLOR_BUTTON_PROPERTIES: Incomplete
    _GTK3_COLOR_BUTTON_SIGNALS: Incomplete
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> Gdk.RGBA | None: ...
    def do_set_value(self, value: Gdk.RGBA | None) -> None: ...
