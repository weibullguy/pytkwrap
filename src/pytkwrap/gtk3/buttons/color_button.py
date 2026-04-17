#       pytkwrap.gtk3.buttons.color_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The GTK3ColorButton module."""

# Third Party Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3ColorButton(Gtk.ColorButton, GTK3BaseButton):
    """The GTK3ColorButton class."""

    # Define private class attributes.
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
        GTK3BaseButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_COLOR_BUTTON_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_COLOR_BUTTON_SIGNALS
        })

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3ColorButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The types dict with the property values to set for the GTK3ColorButton.
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

    # ----- ----- Color Button specific methods. ----- ----- #
    def do_get_value(self) -> Gdk.RGBA | None:  # type: ignore[override]
        """Retrieve the Gtk.RGBA displayed in the GTK3ColorButton.

        Returns
        -------
        Gdk.RGBA
            The Gdk.RGBA displayed in the GTK3ColorButton.
        """
        return self.get_rgba()

    def do_set_value(self, value: Gdk.RGBA | None) -> None:
        """Set the GTK3ColorButton active value.

        Parameters
        ----------
        value : Gtk.RGBA | None
            The Gtk.RGBA to set the GTK3ColorButton active value.
        """
        if value is None:
            value = Gdk.RGBA(0.0, 0.0, 0.0, 1.0)
        self.set_rgba(value)
