# Standard Library Imports
from collections.abc import Mapping, Sequence
from datetime import date
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

class _BoxHost(Protocol):
    dic_properties: GTK3WidgetProperties
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
    @property
    def children(self) -> list[Gtk.Widget]: ...
    def get_children(self) -> list[Gtk.Widget]: ...
    def pack_end(self, child, expand, fill, padding) -> None: ...
    def pack_start(self, child, expand, fill, padding) -> None: ...
    def set_baseline_position(
        self, baseline_position: Gtk.BaselinePosition
    ) -> None: ...
    def set_center_widget(self, center_widget: Gtk.Widget | None) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class _ButtonBoxHost(Protocol):
    dic_attributes: GTK3WidgetAttributes
    dic_properties: GTK3WidgetProperties
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object | None]) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    @property
    def children(self) -> list[Gtk.Widget]: ...
    def get_children(self) -> list[Gtk.Widget]: ...
    def set_layout(self, layout_style: Gtk.ButtonBoxStyle) -> None: ...

class _ContainerHost(Protocol):
    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    def get_children(self) -> list[Gtk.Widget]: ...
    def set_border_width(self, border_width: int) -> None: ...
