# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _ViewportHost as _ViewportHost

class GTK3ViewportMixin(GTK3ContainerMixin):
    _GTK3_VIEWPORT_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    @property
    def bin_window(self) -> Gdk.Window | None: ...
    @property
    def view_window(self) -> Gdk.Window | None: ...

class GTK3Viewport(Gtk.Viewport, GTK3ViewportMixin):
    def __init__(
        self,
        hadjustment: Gtk.Adjustment | None = None,
        vadjustment: Gtk.Adjustment | None = None,
    ) -> None: ...
