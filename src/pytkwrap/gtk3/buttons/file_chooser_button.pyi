# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton as GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import dir_exists as dir_exists
from pytkwrap.utilities import file_exists as file_exists
from pytkwrap.utilities import get_home_directory as get_home_directory

class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3BaseButton):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_FILE_CHOOSER_BUTTON_PROPERTIES: Incomplete
    _GTK3_FILE_CHOOSER_BUTTON_SIGNALS: Incomplete
    default: str
    def __init__(self, label: str = "...") -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> str | list[str] | Gio.File | list[Gio.File] | None: ...
    def do_set_value(self, value: str | Gio.File | None) -> None: ...
    def get_gio_value(self) -> Gio.File | list[Gio.File] | None: ...
    def get_uri_value(self) -> str | list[str] | None: ...
