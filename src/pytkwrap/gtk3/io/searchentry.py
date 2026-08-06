"""The pytkwrap GTK3SearchEntry module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io.entry import GTK3EntryMixin


class GTK3SearchEntryMixin(GTK3EntryMixin):
    """Mixin class for GTK3SearchEntry.

    Attributes
    ----------
    _GTK3_SEARCHENTRY_SIGNALS : list
        The list of signal names specifically associated with the GTK3SearchEntry.
    """

    _GTK3_SEARCHENTRY_SIGNALS: list[str] = [
        "next-match",
        "previous-match",
        "search-changed",
        "stop-search",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3SearchEntry mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SEARCHENTRY_SIGNALS}
        )

        self.show()


class GTK3SearchEntry(Gtk.SearchEntry, GTK3SearchEntryMixin):
    """The GTK3SearchEntry class."""

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3SearchEntry widget."""
        Gtk.SearchEntry.__init__(self)
        GTK3SearchEntryMixin.__init__(self)
