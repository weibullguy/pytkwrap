"""The pytkwrap GTK3 Bin module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Container


class GTK3Bin(Gtk.Bin, GTK3Container):
    """Wrapper for Gtk.Bin."""

    def __init__(self) -> None:
        Gtk.Bin.__init__(self)
        GTK3Container.__init__(self)
