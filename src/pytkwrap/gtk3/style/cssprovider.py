"""The pytkwrap GTK3CssProvider module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3CssProviderMixin(GTK3GObjectMixin):
    """Mixin class for GTK3CssProvider."""

    _GTK3_CSSPROVIDER_SIGNALS = [
        "parsing-error",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CssProvider mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CSSPROVIDER_SIGNALS}
        )


class GTK3CssProvider(Gtk.CssProvider, GTK3CssProviderMixin):
    """Wrapper for version 3.0 Gtk.CssProvider."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CssProvider."""
        Gtk.CssProvider.__init__(self)
        GTK3CssProviderMixin.__init__(self)
