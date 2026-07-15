# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

class GTK3Range(Gtk.Range, GTK3Widget):
    _GTK3_RANGE_ATTRIBUTES: Incomplete
    _GTK3_RANGE_PROPERTIES: Incomplete
    _GTK3_RANGE_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object]) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
