"""The pytkwrap GTK3RecentChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin


class GTK3RecentChooserDialogMixin(GTK3DialogMixin):
    """Mixin class for GTK3RecentChooserDialog."""


class GTK3RecentChooserDialog(Gtk.RecentChooserDialog, GTK3RecentChooserDialogMixin):
    """Wrapper for version 3.0 Gtk.RecentChooserDialog."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3RecentChooserDialog."""
        Gtk.RecentChooserDialog.__init__(self)
        GTK3RecentChooserDialogMixin.__init__(self)
