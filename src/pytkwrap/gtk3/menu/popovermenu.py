"""The pytkwrap GTK3PopoverMenu module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.popover import GTK3Popover


class GTK3PopoverMenu(Gtk.PopoverMenu, GTK3Popover):
    """Wrapper for version 3.0 Gtk.PopoverMenu."""

    _GTK3_POPOVERMENU_PROPERTIES = GTK3WidgetProperties(
        visible_submenu=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3PopoverMenu."""
        Gtk.PopoverMenu.__init__(self)
        GTK3Popover.__init__(self)

        self.dic_properties.update(self._GTK3_POPOVERMENU_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3PopoverMenu-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3PopoverMenu.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["visible_submenu"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
