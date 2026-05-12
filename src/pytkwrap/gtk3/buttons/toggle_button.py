"""The pytkwrap GTK3 Toggle Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.bin import GTK3Bin
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3ToggleButton(Gtk.ToggleButton, GTK3Bin):
    """The GTK3ToggleButton class."""

    # Define private class attributes.
    _GTK3_TOGGLE_BUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value=False,  # i.e., not active
        edit_signal="toggled",
    )
    _GTK3_TOGGLE_BUTTON_PROPERTIES = GTK3WidgetProperties(
        active=False,
        draw_indicator=False,
        inconsistent=False,
    )
    _GTK3_TOGGLE_BUTTON_SIGNALS = [
        "toggled",
    ]
    _DEFAULT_EDIT_SIGNAL = "toggled"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ToggleButton widget."""
        Gtk.ToggleButton.__init__(self)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_TOGGLE_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_TOGGLE_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOGGLE_BUTTON_SIGNALS}
        )

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
        if property_name in self._GTK3_TOGGLE_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3ToggleButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3ToggleButton.
        """
        super().do_set_properties(properties)

        self.set_active(self.dic_properties["active"])
        self.set_inconsistent(self.dic_properties["inconsistent"])
        self.set_mode(self.dic_properties["draw_indicator"])

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Retrieve the state of the GTK3ToggleButton.

        Returns
        -------
        bool
            Whether the GTK3ToggleButton is active (pressed) or not.
        """
        return self.get_active()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3ToggleButton active value.

        If the value passed is not a bool, float, or int, the default value is used.

        Parameters
        ----------
        value : bool | float | int
            The value to set the GTK3ToggleButton active value.
        """
        if not isinstance(value, (bool, float, int)):
            value = self.dic_attributes.get("default_value")
        self.dic_properties["active"] = bool(value)
        self.set_active(bool(value))
