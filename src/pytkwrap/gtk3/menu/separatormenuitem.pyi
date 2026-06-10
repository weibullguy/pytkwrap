# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItem as GTK3MenuItem

class GTK3SeparatorMenuItem(Gtk.SeparatorMenuItem, GTK3MenuItem):
    def __init__(self) -> None: ...
