# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _StackHost as _StackHost

class GTK3StackMixin(GTK3ContainerMixin):
    _GTK3_STACK_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    def do_add_child(
        self, child: Gtk.Widget, name: str, title: str | None = None
    ) -> None: ...
    @property
    def transition_running(self) -> bool: ...

class GTK3Stack(Gtk.Stack, GTK3StackMixin):
    def __init__(self) -> None: ...
