"""The pytkwrap GTK3RadioToolButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toggletoolbutton import GTK3ToggleToolButton


class GTK3RadioToolButton(Gtk.RadioToolButton, GTK3ToggleToolButton):
    """Wrapper for version 3.0 Gtk.RadioToolButton."""

    _GTK3_RADIOTOOLBUTTON_PROPERTIES = GTK3WidgetProperties(
        group=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3RadioToolButton."""
        Gtk.RadioToolButton.__init__(self)
        GTK3ToggleToolButton.__init__(self)

        self.dic_properties.update(self._GTK3_RADIOTOOLBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3RadioToolButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3RadioToolButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_group(self.dic_properties["group"])
