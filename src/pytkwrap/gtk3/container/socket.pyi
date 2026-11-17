# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin

# pytkwrap Local Imports
from ._protocols import _SocketHost as _SocketHost

class GTK3SocketMixin(GTK3ContainerMixin):
    _GTK3_SOCKET_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def plug_window(self) -> Gdk.Window | None: ...

class GTK3Socket(Gtk.Socket, GTK3SocketMixin):
    def __init__(self) -> None: ...
