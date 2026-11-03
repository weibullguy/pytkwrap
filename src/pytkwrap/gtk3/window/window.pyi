# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3WindowMixin(GTK3ContainerMixin):
    _GTK3_WINDOW_PROPERTIES: Incomplete
    _GTK3_WINDOW_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    @property
    def group(self) -> Gtk.WindowGroup: ...
    @property
    def resize_grip_area(self) -> Gdk.Rectangle: ...
    @property
    def size(self) -> tuple[int, int]: ...
    @property
    def window_type(self) -> Gtk.WindowType: ...

class GTK3Window(Gtk.Window, GTK3WindowMixin):
    def __init__(self, wtype: Gtk.WindowType = ...) -> None: ...
