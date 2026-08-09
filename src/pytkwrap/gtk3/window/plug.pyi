# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.window.window import GTK3WindowMixin as GTK3WindowMixin

class GTK3PlugMixin(GTK3WindowMixin):
    _GTK3_PLUG_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GTK3Plug(Gtk.Plug, GTK3PlugMixin):
    def __init__(self) -> None: ...
