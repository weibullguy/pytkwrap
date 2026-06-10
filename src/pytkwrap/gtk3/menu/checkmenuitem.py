"""The pytkwrap GTK3CheckMenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItem
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3CheckMenuItem(Gtk.CheckMenuItem, GTK3MenuItem):
    """Wrapper for version 3.0 Gtk.CheckMenuItem."""

    _GTK3_CHECKMENUITEM_PROPERTIES = GTK3WidgetProperties(
        active=False,
        draw_as_radio=False,
        inconsistent=False,
    )
    _GTK3_CHECKMENUITEM_SIGNALS = [
        "toggled",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CheckMenuItem."""
        Gtk.CheckMenuItem.__init__(self)
        GTK3MenuItem.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CHECKMENUITEM_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_CHECKMENUITEM_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ChecKMenuItem-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3CheckMenuItem.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_active(self.dic_properties["active"])
        self.set_draw_as_radio(self.dic_properties["draw_as_radio"])
        self.set_inconsistent(self.dic_properties["inconsistent"])
