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
from pytkwrap.gtk3._libs import Gdk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class _ColorButtonHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_attributes: GTK3WidgetAttributes
    dic_handler_id: list[str]
    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...
    def do_get_value(self) -> bool | date | float | int | object | str | None: ...
    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None: ...

    # Gtk3 API methods.
    def get_rgba(self) -> Gdk.RGBA: ...
    def set_property(self, property_name: str, value) -> None: ...
    def set_rgba(self, rgba: Gdk.RGBA) -> None: ...
    def set_title(self, title: str | None) -> None: ...


class _ColorChooserDialogHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # Gtk3 API methods.
    def set_property(self, property_name: str, value) -> None: ...


class _ColorChooserWidgetHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_properties: GTK3WidgetProperties

    # pytkwrap-specific methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...

    # Gtk3 API methods.
    def set_property(self, property_name: str, value) -> None: ...
