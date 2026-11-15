# Standard Library Imports
from collections.abc import Mapping
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

class _BoxHost(Protocol):
    dic_properties: GTK3WidgetProperties
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_add_child(
        self,
        child: GTK3Widget,
        expand: bool,
        fill: bool,
        padding: int,
        start: bool = True,
    ) -> None: ...
    def pack_end(self, child, expand, fill, padding) -> None: ...
    def pack_start(self, child, expand, fill, padding) -> None: ...
    def set_baseline_position(
        self, baseline_position: Gtk.BaselinePosition
    ) -> None: ...
    def set_center_widget(self, center_widget: Gtk.Widget | None) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...
