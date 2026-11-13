"""The pytkwrap GTK3ScaleButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from datetime import date
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.button.button import GTK3ButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ScaleButtonHost


class GTK3ScaleButtonMixin(GTK3ButtonMixin):
    """Mixin for GTK3ScaleButton.

    Attributes
    ----------
    _DEFAULT_HEIGHT : int
        The default height of the GTK3ScaleButton.
    _DEFAULT_WIDTH : int
        The default width of the GTK3ScaleButton.
    _GTK3_SCALEBUTTON_ATTRIBUTES : PyTkWrapAttributes
        GTK3ScaleButton-specific attributes.
    _GTK3_SCALEBUTTON_PROPERTIES : GTK3WidgetProperties
        GTK3ScaleButton-specific properties.
    _GTK3_SCALEBUTTON_SIGNALS : list[str]
        List of GTK3ScaleButton-specific signals.
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
    _GTK3_SCALEBUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value=0.0,
        edit_signal="value-changed",
    )
    _GTK3_SCALEBUTTON_PROPERTIES = GTK3WidgetProperties(
        adjustment=GTK3Adjustment(),
        icons=None,
        size=4,  # Button size.
        value=0.0,
    )
    _GTK3_SCALEBUTTON_SIGNALS = [
        "popdown",
        "popup",
        "value-changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ScaleButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_SCALEBUTTON_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SCALEBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SCALEBUTTON_PROPERTIES)

    def do_set_properties(
        self: _ScaleButtonHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3ScaleButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ScaleButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        if self.dic_properties["adjustment"] is not None:
            self.set_adjustment(self.dic_properties["adjustment"])

        if (
            self.dic_properties["icons"] is not None
            and len(self.dic_properties["icons"]) > 0
        ):
            self.set_icons(self.dic_properties["icons"])

        self.set_value(self.dic_properties["value"])

        self.set_property("size", self.dic_properties["size"])

    def do_get_value(
        self: _ScaleButtonHost,
    ) -> bool | date | float | int | object | str | None:
        """Return the current value of the GTK3ScaleButton.

        Returns
        -------
        float
            The current value of the GTK3ScaleButton.
        """
        return self.get_value()

    def do_set_value(
        self: _ScaleButtonHost,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3ScaleButton.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The value to set for the GTK3ScaleButton.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long
        self.dic_properties["value"] = float(value)  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
        self.set_value(float(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long

    def do_configure(
        self: _ScaleButtonHost,
        value: float,
        lower: float,
        upper: float,
        step_increment: float,
        page_increment: float,
        page_size: float,
    ) -> None:
        """Configure the GTK3ScaleButton's GTK3Adjustment.

        Parameters
        ----------
        value : float
            The new value.
        lower : float
            The new minimum value.
        upper : float
            The new maximum value.
        step_increment : float
            The new step increment.
        page_increment : float
            The new page increment.
        page_size : float
            The new page size.
        """
        self.dic_properties["value"] = value

        return self.dic_properties["adjustment"].configure(
            value,
            lower,
            upper,
            step_increment,
            page_increment,
            page_size,
        )

    @property
    def lower(self: _ScaleButtonHost) -> float:
        """Get the minimum value of the GTK3ScaleButton's GTK3Adjustment.

        Returns
        -------
        float
            The minimum value.
        """
        return self.dic_properties["adjustment"].get_lower()

    @property
    def minus_button(self: _ScaleButtonHost) -> Gtk.Button:
        """Get the minus button of the GTK3ScaleButton.

        Returns
        -------
        Gtk.Button
            The GTK3ScaleButton's minus button.
        """
        return self.get_minus_button()

    @property
    def page_increment(self: _ScaleButtonHost) -> float:
        """Get the page increment of the GTK3ScaleButton's GTK3Adjustment.

        Returns
        -------
        float
            The currently set page increment.
        """
        return self.dic_properties["adjustment"].get_page_increment()

    @property
    def page_size(self: _ScaleButtonHost) -> float:
        """Get the page size of the GTK3ScaleButton's GTK3Adjustment.

        Returns
        -------
        float
            The page size.
        """
        return self.dic_properties["adjustment"].get_page_size()

    @property
    def plus_button(self: _ScaleButtonHost) -> Gtk.Button:
        """Get the plus button of the GTK3ScaleButton.

        Returns
        -------
        Gtk.Button
            The GTK3ScaleButton's plus button.
        """
        return self.get_plus_button()

    @property
    def popup(self: _ScaleButtonHost) -> Gtk.Widget:
        """Get the popup of the GTK3ScaleButton.

        Returns
        -------
        Gtk.Widget
            The popup of the GTK3ScaleButton.
        """
        return self.get_popup()

    @property
    def step_increment(self: _ScaleButtonHost) -> float:
        """Get the step increment of the GTK3ScaleButton's GTK3Adjustment.

        Returns
        -------
        float
            The step increment.
        """
        return self.dic_properties["adjustment"].get_step_increment()

    @property
    def upper(self: _ScaleButtonHost) -> float:
        """Get the maximum value of the GTK3ScaleButton's GTK3Adjustment.

        Returns
        -------
        float
            The maximum value.
        """
        return self.dic_properties["adjustment"].get_upper()


class GTK3ScaleButton(Gtk.ScaleButton, GTK3ScaleButtonMixin):
    """Wrapper for version 3.0 Gtk.ScaleButton."""

    def __init__(
        self,
        icons: Sequence[str],
        size: Gtk.IconSize,
        min_value: float = 0.0,
        max_value: float = 100.0,
        step: float = 2,
    ) -> None:
        """Initialize an instance of the GTK3ScaleButton widget.

        Parameters
        ----------
        icons : Sequence[str]
            A list of icon names to be used by the scale button.  The default is an
            empty list which means the set_icons() method will have to be used to set
            the icons after initialization.
        size : int
            A stock icon size.
        min_value : float
            The minimum value of the scale.  The default is 0.0.
        max_value : float
            The maximum value of the scale.  The default is 100.0.
        step : float
            The stepping value when a scroll-wheel event, or up/down arrow event
            occurs.  The default is 2.0.
        """
        _adjustment = GTK3Adjustment(min_value, min_value, max_value, step)

        Gtk.ScaleButton.__init__(
            self,
            adjustment=_adjustment,
            icons=icons,
            size=size,
        )
        GTK3ScaleButtonMixin.__init__(self)

        self.dic_properties["adjustment"] = _adjustment
        self.dic_properties["icons"] = icons
        self.dic_properties["size"] = size
