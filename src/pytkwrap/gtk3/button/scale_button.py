"""The pytkwrap GTK3ScaleButton module.

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


class GTK3ScaleButton(Gtk.ScaleButton, GTK3Button):
    """Wrapper for version 3.0 Gtk.ScaleButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
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

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ScaleButton widget."""
        Gtk.ScaleButton.__init__(self)
        GTK3Button.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_SCALE_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_SCALE_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SCALE_BUTTON_SIGNALS}
        )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3ScaleButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ScaleButton.
        """
        super().do_set_properties(properties)

        if self.dic_properties["adjustment"] is not None:
            self.set_adjustment(self.dic_properties["adjustment"])

        if len(self.dic_properties["icons"]) > 0:
            self.set_icons(self.dic_properties["icons"])

        self.set_value(self.dic_properties["value"])

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Return the current value of the GTK3ScaleButton.

        Returns
        -------
        float
            The current value of the GTK3ScaleButton.
        """
        return self.get_value()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3ScaleButton.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The value to set for the GTK3ScaleButton.
        """
        # Boolean values are also of type int.  False is 0, True is 1.
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)
        self.dic_properties["value"] = float(value)  # type: ignore[arg-type]
        self.set_value(float(value))  # type: ignore[arg-type]
