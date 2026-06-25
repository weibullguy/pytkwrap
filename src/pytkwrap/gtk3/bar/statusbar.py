"""The pytkwrap GTK3Statusbar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box


class GTK3Statusbar(Gtk.Statusbar, GTK3Box):
    """Wrapper for version 3.0 Gtk.Statusbar."""

    _GTK3_STATUSBAR_SIGNALS = ["text-popped", "text-pushed"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Statusbar."""
        Gtk.Statusbar.__init__(self)
        GTK3Box.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_STATUSBAR_SIGNALS}
        )
