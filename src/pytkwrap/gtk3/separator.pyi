# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget

class GTK3Separator(Gtk.Separator, GTK3Widget):
    def __init__(self) -> None: ...
