"""The pytkwrap GTK3Bin module.

Convenience wrapper for working with Gtk.Bin.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin


class GTK3Bin(Gtk.Bin, GTK3ContainerMixin):
    """Wrapper for version 3.0 Gtk.Bin."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Bin."""
        Gtk.Bin.__init__(self)
        GTK3ContainerMixin.__init__(self)
