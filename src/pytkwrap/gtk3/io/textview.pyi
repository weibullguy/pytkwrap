# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from types import FunctionType

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError as UnkSignalError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3Container as GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3TextView(Gtk.TextView, GTK3Container):
    _GTK3_TEXTVIEW_ATTRIBUTES: Incomplete
    _GTK3_TEXTVIEW_PROPERTIES: Incomplete
    _GTK3_TEXTVIEW_SIGNALS: Incomplete
    buffer: Incomplete
    def __init__(self, buffer: Gtk.TextBuffer | None = None) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object]) -> None: ...
    def do_set_callbacks(
        self, signal: list[str] | str, callback: FunctionType, after: bool = False
    ) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> str: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
