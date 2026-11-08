# pylint: disable=missing-function-docstring
"""The pytkwrap button protocols module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class _SpinButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_attributes: GTK3WidgetAttributes
    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    def configure(
        self,
        adjustment: Gtk.Adjustment | None,
        climb_rate: float,
        digits: int,
    ) -> None: ...
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...
    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None = None,
    ) -> None: ...
    def get_increments(self) -> tuple[float | None, float | None]: ...
    def get_range(self) -> tuple[float | None, float | None]: ...
    def get_value(self) -> float: ...
    def set_adjustment(self, adjustment: Gtk.Adjustment) -> None: ...
    def set_increments(
        self,
        step: float,
        page: float,
    ) -> None: ...
    def set_range(
        self,
        min: float,  # pylint: disable=redefined-builtin
        max: float,  # pylint: disable=redefined-builtin
    ) -> None: ...
    def set_digits(self, digits: int) -> None: ...
    def set_numeric(self, numeric: bool) -> None: ...
    def set_snap_to_ticks(self, snap_to_ticks: bool) -> None: ...
    def set_update_policy(self, policy: Gtk.SpinButtonUpdatePolicy) -> None: ...
    def set_value(self, value: float) -> None: ...
    def set_wrap(self, wrap: bool) -> None: ...
    def set_property(self, property_name: str, value: object, /) -> None: ...
