"""The pytkwrap GTK3TearoffMenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin


class GTK3TearoffMenuItemMixin(GTK3MenuItemMixin):
    """Mixin class for GTK3TearoffMenuItem."""


class GTK3TearoffMenuItem(Gtk.TearoffMenuItem, GTK3TearoffMenuItemMixin):
    """Wrapper for version 3.0 Gtk.TearoffMenuItem."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3TearoffMenuItem."""
        Gtk.TearoffMenuItem.__init__(self)
        GTK3TearoffMenuItemMixin.__init__(self)
