"""The pytkwrap GTK3 Scale Button module.

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


class GTK3ScaleButton(Gtk.ScaleButton, GTK3Bin):
    """The GTK3ScaleButton class."""

    # Define private class attributes.
    _GTK3_SCALE_BUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value=0.0,
        edit_signal="value-changed",
    )
    _GTK3_SCALE_BUTTON_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        icons=[],
        size=Gtk.IconSize.SMALL_TOOLBAR,
        value=0.0,
    )
    _GTK3_SCALE_BUTTON_SIGNALS = [
        "popdown",
        "popup",
        "value-changed",
    ]
    _DEFAULT_EDIT_SIGNAL = "value-changed"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ScaleButton widget."""
        Gtk.ScaleButton.__init__(self)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_SCALE_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_SCALE_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SCALE_BUTTON_SIGNALS}
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
        if property_name in self._GTK3_SCALE_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3ScaleButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3ScaleButton.
        """
        super().do_set_properties(properties)

        self.set_adjustment(self.dic_properties["adjustment"])
        self.set_icons(self.dic_properties["icons"])
        self.set_value(self.dic_properties["value"])

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Retrieve the Gtk.RGBA displayed in the GTK3ScaleButton.

        Returns
        -------
        Gdk.RGBA
            The Gdk.RGBA displayed in the GTK3ScaleButton.
        """
        return self.get_value()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3ScaleButton active value.

        If the value passed is not a float or int, the default value is used.

        Parameters
        ----------
        value : float | int | str
            The value to set the GTK3ScaleButton active value.
        """
        if not isinstance(value, (float, int, str)):
            value = self.dic_attributes.get("default_value")
        self.set_value(float(value))
