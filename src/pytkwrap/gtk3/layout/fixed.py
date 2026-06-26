"""The pytkwrap GTK3Fixed module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container


class GTK3Fixed(Gtk.Fixed, GTK3Container):
    """Wrapper for version 3.0 Gtk.Fixed."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Fixed."""
        Gtk.Fixed.__init__(self)
        GTK3Container.__init__(self)
