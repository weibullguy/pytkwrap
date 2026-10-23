"""The pytkwrap GTK3TextTagTable module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3TextTagTableMixin(GTK3GObjectMixin):
    """Mixin class for GTK3TextTagTable.

    Attributes
    ----------
    _GTK3_TEXTTAGTABLE_SIGNALS : list[str]
        Signals unique to the GTK3TextTagTable.
    """

    _GTK3_TEXTTAGTABLE_SIGNALS = [
        "tag-added",
        "tag-changed",
        "tag-removed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3TextTagTable mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TEXTTAGTABLE_SIGNALS}
        )

    @property
    def size(self) -> int:
        """Return the number of tags in the tag table."""
        return self.get_size()


class GTK3TextTagTable(Gtk.TextTagTable, GTK3TextTagTableMixin):
    """Wrapper for version 3.0 Gtk.TextTagTable."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3TextTagTable."""
        Gtk.TextTagTable.__init__(self)
        GTK3TextTagTableMixin.__init__(self)
