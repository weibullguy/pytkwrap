# Standard Library Imports
from datetime import date
from types import EllipsisType
from typing import Any

# Third Party Imports
from _typeshed import Incomplete
from gi.overrides.GdkPixbuf import Pixbuf as Pixbuf

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes as GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseDataWidget as GTK3BaseDataWidget
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ComboBox(Gtk.ComboBox, GTK3BaseDataWidget):
    _GTK3_COMBO_BOX_ATTRIBUTES: Incomplete
    _GTK3_COMBO_BOX_PROPERTIES: Incomplete
    _GTK3_COMBO_BOX_SIGNALS: list[str]
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    default: int
    has_entry: bool
    n_items: int
    simple: bool
    def __init__(
        self,
        index: int = 0,
        simple: bool = True,
        n_items: int = 1,
        column_types: list[EllipsisType] | list[GObject.GType] | None = None,
        has_entry: bool = False,
    ) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
    def do_get_options(self) -> dict[int, Any]: ...
    def do_load_combo(self, entries: list[list[str | int | Pixbuf | None]]) -> None: ...
    def do_get_value(self) -> str: ...
    def do_set_value(self, value: int) -> None: ...
    def get_value_at_index(self, index: int = -1) -> str: ...
