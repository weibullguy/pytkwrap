"""The pytkwrap GTK3 Volume Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.scale_button import GTK3ScaleButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3VolumeButton(Gtk.VolumeButton, GTK3ScaleButton):
    """The GTK3VolumeButton class."""

    # Define private class attributes.
    _GTK3_VOLUME_BUTTON_PROPERTIES = GTK3WidgetProperties(
        use_symbolic=True,
    )
    _DEFAULT_EDIT_SIGNAL = "value-changed"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60

    def __init__(self) -> None:
        """Initialize an instance of the GTK3VolumeButton widget."""
        Gtk.VolumeButton.__init__(self)
        GTK3ScaleButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_VOLUME_BUTTON_PROPERTIES)

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
        if property_name in self._GTK3_VOLUME_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Retrieve the value displayed in the GTK3VolumeButton.

        Returns
        -------
        float
            The value displayed in the GTK3VolumeButton.
        """
        return self.get_value()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3VolumeButton active value.

        If the value passed is not a float, int, or str, the default value is used.

        Parameters
        ----------
        value : float | int | str
            The value to set the GTK3VolumeButton active value.
        """
        if not isinstance(value, (float, int, str)):
            value = self.dic_attributes.get("default_value")
        self.set_value(float(value))
