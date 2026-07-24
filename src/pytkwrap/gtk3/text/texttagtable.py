"""The pytkwrap GTK3TextTagTable module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3TextTagTable(Gtk.TextTagTable, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.TextTagTable."""

    _GTK3_TEXTTAGTABLE_SIGNALS = [
        "tag-added",
        "tag-changed",
        "tag-removed",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3TextTagTable."""
        Gtk.TextTagTable.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TEXTTAGTABLE_SIGNALS}
        )
