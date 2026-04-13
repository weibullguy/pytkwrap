from . import BaseWidget as BaseWidget, WidgetAttributes as WidgetAttributes, WidgetProperties as WidgetProperties
from _typeshed import Incomplete
from datetime import date, datetime as datetime
from pytkwrap.exceptions import UnkSignalError as UnkSignalError
from pytkwrap.gtk3._libs import Gtk as Gtk, Pango as Pango, _ as _

class TextView(Gtk.TextView, BaseWidget):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _TEXTVIEW_PROPERTIES: Incomplete
    _TEXTVIEW_SIGNALS: list[str]
    tag_bold: Incomplete
    scrollwindow: Incomplete
    def __init__(self, txtbuffer: Gtk.TextBuffer) -> None: ...
    def do_set_properties(self, properties: WidgetProperties) -> None: ...
    def do_update(self, package: dict[str, bool | date | float | int | str]) -> None: ...
    def on_changed(self) -> None: ...
    def do_get_text(self) -> str: ...
