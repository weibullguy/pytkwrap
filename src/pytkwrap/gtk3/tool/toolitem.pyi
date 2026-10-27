# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ToolItemMixin(GTK3ContainerMixin):
    _GTK3_TOOLITEM_PROPERTIES: Incomplete
    _GTK3_TOOLITEM_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    @property
    def ellipsize_mode(self) -> Pango.EllipsizeMode: ...
    @property
    def icon_size(self) -> int: ...
    @property
    def orientation(self) -> Gtk.Orientation: ...
    @property
    def relief_style(self) -> Gtk.ReliefStyle: ...
    @property
    def text_alignment(self) -> float: ...
    @property
    def text_orientation(self) -> Gtk.Orientation: ...
    @property
    def text_size_group(self) -> Gtk.SizeGroup: ...
    @property
    def toolbar_style(self) -> Gtk.ToolbarStyle: ...

class GTK3ToolItem(Gtk.ToolItem, GTK3ToolItemMixin):
    def __init__(self) -> None: ...
