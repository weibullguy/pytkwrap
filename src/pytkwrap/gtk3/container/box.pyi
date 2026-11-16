# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

# pytkwrap Local Imports
from ._protocols import _BoxHost as _BoxHost

class GTK3BoxMixin(GTK3ContainerMixin):
    _GTK3_BOX_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
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

class GTK3Box(Gtk.Box, GTK3BoxMixin):
    def __init__(
        self, orientation: Gtk.Orientation = ..., spacing: int = 0
    ) -> None: ...
