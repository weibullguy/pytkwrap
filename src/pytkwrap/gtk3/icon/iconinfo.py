"""The pytkwrap GTK3IconInfo module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3IconInfo(Gtk.IconInfo, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.IconInfo."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3IconInfo."""
        Gtk.IconInfo.__init__(self)
        GTK3GObjectMixin.__init__(self)
