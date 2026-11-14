# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class _ColorButtonHost(Protocol):
    dic_attributes: GTK3WidgetAttributes
    dic_handler_id: list[str]
    dic_properties: GTK3WidgetProperties
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> bool | date | float | int | object | str | None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
    def get_rgba(self) -> Gdk.RGBA: ...
    def set_property(self, property_name: str, value) -> None: ...
    def set_rgba(self, rgba: Gdk.RGBA) -> None: ...
    def set_title(self, title: str | None) -> None: ...

class _ColorChooserDialogHost(Protocol):
    dic_properties: GTK3WidgetProperties
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def set_property(self, property_name: str, value) -> None: ...
