"""The pytkwrap GTK3FontChooserWidget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box


class GTK3FontChooserWidget(Gtk.FontChooserWidget, GTK3Box):
    """Wrapper for version 3.0 Gtk.FontChooserWidget."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FontChooserWidget."""
        Gtk.FontChooserWidget.__init__(self)
        GTK3Box.__init__(self)
