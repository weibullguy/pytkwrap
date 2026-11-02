# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment as GTK3Adjustment
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ScrolledWindowMixin(GTK3ContainerMixin):
    _GTK3_SCROLLEDWINDOW_PROPERTIES: Incomplete
    _GTK3_SCROLLEDWINDOW_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    @property
    def hscrollbar(self) -> Gtk.Scrollbar | None: ...
    @property
    def vscrollbar(self) -> Gtk.Scrollbar | None: ...

class GTK3ScrolledWindow(Gtk.ScrolledWindow, GTK3ScrolledWindowMixin):
    def __init__(
        self,
        hadjustment: GTK3Adjustment | None = None,
        vadjustment: GTK3Adjustment | None = None,
    ) -> None: ...
