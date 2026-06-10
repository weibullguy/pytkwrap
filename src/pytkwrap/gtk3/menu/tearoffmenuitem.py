"""The pytkwrap GTK3TearoffMenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItem


class GTK3TearoffMenuItem(Gtk.TearoffMenuItem, GTK3MenuItem):
    """Wrapper for version 3.0 Gtk.TearoffMenuItem."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3TearoffMenuItem."""
        Gtk.TearoffMenuItem.__init__(self)
        GTK3MenuItem.__init__(self)
