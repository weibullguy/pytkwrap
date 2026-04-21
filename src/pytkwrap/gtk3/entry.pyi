# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common import WidgetAttributes as WidgetAttributes
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import FontDescription as FontDescription

class GTK3Entry(Gtk.Entry, GTK3BaseDataWidget):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_ENTRY_PROPERTIES: Incomplete
    _GTK3_ENTRY_SIGNALS: list[str]
    def __init__(self, font: FontDescription | None = None) -> None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_value(self) -> float | int | str | None: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
    def do_set_font_description(self, font: FontDescription | None = None) -> None: ...
