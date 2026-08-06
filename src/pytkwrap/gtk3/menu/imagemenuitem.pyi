# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin as GTK3MenuItemMixin

class GTK3ImageMenuItemMixin(GTK3MenuItemMixin): ...

class GTK3ImageMenuItem(Gtk.ImageMenuItem, GTK3ImageMenuItemMixin):
    def __init__(self) -> None: ...
