# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.range import GTK3Range as GTK3Range

class GTK3ScrollBar(Gtk.Scrollbar, GTK3Range):
    def __init__(self) -> None: ...
