# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common import WidgetAttributes as WidgetAttributes
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes as GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import FontDescription as FontDescription

class GTK3Label(Gtk.Label, GTK3BaseDataWidget):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_LABEL_ATTRIBUTES: Incomplete
    _GTK3_LABEL_PROPERTIES: Incomplete
    _GTK3_LABEL_SIGNALS: Incomplete
    def __init__(self, text: str) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_update(
        self, package: dict[str, bool | date | float | int | str | None]
    ) -> None: ...
    def do_get_value(self) -> str | None: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
    def do_set_font_description(self, font: FontDescription | None = None) -> None: ...

def do_make_label_group(label_text: list[str]) -> tuple[int, list[GTK3Label]]: ...
