"""The pytkwrap GTK3Socket module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin


class GTK3SocketMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Socket.

    Notes
    -----
    GTK3Socket passes no widgets to its callback function.
    """

    _GTK3_SOCKET_SIGNALS = [
        "plug-added",
        "plug-removed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Socket mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SOCKET_SIGNALS}
        )


class GTK3Socket(Gtk.Socket, GTK3SocketMixin):
    """Wrapper for version 3.0 Gtk.Socket."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Socket."""
        Gtk.Socket.__init__(self)
        GTK3SocketMixin.__init__(self)
