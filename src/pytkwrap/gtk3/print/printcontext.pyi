# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3PrintContextMixin(GTK3GObjectMixin): ...

class GTK3PrintContext(Gtk.PrintContext, GTK3PrintContextMixin):
    def __init__(self) -> None: ...
