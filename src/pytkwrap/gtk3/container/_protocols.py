# pylint: disable=missing-function-docstring
"""The pytkwrap container protocols module.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

# Standard Library Imports
from collections.abc import Mapping, Sequence
from datetime import date
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class _BoxHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    def do_add_child(
        self,
        child: GTK3Widget,
        expand: bool,
        fill: bool,
        padding: int,
        start: bool = True,
    ) -> None: ...

    # pytkwrap-specific managed attributes.
    @property
    def children(self) -> list[Gtk.Widget]: ...

    # Gtk3 API methods.
    def get_children(self) -> list[Gtk.Widget]: ...
    def pack_end(self, child, expand, fill, padding) -> None: ...
    def pack_start(self, child, expand, fill, padding) -> None: ...
    def set_baseline_position(
        self,
        baseline_position: Gtk.BaselinePosition,
    ) -> None: ...
    def set_center_widget(self, center_widget: Gtk.Widget | None) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...


class _ButtonBoxHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_attributes: GTK3WidgetAttributes
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object | None]) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...

    # pytkwrap-specific managed attributes.
    @property
    def children(self) -> list[Gtk.Widget]: ...

    # Gtk3 API methods.
    def get_children(self) -> list[Gtk.Widget]: ...
    def set_layout(self, layout_style: Gtk.ButtonBoxStyle) -> None: ...


class _ContainerHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...

    # Gtk3 API methods.
    def get_children(self) -> list[Gtk.Widget]: ...
    def set_border_width(self, border_width: int) -> None: ...


class _ExpanderHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...

    # Gtk3 API methods.
    def set_expanded(self, expanded: bool) -> None: ...
    def set_label(self, label: str | None) -> None: ...
    def set_label_fill(self, label_fill: bool) -> None: ...
    def set_label_widget(self, label_widget: Gtk.Widget | None) -> None: ...
    def set_resize_toplevel(self, resize_toplevel: bool) -> None: ...
    def set_use_markup(self, use_markup: bool) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...


class _FrameHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...

    # Gtk3 API methods.
    def set_label(self, label: str | None) -> None: ...
    def set_label_align(self, xalign: float, yalign: float) -> None: ...
    def set_label_widget(self, label_widget: Gtk.Widget) -> None: ...
    def set_shadow_type(
        self,
        type: Gtk.ShadowType,  # pylint: disable=redefined-builtin
    ) -> None: ...
