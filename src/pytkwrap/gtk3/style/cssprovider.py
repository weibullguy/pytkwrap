"""The pytkwrap GTK3CssProvider module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3CssProvider(Gtk.CssProvider, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.CssProvider."""

    _GTK3_CSSPROVIDER_SIGNALS = [
        "parsing-error",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CssProvider."""
        Gtk.CssProvider.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CSSPROVIDER_SIGNALS}
        )
