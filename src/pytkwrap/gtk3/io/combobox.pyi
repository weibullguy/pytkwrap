# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from types import EllipsisType as EllipsisType
from typing import Any

# Third Party Imports
from _typeshed import Incomplete
from gi.overrides.GdkPixbuf import Pixbuf as Pixbuf

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.bin import GTK3BinMixin as GTK3BinMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ComboBoxMixin(GTK3BinMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_COMBOBOX_ATTRIBUTES: Incomplete
    _GTK3_COMBOBOX_PROPERTIES: Incomplete
    _GTK3_COMBOBOX_SIGNALS: list[str]
    display_index: int
    _n_items: int
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_options(self) -> dict[int, Any]: ...
    def do_load_combo(
        self,
        entries: list[
            str | list[str | int | Pixbuf | None] | tuple[str | int | Pixbuf | None]
        ],
    ) -> None: ...
    def do_get_value(self) -> str: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
    def get_value_at_index(self, display_index: int = -1) -> str: ...

class GTK3ComboBox(Gtk.ComboBox, GTK3ComboBoxMixin):
    n_items: Incomplete
    def __init__(
        self, has_entry: bool = False, model: Gtk.TreeModel | None = None
    ) -> None: ...
