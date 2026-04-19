#       pytkwrap.gtk3.buttons.spin_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The GTK3SpinButton module."""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3SpinButton(
    Gtk.SpinButton,
    GTK3BaseButton,
):  # ty:ignore[inconsistent-mro]
    """The GTK3SpinButton class."""

    # Define private class scalar attributes.
    _DEFAULT_EDIT_SIGNAL = "value-changed"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_SPIN_BUTTON_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        climb_rate=0.0,
        digits=0,
        lower=0.0,
        numeric=False,
        page_increment=0.0,
        snap_to_ticks=False,
        step_increment=0.0,
        update_policy=Gtk.SpinButtonUpdatePolicy.ALWAYS,
        upper=0.0,
        value=0.0,
        wrap=False,
    )
    _GTK3_SPIN_BUTTON_SIGNALS: list[str] = [
        "activate",
        "backspace",
        "change-value",
        "changed",
        "copy-clipboard",
        "cut-clipboard",
        "delete-from-cursor",
        "delete-text",
        "editing-done",
        "icon-press",
        "icon-release",
        "input",
        "insert-at-cursor",
        "insert-emoji",
        "insert-text",
        "move-cursor",
        "output",
        "paste-clipboard",
        "populate-popup",
        "preedit-changed",
        "remove-widget",
        "toggle-direction",
        "toggle-overwrite",
        "value-changed",
        "wrapped",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3SpinButton."""
        Gtk.SpinButton.__init__(self)
        GTK3BaseButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_SPIN_BUTTON_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_SPIN_BUTTON_SIGNALS
        })

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3SpinButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3SpinButton.
        """
        super().do_set_properties(properties)

        if isinstance(self.dic_properties["adjustment"], Gtk.Adjustment):
            self.set_adjustment(self.dic_properties["adjustment"])

        self.set_digits(self.dic_properties["digits"])
        self.set_increments(
            self.dic_properties["step_increment"], self.dic_properties["page_increment"]
        )
        self.set_numeric(self.dic_properties["numeric"])
        self.set_range(self.dic_properties["lower"], self.dic_properties["upper"])
        self.set_snap_to_ticks(self.dic_properties["snap_to_ticks"])
        self.set_update_policy(self.dic_properties["update_policy"])
        self.set_value(self.dic_properties["value"])
        self.set_wrap(self.dic_properties["wrap"])

        for _property in [
            "climb_rate",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    # ----- ----- Option Button specific methods. ----- ----- #
    def do_get_value(self) -> float:  # type: ignore[override]
        """Return the value of the GTK3SpinButton.

        Returns
        -------
        value : float
            Whether the GTK3SpinButton is active or not.
        """
        return self.get_value()

    def do_set_value(self, value: float | int | None) -> None:
        """Set the value of the GTK3SpinButton.

        Parameters
        ----------
        value : float | int | None
            The number to set the value of the GTK3SpinButton.
        """
        if value is None:
            return

        self.set_value(float(value))
