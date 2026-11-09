"""The pytkwrap GTK3SpinButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.io.entry import GTK3EntryMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties

if TYPE_CHECKING:
    # noinspection unused-imports
    # pytkwrap Local Imports
    from ._protocols import _SpinButtonHost


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

    Notes
    -----
    The following Gtk.SpinButton methods are not wrapped in a convenience layer,
    but may be called directly:

        * spin(direction, increment)
        * update()

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/SpinButton.html for
    details on these methods.
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
        lower=0.0,
        numeric=False,
        page_increment=0.0,
        page_size=0.0,
        snap_to_ticks=False,
        step_increment=0.0,
        update_policy=Gtk.SpinButtonUpdatePolicy.ALWAYS,
        upper=0.0,
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
        self: _SpinButtonHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3SpinButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3SpinButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        if isinstance(self.dic_properties["adjustment"], Gtk.Adjustment):
            self.dic_properties["page_increment"] = self.dic_properties[
                "adjustment"
            ].get_page_increment()
            self.dic_properties["page_size"] = self.dic_properties[
                "adjustment"
            ].get_page_size()
            self.dic_properties["step_increment"] = self.dic_properties[
                "adjustment"
            ].get_step_increment()
            self.dic_properties["lower"] = self.dic_properties["adjustment"].get_lower()
            self.dic_properties["upper"] = self.dic_properties["adjustment"].get_upper()
            self.set_adjustment(self.dic_properties["adjustment"])
        else:
            self.set_increments(
                self.dic_properties["step_increment"],
                self.dic_properties["page_increment"],
            )
            self.set_range(self.dic_properties["lower"], self.dic_properties["upper"])

        self.set_digits(self.dic_properties["digits"])
        self.set_numeric(self.dic_properties["numeric"])
        self.set_snap_to_ticks(self.dic_properties["snap_to_ticks"])
        self.set_update_policy(self.dic_properties["update_policy"])
        self.set_value(self.dic_properties["value"])
        self.set_wrap(self.dic_properties["wrap"])

        self.set_property("climb-rate", self.dic_properties["climb_rate"])

    def do_get_value(self: _SpinButtonHost) -> float | int:  # type: ignore[override]
        """Return the value of the GTK3SpinButton.

        Returns
        -------
        value : float | int
            The value displayed in the GTK3SpinButton.  The data type returned
            depends on the data type attribute set for the GTK3SpinButton.
        """
        return self.dic_attributes["data_type"](self.get_value())

    def do_set_value(
        self: _SpinButtonHost,
        value: bool | date | float | int | object | str | tuple | None = None,
    ) -> None:
        """Set the value of the GTK3SpinButton.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The number to set the value of the GTK3SpinButton.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_value(self.dic_attributes["data_type"](value))

    def do_configure(
        self: _SpinButtonHost,
        adjustment: GTK3Adjustment | None,
        climb_rate: float,
        digits: int,
    ) -> None:
        """(Re)configure the GTK3SpinButton.

        Parameters
        ----------
        adjustment : GTK3Adjustment
            The GTK3Adjustment to replace the existing adjustment or None to leave
        the current adjustment unchanged.
        climb_rate : float
            The new climb rate.
        digits : int
            The number of decimal places to display in the GTK3SpinButton.
        """
        if adjustment is not None:
            self.dic_properties["adjustment"] = adjustment
        self.dic_properties["climb_rate"] = climb_rate
        self.dic_properties["digits"] = digits

        self.dic_attributes["format"] = f"{{:3.{digits}f}}"

        self.configure(adjustment, climb_rate, digits)

    @property
    def increments(self: _SpinButtonHost) -> tuple[float | None, float | None]:
        """Get the step and page increments for the embedded GTK3Adjustment.

        Returns
        -------
        tuple[float | None, float | None]
            The current step increment, or None, and page increment, or None.
        """
        return self.get_increments()

    @property
    def range(self: _SpinButtonHost) -> tuple[float | None, float | None]:
        """Get the minimum and maximum values for the embedded GTK3Adjustment.

        Returns
        -------
        tuple[float | None, float | None]
            The current minimum value, or None, and maximum value, or None.
        """
        return self.get_range()


class GTK3SpinButton(Gtk.SpinButton, GTK3SpinButtonMixin):
    """Wrapper for version 3.0 Gtk.SpinButton."""

    def __init__(
        self,
        adjustment: Gtk.Adjustment | None = None,
        climb_rate: float = 0.0,
        digits: int = 1,
    ) -> None:
        """Initialize an instance of the GTK3SpinButton widget.

        Parameters
        ----------
        adjustment : Gtk.Adjustment | None
            The adjustment to use for the spin button.  The default is None.
        climb_rate : float
            Specifies how much the rate of change in the value will accelerate if the
            user continues to hold down an up/down button or arrow key.  The default
            is 0.0.
        digits : int
            The number of decimal places to display.  The
            default is 1.
        """
        # None is valid for the adjustment argument per GTK API, so we suppress the
        # typing errors.
        Gtk.SpinButton.__init__(
            self,
            adjustment=adjustment,  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
            climb_rate=climb_rate,
            digits=digits,
        )
        GTK3SpinButtonMixin.__init__(self)

        self.dic_attributes["format"] = f"{{:3.{digits}f}}"

        self.dic_properties["adjustment"] = adjustment
        self.dic_properties["climb_rate"] = climb_rate
        self.dic_properties["digits"] = digits
