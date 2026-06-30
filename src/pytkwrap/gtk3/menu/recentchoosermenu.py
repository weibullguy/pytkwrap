"""The pytkwrap GTK3RecentChooserMenu module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menu import GTK3Menu
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3RecentChooserMenu(Gtk.RecentChooserMenu, GTK3Menu):
    """Wrapper for version 3.0 Gtk.RecentChooserMenu."""

    _GTK3_RECENTCHOOSERMENU_PROPERTIES = GTK3WidgetProperties(
        show_numbers=False,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3RecentChooserMenu."""
        Gtk.RecentChooserMenu.__init__(self)
        GTK3Menu.__init__(self)

        self.dic_properties.update(self._GTK3_RECENTCHOOSERMENU_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3RecentChooserMenu-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3RecentChooserMenu.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_show_numbers(self.dic_properties["show_numbers"])
