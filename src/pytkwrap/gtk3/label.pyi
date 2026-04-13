from _typeshed import Incomplete
from datetime import date
from pytkwrap.common import DataWidgetAttributes as DataWidgetAttributes
from pytkwrap.gtk3._libs import Gtk as Gtk, Pango as Pango
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes as GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseWidget as GTK3BaseWidget, GTK3WidgetProperties as GTK3WidgetProperties

class GTK3Label(Gtk.Label, GTK3BaseWidget):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _LABEL_ATTRIBUTES: Incomplete
    _LABEL_PROPERTIES: Incomplete
    _LABEL_SIGNALS: Incomplete
    default: str
    font_allow_breaks: str
    font_bgalpha: str
    font_bgcolor: str
    font_description: str
    font_family: str
    font_features: str
    font_fgalpha: str
    font_fgcolor: str
    font_gravity: str
    font_gravity_hint: str
    font_insert_hyphens: str
    font_lang: str
    font_letter_spacing: str
    font_overline: str
    font_overline_color: str
    font_rise: str
    font_scale: str
    font_size: str
    font_stretch: str
    font_strikethrough: str
    font_strikethrough_color: str
    font_style: str
    font_underline: str
    font_underline_color: str
    font_variant: str
    font_weight: str
    def __init__(self, text: str) -> None: ...
    def do_get_attribute(self, attribute: str) -> bool | date | float | int | str | None: ...
    def do_set_attributes(self, attributes: GTK3DataWidgetAttributes) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_update(self, package: dict[str, bool | date | float | int | str | None]) -> None: ...
    def do_set_font_description(self) -> None: ...

def do_make_label_group(label_text: list[str]) -> tuple[int, list[GTK3Label]]: ...
