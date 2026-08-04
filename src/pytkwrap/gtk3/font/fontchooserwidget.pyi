# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin

class GTK3FontChooserWidget(Gtk.FontChooserWidget, GTK3BoxMixin):
    def __init__(self) -> None: ...
