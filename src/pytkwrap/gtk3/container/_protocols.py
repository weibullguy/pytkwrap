# pylint: disable=missing-function-docstring
"""The pytkwrap container protocols module.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

# Standard Library Imports
from collections.abc import Mapping
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class _BoxHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...
    def do_add_child(
        self,
        child: GTK3Widget,
        expand: bool,
        fill: bool,
        padding: int,
        start: bool = True,
    ) -> None: ...

    # Gtk3 API methods.
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

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # Gtk3 API methods.
    def set_layout(self, layout_style: Gtk.ButtonBoxStyle) -> None: ...
