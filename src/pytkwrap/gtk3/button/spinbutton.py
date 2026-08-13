"""The pytkwrap GTK3SpinButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.io.entry import GTK3EntryMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class GTK3SpinButtonMixin(GTK3EntryMixin):
    """Mixin for GTK3SpinButton.

    Attributes
    ----------
    _GTK3_SPINBUTTON_ATTRIBUTES : GTK3DataWidgetAttributes
        The typed dict containing GTK3SpinButton specific attributes and their default
        values.
    _GTK3_SPINBUTTON_PROPERTIES : GTK3WidgetProperties
        The typed dict containing GTK3SpinButton specific properties and their default
        values.
    _GTK3_SPINBUTTON_SIGNALS : list
        The list of signal names specifically associated with the GTK3SpinButton.
    """

    # Define private class attributes.
    _GTK3_SPINBUTTON_ATTRIBUTES = GTK3WidgetAttributes(
        data_type=float,
        default_value=0.0,
        edit_signal="value-changed",
        format="{:3.1f}",
    )
    _GTK3_SPINBUTTON_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        climb_rate=0.0,
        digits=0,
        numeric=False,
        snap_to_ticks=False,
        update_policy=Gtk.SpinButtonUpdatePolicy.ALWAYS,
        value=0.0,
        wrap=False,
    )
    _GTK3_SPINBUTTON_SIGNALS: list[str] = [
        "change-value",
        "input",
        "output",
        "value-changed",
        "wrapped",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3SpinButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_SPINBUTTON_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SPINBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SPINBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3SpinButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3SpinButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if isinstance(self.dic_properties["adjustment"], Gtk.Adjustment):
            self.set_adjustment(self.dic_properties["adjustment"])

        self.set_digits(self.dic_properties["digits"])
        # self.set_increments(
        #    self.dic_properties["step_increment"], self.dic_properties[
        #    "page_increment"]
        # )
        self.set_numeric(self.dic_properties["numeric"])
        # self.set_range(self.dic_properties["lower"], self.dic_properties["upper"])
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

    def do_get_value(self) -> float:  # type: ignore[override]
        """Return the value of the GTK3SpinButton.

        Returns
        -------
        value : float | int
            The value displayed in the GTK3SpinButton.
        """
        return self.dic_attributes["data_type"](self.get_value())

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None = None,
    ) -> None:
        """Set the value of the GTK3SpinButton.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The number to set the value of the GTK3SpinButton.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)

        self.set_value(self.dic_attributes["data_type"](value))


class GTK3SpinButton(Gtk.SpinButton, GTK3SpinButtonMixin):
    """Wrapper for version 3.0 Gtk.SpinButton."""

    def __init__(
        self,
        adjustment: GTK3Adjustment | None = None,
        climb_rate: float = 0.0,
        digits: int = 1,
    ) -> None:
        """Initialize an instance of the GTK3SpinButton widget.

        Parameters
        ----------
        adjustment : GTK3Adjustment | None
            The adjustment to use for the spin button.  The default is None.
        climb_rate : float
            Specifies how much the rate of change in the value will accelerate if the
            user continues to hold down an up/down button or arrow key.  The default
            is 0.0.
        digits : int
            The number of decimal places to display.  The
            default is 1.
        """
        Gtk.SpinButton.__init__(
            self,
            adjustment=adjustment,
            climb_rate=climb_rate,
            digits=digits,
        )
        GTK3SpinButtonMixin.__init__(self)

        self.dic_attributes["format"] = f"{{:3.{digits}f}}"

        self.dic_properties["adjustment"] = adjustment
        self.dic_properties["climb_rate"] = climb_rate
        self.dic_properties["digits"] = digits
