# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin as GTK3DialogMixin

class GTK3FileChooserDialogMixin(GTK3DialogMixin): ...

class GTK3FileChooserDialog(Gtk.FileChooserDialog, GTK3FileChooserDialogMixin):
    def __init__(self) -> None: ...
