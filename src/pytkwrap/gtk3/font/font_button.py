"""The pytkwrap GTK3 Font Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.button import GTK3Button
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FontButton(Gtk.FontButton, GTK3Button):
    """The GTK3FontButton class."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
    _GTK3_FONT_BUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value="Sans 12",
        edit_signal="font-set",
    )
    _GTK3_FONT_BUTTON_PROPERTIES = GTK3WidgetProperties(
        font_name="Sans 12",
        show_size=True,
        show_style=True,
        title="Pick a Font",
        use_font=False,
        use_size=False,
    )
    _GTK3_FONT_BUTTON_SIGNALS = [
        "font-set",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FontButton widget."""
        Gtk.FontButton.__init__(self)
        GTK3Button.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_FONT_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_FONT_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_FONT_BUTTON_SIGNALS}
        )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3FontButton.

        Note
        ----
        We call the Gtk.FontChooser.set_font() method which is inherited by
        Gtk.FontButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3FontButton.
        """
        super().do_set_properties(properties)

        self.set_font(self.dic_properties["font_name"])
        self.set_show_size(self.dic_properties["show_size"])
        self.set_show_style(self.dic_properties["show_style"])
        self.set_title(self.dic_properties["title"])
        self.set_use_font(self.dic_properties["use_font"])
        self.set_use_size(self.dic_properties["use_size"])

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Retrieve the name of the currently selected font in the GTK3FontButton.

        Note
        ----
        We call the Gtk.FontChooser.get_font() method which is inherited by
        Gtk.FontButton.

        Returns
        -------
        str
            The name of the currently selected font in the GTK3FontButton.
        """
        return self.get_font()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3FontButton active value.

        Note
        ----
        We call the Gtk.FontChooser.set_font() method which is inherited by
        Gtk.FontButton.

        Parameters
        ----------
        value : str
            The name of the font to set the GTK3FontButton active value.
        """
        if not isinstance(value, str):
            super().do_set_value(value)
        self.dic_properties["font_name"] = value
        self.set_font(str(value))
