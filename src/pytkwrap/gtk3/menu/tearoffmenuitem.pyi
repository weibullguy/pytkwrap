# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin as GTK3MenuItemMixin

class GTK3TearoffMenuItemMixin(GTK3MenuItemMixin): ...

class GTK3TearoffMenuItem(Gtk.TearoffMenuItem, GTK3TearoffMenuItemMixin):
    def __init__(self) -> None: ...
