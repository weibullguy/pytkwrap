# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin as GTK3DialogMixin

class GTK3FontChooserDialog(Gtk.FontChooserDialog, GTK3DialogMixin):
    def __init__(
        self,
        title: str | None = "Choose a Font",
        transient_for: Gtk.Window | None = None,
    ) -> None: ...
