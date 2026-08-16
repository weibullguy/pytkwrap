"""The pytkwrap GTK3RecentManager module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3RecentManagerMixin(GTK3GObjectMixin):
    """Mixin class for GTK3RecentManager.

    Notes
    -----
    GTK3RecentManager passes no widgets to its callback function.
    """

    _GTK3_RECENTMANAGER_SIGNALS = [
        "changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3RecentManager mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_RECENTMANAGER_SIGNALS}
        )


class GTK3RecentManager(Gtk.RecentManager, GTK3RecentManagerMixin):
    """Wrapper for version 3.0 Gtk.RecentManager."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3RecentManager."""
        Gtk.RecentManager.__init__(self)
        GTK3RecentManagerMixin.__init__(self)

    def do_add_recent(
        self,
        uri: str,
        recent_data: Gtk.RecentData | None = None,
    ) -> bool:
        """Add a recent file.

        Parameters
        ----------
        uri : str
            A valid URI pointing to the file to add to the manager.
        recent_data : Gtk.RecentData, optional
            Metadata to associate with the file.

        Returns
        -------
            True if the new item was successfully added, False otherwise.
        """
        if recent_data is None:
            return self.add_item(uri)
        return self.add_full(uri, recent_data)

    def do_remove_recent(self, uri: str, remove_all: bool = False) -> bool:
        """Remove a recent file.

        Parameters
        ----------
        uri : str
            The URI of the file to remove.
        remove_all : bool, optional
            True to remove all items, False to remove only the item with the given URI.

        Returns
        -------
            True if the item was successfully removed, False otherwise.
        """
        if remove_all:
            return bool(self.purge_items())
        return self.remove_item(uri)

    @property
    def recent_items(self) -> list[Gtk.RecentData]:
        """Return a list of Gtk.RecentData objects."""
        return self.get_items()
