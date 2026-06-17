"""The pytkwrap GTK3ColorSelectionDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog


class GTK3ColorSelectionDialog(Gtk.ColorSelectionDialog, GTK3Dialog):
    """Wrapper for version 3.0 Gtk.ColorSelectionDialog."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorSelectionDialog."""
        Gtk.ColorSelectionDialog.__init__(self)
        GTK3Dialog.__init__(self)
