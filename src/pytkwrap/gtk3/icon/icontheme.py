"""The pytkwrap GTK3IconTheme module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3IconThemeMixin(GTK3GObjectMixin):
    """Mixin class for GTK3IconTheme."""

    _GTK3_ICONTHEME_SIGNALS = ["changed"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3IconTheme mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ICONTHEME_SIGNALS}
        )


class GTK3IconTheme(Gtk.IconTheme, GTK3IconThemeMixin):
    """Wrapper for version 3.0 Gtk.IconTheme."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3IconTheme."""
        Gtk.IconTheme.__init__(self)
        GTK3IconThemeMixin.__init__(self)
