# pylint: disable=missing-function-docstring, too-many-public-methods
# ruff: noqa: PLR0904
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


class _ButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # Gtk3 API methods.
    def set_always_show_image(self, always_show_image: bool) -> None: ...
    def set_image(self, image: Gtk.Widget | None) -> None: ...
    def set_image_position(self, image_position: Gtk.PositionType) -> None: ...
    def set_label(self, label: str | None) -> None: ...
    def set_relief(self, relief: Gtk.ReliefStyle) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...


class _AppChooserButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # Gtk3 API methods.
    def set_heading(self, heading: str) -> None: ...
    def set_show_default_item(self, show_default_item: bool) -> None: ...
    def set_show_dialog_item(self, show_dialog_item: bool) -> None: ...


class _RadioButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # pytkwrap-specific managed attributes.
    @property
    def group(self) -> list[Gtk.RadioButton]: ...

    # Gtk3 API methods.
    def get_group(self) -> list[Gtk.RadioButton]: ...
    def join_group(self, group: Gtk.RadioButton | None) -> None: ...


class _ScaleButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_attributes: GTK3WidgetAttributes
    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def configure(
        self,
        value: float,
        lower: float,
        upper: float,
        step_increment: float,
        page_increment: float,
        page_size: float,
    ) -> None: ...
    def do_get_value(self) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...
    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None = None,
    ) -> None: ...

    # pytkwrap-specific managed attributes.
    @property
    def lower(self) -> float: ...
    @property
    def minus_button(self) -> Gtk.Button: ...
    @property
    def page_increment(self) -> float: ...
    @property
    def page_size(self) -> float: ...
    @property
    def plus_button(self) -> Gtk.Button: ...
    @property
    def popup(self) -> Gtk.Widget: ...
    @property
    def step_increment(self) -> float: ...
    @property
    def upper(self) -> float: ...

    # Gtk3 API methods.
    def get_minus_button(self) -> Gtk.Button: ...
    def get_plus_button(self) -> Gtk.Button: ...
    def get_popup(self) -> Gtk.Widget: ...
    def get_value(self) -> float: ...
    def set_adjustment(self, adjustment: Gtk.Adjustment) -> None: ...
    def set_icons(self, icons: list[str]) -> None: ...
    def set_property(self, property_name, value) -> None: ...
    def set_value(self, value: float) -> None: ...


class _SpinButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_attributes: GTK3WidgetAttributes
    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
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

    # pytkwrap-specific managed attributes.
    @property
    def increments(self) -> tuple[float | None, float | None]: ...
    @property
    def lower(self) -> float: ...
    @property
    def page_increment(self) -> float: ...
    @property
    def range(self) -> tuple[float | None, float | None]: ...
    @property
    def step_increment(self) -> float: ...
    @property
    def upper(self) -> float: ...

    # Gtk3 API methods.
    def get_adjustment(self) -> Gtk.Adjustment: ...
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


class _ToggleButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_attributes: GTK3WidgetAttributes
    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_get_value(self) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...
    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None = None,
    ) -> None: ...

    # Gtk3 API methods.
    def get_active(self) -> bool: ...
    def set_active(self, active: bool) -> None: ...
    def set_inconsistent(self, inconsistent: bool) -> None: ...
    def set_mode(self, draw_indicator: bool) -> None: ...


class _VolumeButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # Gtk3 API methods.
    def set_property(self, property_name: str, value) -> None: ...
