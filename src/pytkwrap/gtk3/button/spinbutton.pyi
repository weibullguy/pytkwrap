# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment as GTK3Adjustment
from pytkwrap.gtk3.io.entry import GTK3EntryMixin as GTK3EntryMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _SpinButtonHost as _SpinButtonHost

class GTK3SpinButtonMixin(GTK3EntryMixin):
    _GTK3_SPINBUTTON_ATTRIBUTES: Incomplete
    _GTK3_SPINBUTTON_PROPERTIES: Incomplete
    _GTK3_SPINBUTTON_SIGNALS: list[str]
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float | int: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None: ...
    def do_configure(
        self, adjustment: GTK3Adjustment | None, climb_rate: float, digits: int
    ) -> None: ...
    @property
    def increments(self) -> tuple[float | None, float | None]: ...
    @property
    def range(self) -> tuple[float | None, float | None]: ...

class GTK3SpinButton(Gtk.SpinButton, GTK3SpinButtonMixin):
    def __init__(
        self,
        adjustment: Gtk.Adjustment | None = None,
        climb_rate: float = 0.0,
        digits: int = 1,
    ) -> None: ...
