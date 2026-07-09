# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget
from pytkwrap.utilities import FontDescription as FontDescription

class GTK3Entry(Gtk.Entry, GTK3Widget):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_ENTRY_ATTRIBUTES: Incomplete
    _GTK3_ENTRY_PROPERTIES: Incomplete
    _GTK3_ENTRY_SIGNALS: list[str]
    def __init__(self, font: FontDescription | None = None) -> None: ...
    def do_set_attributes(self, attributes: Mapping[str, object]) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float | int | str | None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None: ...
    def do_set_font_description(self, font: FontDescription | None = None) -> None: ...
