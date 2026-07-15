"""The pytkwrap GTK3Separator module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3Separator(Gtk.Separator, GTK3Widget):
    """Wrapper for version 3.0 Gtk.Separator."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Separator."""
        Gtk.Separator.__init__(self)
        GTK3Widget.__init__(self)
