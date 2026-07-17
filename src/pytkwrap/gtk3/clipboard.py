"""The pytkwrap GTK3Clipboard module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3Clipboard(Gtk.Clipboard, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.Clipboard."""

    _GTK3_CLIPBOARD_SIGNALS = [
        "owner-change",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Clipboard."""
        Gtk.Clipboard.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CLIPBOARD_SIGNALS}
        )
