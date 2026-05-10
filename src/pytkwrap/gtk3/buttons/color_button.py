"""The pytkwrap GTK3 Color Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.bin import GTK3Bin
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3ColorButton(Gtk.ColorButton, GTK3Bin):
    """The GTK3ColorButton class."""

    # Define private class attributes.
    _GTK3_COLOR_BUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value=None,
        edit_signal="color-set",
    )
    _GTK3_COLOR_BUTTON_PROPERTIES = GTK3WidgetProperties(
        alpha=65535,
        rgba=None,
        show_editor=False,
        title="Pick a Color",
        use_alpha=True,
    )
    _GTK3_COLOR_BUTTON_SIGNALS = [
        "color-activated",
        "color-set",
    ]
    _DEFAULT_EDIT_SIGNAL = "color-set"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorButton widget."""
        Gtk.ColorButton.__init__(self)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_COLOR_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_COLOR_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_COLOR_BUTTON_SIGNALS}
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
        if property_name in self._GTK3_COLOR_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3ColorButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3ColorButton.
        """
        super().do_set_properties(properties)

        if self.dic_properties["rgba"] is not None:
            self.set_rgba(self.dic_properties["rgba"])
        self.set_title(self.dic_properties["title"])
        self.set_use_alpha(self.dic_properties["use_alpha"])

        for _property in [
            "show_editor",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Retrieve the Gtk.RGBA displayed in the GTK3ColorButton.

        Returns
        -------
        Gdk.RGBA
            The Gdk.RGBA displayed in the GTK3ColorButton.
        """
        return self.get_rgba()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3ColorButton active value.

        Parameters
        ----------
        value : Gtk.RGBA
            The Gtk.RGBA to set the GTK3ColorButton active value.
        """
        if not isinstance(value, Gdk.RGBA):
            value = Gdk.RGBA(0.0, 0.0, 0.0, 1.0)
        self.set_rgba(value)
