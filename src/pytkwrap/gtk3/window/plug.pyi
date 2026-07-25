# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.window.window import GTK3Window as GTK3Window

class GTK3Plug(Gtk.Plug, GTK3Window):
    _GTK3_PLUG_SIGNALS: Incomplete
    def __init__(self) -> None: ...
