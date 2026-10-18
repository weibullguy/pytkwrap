"""The pytkwrap GTK3SeparatorMenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin


class GTK3SeparatorMenuItem(Gtk.SeparatorMenuItem, GTK3MenuItemMixin):
    """Wrapper for version 3.0 Gtk.SeparatorMenuItem.

    Notes
    -----
    GTK3SeparatorMenuItem passes no widgets to its callback functions.
    """

    def __init__(self) -> None:
        """Initialize an instance of the GTK3SeparatorMenuItem."""
        Gtk.SeparatorMenuItem.__init__(self)
        GTK3MenuItemMixin.__init__(self)
