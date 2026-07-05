"""The pytkwrap GTK3DrawingArea module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3DrawingArea(Gtk.DrawingArea, GTK3Widget):
    """Wrapper for version 3.0 Gtk.DrawingArea."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3DrawingArea."""
        Gtk.DrawingArea.__init__(self)
        GTK3Widget.__init__(self)
