# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError as UnkSignalError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3.scrolledwindow import GTK3ScrolledWindow as GTK3ScrolledWindow
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3TextView(Gtk.TextView, GTK3BaseDataWidget):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_TEXTVIEW_PROPERTIES: Incomplete
    _GTK3_TEXTVIEW_SIGNALS: list[str]
    default: str
    tag_bold: Incomplete
    scrollwindow: Incomplete
    def __init__(self, txtbuffer: Gtk.TextBuffer) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_update(
        self, package: dict[str, bool | date | float | int | str | None]
    ) -> None: ...
    def on_changed(self, /, __buffer: Gtk.TextBuffer) -> None: ...
    def do_get_value(self) -> str: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
    def _get_signal_owner(self) -> Gtk.TextBuffer: ...
