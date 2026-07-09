"""The pytkwrap GTK3SearchEntry module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io.entry import GTK3Entry
from pytkwrap.utilities import FontDescription


class GTK3SearchEntry(Gtk.SearchEntry, GTK3Entry):
    """The GTK3SearchEntry class.

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

    def __init__(
        self,
        font: FontDescription | None = None,
    ) -> None:
        """Initialize an instance of the GTK3SearchEntry widget.

        Parameters
        ----------
        font : FontDescription | None
            The font description for the font used by the GTK3SearchEntry.
        """
        Gtk.SearchEntry.__init__(self)
        GTK3Entry.__init__(self, font=font)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SEARCHENTRY_SIGNALS}
        )

        self.show()
