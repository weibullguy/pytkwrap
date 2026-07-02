# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3Container as GTK3Container

class GTK3Socket(Gtk.Socket, GTK3Container):
    _GTK3_SOCKET_SIGNALS: Incomplete
    def __init__(self) -> None: ...
