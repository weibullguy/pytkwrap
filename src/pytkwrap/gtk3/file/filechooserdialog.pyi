# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog as GTK3Dialog

class GTK3FileChooserDialog(Gtk.FileChooserDialog, GTK3Dialog):
    def __init__(self) -> None: ...
