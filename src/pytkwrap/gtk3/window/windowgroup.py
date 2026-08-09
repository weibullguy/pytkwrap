"""The pytkwrap GTK3WindowGroup module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3WindowGroupMixin(GTK3GObjectMixin):
    """Mixin class for GTK3WindowGroup."""


class GTK3WindowGroup(Gtk.WindowGroup, GTK3WindowGroupMixin):
    """Wrapper for version 3.0 Gtk.WindowGroup."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3WindowGroup."""
        Gtk.WindowGroup.__init__(self)
        GTK3WindowGroupMixin.__init__(self)
