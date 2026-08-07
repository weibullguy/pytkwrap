"""The pytkwrap GTK3PrintContext module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3PrintContextMixin(GTK3GObjectMixin):
    """Mixin class for GTK3PrintContext."""


class GTK3PrintContext(Gtk.PrintContext, GTK3PrintContextMixin):
    """Wrapper for version 3.0 Gtk.PrintContext."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3PrintContext."""
        Gtk.PrintContext.__init__(self)
        GTK3PrintContextMixin.__init__(self)
