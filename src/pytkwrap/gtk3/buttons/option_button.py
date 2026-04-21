#       pytkwrap.gtk3.buttons.option_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3OptionButton module."""

# Standard Library Imports
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3OptionButton(Gtk.RadioButton, GTK3BaseButton):
    """The GTK3OptionButton class."""

    # Define private class attributes.
    _GTK3_OPTION_BUTTON_PROPERTIES = GTK3WidgetProperties(
        active=False,
        draw_indicator=False,
        group=None,
        inconsistent=False,
    )
    _GTK3_OPTION_BUTTON_SIGNALS = ["group-changed", "toggled"]
    _DEFAULT_EDIT_SIGNAL = "toggled"
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200

    def __init__(self, group: Gtk.RadioButton = None, label: str = "") -> None:
        """Initialize an instance of the GTK3OptionButton widget.

        Parameters
        ----------
        group : Gtk.RadioButton | GTK3OptionButton
            The group the GTK3OptionButton belongs to, if any. Default is None.
        label : str
            The text to place in the label on the GTK3OptionButton. Default is an empty
             string.
        """
        Gtk.RadioButton.__init__(self)
        GTK3BaseButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_OPTION_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_OPTION_BUTTON_SIGNALS}
        )

        self.do_set_properties(
            GTK3WidgetProperties(
                group=group,
                label=label,
            )
        )

    # ----- ----- ----- ----- --- Standard widget methods. --- ----- ----- ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3OptionButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3OptionButton.
        """
        super().do_set_properties(properties)

        self.set_active(self.dic_properties["active"])
        self.join_group(self.dic_properties["group"])
        self.set_inconsistent(self.dic_properties["inconsistent"])

        for _property in [
            "draw_indicator",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    # ----- ----- ----- ----- Option Button specific methods. ----- ----- ----- ----- #
    def do_get_value(self) -> bool:  # type: ignore[override]
        """Return the value of the GTK3OptionButton.

        Returns
        -------
        active : bool
            Whether the GTK3OptionButton is active or not.
        """
        return self.get_active()

    def do_set_value(self, value: bool | date | float | int | str | None) -> None:
        """Set the status of the GTK3OptionButton.

        Parameters
        ----------
        value : bool | date | float | int | str | None
            The index of the item in the GTK3ComboBox to set active.
        """
        if not isinstance(value, bool):
            return

        self.set_active(bool(value))
