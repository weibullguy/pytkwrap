from _typeshed import Incomplete
from datetime import date
from pytkwrap.exceptions import UnkSignalError as UnkSignalError
from pytkwrap.gtk3._libs import Gtk as Gtk, Pango as Pango
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget, GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import none_to_default as none_to_default

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
    def do_update(self, package: dict[str, str]) -> None: ...
    def on_changed(self, /, __buffer: Gtk.TextBuffer) -> None: ...
    def do_get_value(self) -> str: ...
    def do_set_value(self, value: bool | date | float | int | str) -> None: ...
