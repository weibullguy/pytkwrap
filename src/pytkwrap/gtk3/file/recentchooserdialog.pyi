# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin as GTK3DialogMixin

class GTK3RecentChooserDialogMixin(GTK3DialogMixin): ...

class GTK3RecentChooserDialog(Gtk.RecentChooserDialog, GTK3RecentChooserDialogMixin):
    def __init__(self) -> None: ...
