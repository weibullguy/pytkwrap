"""The pytkwrap GTK3Socket module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container


class GTK3Socket(Gtk.Socket, GTK3Container):
    """Wrapper for version 3.0 Gtk.Socket."""

    _GTK3_SOCKET_SIGNALS = [
        "plug-added",
        "plug-removed",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Socket."""
        Gtk.Socket.__init__(self)
        GTK3Container.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SOCKET_SIGNALS}
        )
