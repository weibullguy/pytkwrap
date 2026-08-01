# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin

class GTK3BinMixin(GTK3ContainerMixin):
    def __init__(self) -> None: ...

class GTK3Bin(Gtk.Bin, GTK3BinMixin):
    def __init__(self) -> None: ...
