# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3Box as GTK3Box

class GTK3FontChooserWidget(Gtk.FontChooserWidget, GTK3Box):
    def __init__(self) -> None: ...
