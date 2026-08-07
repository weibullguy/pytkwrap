# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3PageSetupMixin(GTK3GObjectMixin): ...

class GTK3PageSetup(Gtk.PageSetup, GTK3PageSetupMixin):
    def __init__(self) -> None: ...
