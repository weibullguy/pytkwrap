# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container import GTK3Container as GTK3Container

class GTK3Bin(Gtk.Bin, GTK3Container):
    def __init__(self) -> None: ...
