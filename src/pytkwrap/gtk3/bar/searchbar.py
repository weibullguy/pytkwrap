"""The pytkwrap GTK3SearchBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

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

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_SEARCHBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3SearchBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3SearchBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_search_mode(self.dic_properties["search_mode_enabled"])
        self.set_show_close_button(self.dic_properties["show_close_button"])
