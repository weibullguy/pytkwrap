"""The pytkwrap GTK3FontChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog


class GTK3FontChooserDialog(Gtk.FontChooserDialog, GTK3Dialog):
    """Wrapper for version 3.0 Gtk.FontChooserDialog."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FontChooserDialog."""
        Gtk.FontChooserDialog.__init__(self)
        GTK3Dialog.__init__(self)
