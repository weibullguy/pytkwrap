# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

class GTK3Calendar(Gtk.Calendar, GTK3Widget):
    _GTK3_CALENDAR_PROPERTIES: Incomplete
    _GTK3_CALENDAR_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_get_value(self) -> date: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
