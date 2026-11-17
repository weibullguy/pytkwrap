"""The pytkwrap GTK3Socket module.

Convenience wrapper for working with Gtk.Socket.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

from __future__ import annotations

# Standard Library Imports
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _SocketHost


class GTK3SocketMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Socket.

    Notes
    -----
    The following Gtk.Socket methods are not wrapped in a convenience layer, but may be
    called directly:

        * add_id(window)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Socket.html for details
    on these methods.
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

    @property
    def id(self: _SocketHost) -> int:
        """Get the window ID of the GTK3Socket.

        Returns
        -------
        int
            The GTK3Socket's window ID.
        """
        return self.get_id()

    @property
    def plug_window(self: _SocketHost) -> Gdk.Window | None:
        """Get the window of the GTK3Plug.

        Returns
        -------
        Gdk.Window | None
            The Gdk.Window associated with the GTK3Plug or None.
        """
        return self.get_plug_window()


class GTK3Socket(Gtk.Socket, GTK3SocketMixin):
    """Wrapper for version 3.0 Gtk.Socket."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Socket."""
        Gtk.Socket.__init__(self)
        GTK3SocketMixin.__init__(self)
