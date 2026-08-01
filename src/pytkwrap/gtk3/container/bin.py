"""The pytkwrap GTK3Bin module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin


class GTK3BinMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Bin."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3BinMixin."""
        GTK3ContainerMixin.__init__(self)


class GTK3Bin(Gtk.Bin, GTK3BinMixin):
    """Wrapper for version 3.0 Gtk.Bin."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Bin."""
        Gtk.Bin.__init__(self)
        GTK3BinMixin.__init__(self)
