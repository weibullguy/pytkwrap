from _typeshed import Incomplete
from datetime import date
from gi.overrides.GdkPixbuf import Pixbuf as Pixbuf
from pytkwrap.gtk3._libs import GObject as GObject, Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes as GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget, GTK3WidgetProperties as GTK3WidgetProperties
from types import EllipsisType
from typing import Any

class GTK3ComboBox(Gtk.ComboBox, GTK3BaseDataWidget):
    _GTK3_COMBO_ATTRIBUTES: Incomplete
    _GTK3_COMBO_PROPERTIES: Incomplete
    _GTK3_COMBO_SIGNALS: list[str]
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    default: int
    has_entry: bool
    index: int
    n_items: int
    simple: bool
    column_types: list[EllipsisType] | list[GObject.GType] | None
    def __init__(self, index: int = 0, simple: bool = True, n_items: int = 1, column_types: list[EllipsisType] | list[GObject.GType] | None = None, has_entry: bool = False) -> None: ...
    def do_get_attribute(self, attribute: str) -> bool | date | float | int | str | None: ...
    font_description: Incomplete
    def do_set_attributes(self, attributes: GTK3DataWidgetAttributes) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_options(self) -> dict[int, Any]: ...
    def do_load_combo(self, entries: list[list[str | int | Pixbuf | None]]) -> None: ...
    def do_get_value(self, index: int = -1) -> str: ...
    def do_set_value(self, value: int) -> None: ...
