# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.range import GTK3RangeMixin as GTK3RangeMixin

class GTK3ScrollBarMixin(GTK3RangeMixin):
    def __init__(self) -> None: ...

class GTK3ScrollBar(Gtk.Scrollbar, GTK3ScrollBarMixin):
    def __init__(self) -> None: ...
