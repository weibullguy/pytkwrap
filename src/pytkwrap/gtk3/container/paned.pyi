# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _PanedHost as _PanedHost

TOPLEFT: int
BOTTOMRIGHT: int

class GTK3PanedMixin(GTK3ContainerMixin):
    _GTK3_PANED_ATTRIBUTES: Incomplete
    _GTK3_PANED_PROPERTIES: Incomplete
    _GTK3_PANED_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    def do_add_child(
        self, child: Gtk.Widget, resize: bool, shrink: bool, position: int = 1
    ) -> None: ...
    @property
    def children(self) -> tuple[Gtk.Widget, Gtk.Widget]: ...
    @property
    def handle_window(self) -> Gdk.Window: ...

class GTK3Paned(Gtk.Paned, GTK3PanedMixin):
    def __init__(self, orientation: Gtk.Orientation = ...) -> None: ...
