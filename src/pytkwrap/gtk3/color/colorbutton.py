"""The pytkwrap GTK3ColorButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.button.button import GTK3Button
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class GTK3ColorButton(Gtk.ColorButton, GTK3Button):
    """Wrapper for version 3.0 Gtk.ColorButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
    _GTK3_COLOR_BUTTON_ATTRIBUTES: GTK3WidgetAttributes = GTK3WidgetAttributes(
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
        "color-set",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorButton."""
        Gtk.ColorButton.__init__(self)
        GTK3Button.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_COLOR_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_COLOR_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_COLOR_BUTTON_SIGNALS}
        )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ColorButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ColorButton.
        """
        super().do_set_properties(properties)

        if self.dic_properties["rgba"] is not None:
            self.set_rgba(self.dic_properties["rgba"])
        self.set_title(self.dic_properties["title"])

        for _property in [
            "show_editor",
            "use_alpha",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_get_value(self) -> bool | date | float | int | object | str | None:
        """Return the current value of the GTK3ColorButton.

        Returns
        -------
        Gdk.RGBA
            The current Gdk.RGBA displayed in the GTK3ColorButton.
        """
        return self.get_rgba()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3ColorButton.

        Parameters
        ----------
        value : Gtk.RGBA
            The Gtk.RGBA to set for the GTK3ColorButton.
        """
        if value is None:
            value = Gdk.RGBA(0.0, 0.0, 0.0, 1.0)
        if not isinstance(value, Gdk.RGBA):
            super().do_set_value(value)
        self.dic_properties["rgba"] = value
        self.set_rgba(value)
