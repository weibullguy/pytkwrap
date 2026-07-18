# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3IconInfo(Gtk.IconInfo, GTK3GObjectMixin):
    def __init__(self) -> None: ...
