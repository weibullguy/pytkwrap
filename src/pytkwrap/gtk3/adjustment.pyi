# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3Adjustment(Gtk.Adjustment, GTK3GObjectMixin):
    _GTK3_ADJUSTMENT_PROPERTIES: Incomplete
    _GTK3_ADJUSTMENT_SIGNALS: Incomplete
    dic_handler_id: Incomplete
    def __init__(
        self,
        value: float = 0.0,
        lower: float = 0.0,
        upper: float = 0.0,
        step_increment: float = 0.0,
        page_increment: float = 0.0,
        page_size: float = 0.0,
    ) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float: ...
    def do_set_value(
        self, value: bool | date | float | int | str | tuple | None
    ) -> None: ...
