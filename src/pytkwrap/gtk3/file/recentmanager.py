"""The pytkwrap GTK3RecentManager module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3RecentManagerMixin(GTK3GObjectMixin):
    """Mixin class for GTK3RecentManager."""

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
