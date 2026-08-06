# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin

class GTK3FixedMixin(GTK3ContainerMixin): ...

class GTK3Fixed(Gtk.Fixed, GTK3FixedMixin):
    def __init__(self) -> None: ...
