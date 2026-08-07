# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin as GTK3MenuItemMixin

class GTK3SeparatorMenuItemMixin(GTK3MenuItemMixin): ...

class GTK3SeparatorMenuItem(Gtk.SeparatorMenuItem, GTK3SeparatorMenuItemMixin):
    def __init__(self) -> None: ...
