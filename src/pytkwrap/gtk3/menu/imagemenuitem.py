"""The pytkwrap GTK3ImageMenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItemMixin


class GTK3ImageMenuItemMixin(GTK3MenuItemMixin):
    """Mixin class for GTK3ImageMenuItem."""


class GTK3ImageMenuItem(Gtk.ImageMenuItem, GTK3ImageMenuItemMixin):
    """Wrapper for version 3.0 Gtk.ImageMenuItem."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ImageMenuItem."""
        Gtk.ImageMenuItem.__init__(self)
        GTK3ImageMenuItemMixin.__init__(self)
