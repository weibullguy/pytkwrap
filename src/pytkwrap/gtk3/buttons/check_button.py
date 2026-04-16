#       pytkwrap.gtk3.buttons.check_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3CheckButton module."""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3BaseButton
from pytkwrap.gtk3.widget import (
    GTK3BaseDataWidget,
    GTK3WidgetProperties,
)


# pylint: disable=too-many-ancestors
# GTK3's own inheritance chain accounts for 7 of the 9 ancestors.
# The pytkwrap additions (GTK3BaseButton, GTK3BaseDataWidget) are necessary
# to provide button label handling and pubsub data widget support.
# TODO: Refactor the GTKBaseButton to inherit from GTK3BaseDataWidget instead of
#  GTK3BaseWidget and then remove the GTK3BaseDataWidget ancestor from here.
class GTK3CheckButton(Gtk.CheckButton, GTK3BaseButton, GTK3BaseDataWidget):
    """The GTK3CheckButton class."""

    # Define private class attributes.
    _CHECK_BUTTON_PROPERTIES = GTK3WidgetProperties(
        active=False,
        draw_indicator=False,
        inconsistent=False,
    )
    _CHECK_BUTTON_SIGNALS = ["toggled"]
    _DEFAULT_EDIT_SIGNAL = "toggled"
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200

    def __init__(self, label: str = "") -> None:
        """Initialize an instance of the GTK3CheckButton widget.

        Parameters
        ----------
        label : str
            The text to display with the GTK3CheckButton. Default is an empty string.
        """
        Gtk.CheckButton.__init__(self)
        GTK3BaseDataWidget.__init__(self)
        GTK3BaseButton.__init__(self, label=label)

        # Initialize public instance attributes.
        self.dic_properties.update(self._CHECK_BUTTON_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._CHECK_BUTTON_SIGNALS
        })

        self.default = False

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3CheckButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3CheckButton.
        """
        super().do_set_properties(properties)

        self.dic_properties["active"] = properties.get("active", False)
        self.dic_properties["draw_indicator"] = properties.get("draw_indicator", False)
        self.dic_properties["inconsistent"] = properties.get("inconsistent", False)

        self.set_active(self.dic_properties["active"])
        self.set_inconsistent(self.dic_properties["inconsistent"])

        for _property in [
            "draw_indicator",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    # ----- ----- Check Button specific methods. ----- ----- #
    def do_get_value(self) -> bool:  # type: ignore[override]
        """Retrieve the status of the GTK3CheckButton.

        Returns
        -------
        bool
            The status of the GTK3CheckButton.
        """
        return self.get_active()

    def do_set_value(self, value: bool | int) -> None:
        """Set the GTK3CheckButton active value.

        Parameters
        ----------
        value : bool or int or None
            The desired status of the GTK3CheckButton.
        """
        if value is None:
            value = False

        self.set_active(value)
