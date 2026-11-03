# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3WindowGroupMixin(GTK3GObjectMixin):
    @property
    def current_grab(self) -> Gtk.Widget: ...
    @property
    def windows(self) -> list[Gtk.Window]: ...

class GTK3WindowGroup(Gtk.WindowGroup, GTK3WindowGroupMixin):
    def __init__(self) -> None: ...
