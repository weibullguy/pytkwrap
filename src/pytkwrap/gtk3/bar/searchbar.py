"""The pytkwrap GTK3SearchBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3SearchBar(Gtk.SearchBar, GTK3Bin):
    """Wrapper for version 3.0 Gtk.SearchBar."""

    _GTK3_SEARCHBAR_PROPERTIES = GTK3WidgetProperties(
        search_mode_enabled=False,
        show_close_button=False,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3SearchBar."""
        Gtk.SearchBar.__init__(self)
        GTK3Bin.__init__(self)

        self.dic_properties.update(self._GTK3_SEARCHBAR_PROPERTIES)
