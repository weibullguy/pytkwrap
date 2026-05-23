"""The pytkwrap GTK3 Check Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.toggle_button import GTK3ToggleButton
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3CheckButton(Gtk.CheckButton, GTK3ToggleButton):
    """The GTK3CheckButton class."""

    # Define private class attributes.
    _DEFAULT_EDIT_SIGNAL = "toggled"
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200
    _GTK3_CHECK_BUTTON_PROPERTIES = GTK3WidgetProperties(
        label="...",
    )

    def __init__(self, label="...") -> None:
        """Initialize an instance of the GTK3CheckButton widget.

        Parameters
        ----------
        label : str
            The text to display in the GTK3CheckButton label.  The default value is
            an ellipsis (...).
        """
        Gtk.CheckButton.__init__(self, label=label)
        GTK3ToggleButton.__init__(self, label)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CHECK_BUTTON_PROPERTIES)

    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
        """
        if property_name in self._GTK3_CHECK_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3CheckButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3ColorButton.
        """
        super().do_set_properties(properties)

        self.set_label(self.dic_properties["label"])
