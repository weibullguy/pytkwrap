# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin

class GTK3SocketMixin(GTK3ContainerMixin):
    _GTK3_SOCKET_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GTK3Socket(Gtk.Socket, GTK3SocketMixin):
    def __init__(self) -> None: ...
