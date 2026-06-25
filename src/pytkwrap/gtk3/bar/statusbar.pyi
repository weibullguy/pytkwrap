# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3Box as GTK3Box

class GTK3Statusbar(Gtk.Statusbar, GTK3Box):
    _GTK3_STATUSBAR_SIGNALS: Incomplete
    def __init__(self) -> None: ...
