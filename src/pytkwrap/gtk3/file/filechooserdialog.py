"""The pytkwrap GTK3FileChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin


class GTK3FileChooserDialogMixin(GTK3DialogMixin):
    """Mixin class for GTK3FileChooserDialog."""


class GTK3FileChooserDialog(Gtk.FileChooserDialog, GTK3FileChooserDialogMixin):
    """Wrapper for version 3.0 Gtk.FileChooserDialog."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FileChooserDialog."""
        Gtk.FileChooserDialog.__init__(self)
        GTK3FileChooserDialogMixin.__init__(self)
