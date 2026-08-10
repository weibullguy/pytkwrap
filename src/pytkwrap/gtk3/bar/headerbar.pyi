# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container import GTK3ContainerMixin as GTK3ContainerMixin

class GTK3HeaderBarMixin(GTK3ContainerMixin):
    _GTK3_HEADERBAR_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3HeaderBar(Gtk.HeaderBar, GTK3HeaderBarMixin):
    def __init__(self) -> None: ...
