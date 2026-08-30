"""The pytkwrap GTK3Fixed module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin


class GTK3Fixed(Gtk.Fixed, GTK3ContainerMixin):
    """Wrapper for version 3.0 Gtk.Fixed.

    Notes
    -----
    GTK3Fixed passes no widgets to its callback function.
    """

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Fixed."""
        Gtk.Fixed.__init__(self)
        GTK3ContainerMixin.__init__(self)
