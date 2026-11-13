"""The pytkwrap GTK3ToggleButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.button import GTK3ButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ToggleButtonHost


class GTK3ToggleButtonMixin(GTK3ButtonMixin):
    """Mixin for GTK3ToggleButton.

    Notes
    -----
    GTK3ToggleButton passes a Gtk.Label to its callback function.
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_TOGGLE_BUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value=False,  # i.e., not active
        edit_signal="toggled",
    )
    _GTK3_TOGGLE_BUTTON_PROPERTIES = GTK3WidgetProperties(
        active=False,
        draw_indicator=False,
        inconsistent=False,
    )
    _GTK3_TOGGLE_BUTTON_SIGNALS = [
        "toggled",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ToggleButton widget."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_TOGGLE_BUTTON_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_TOGGLE_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOGGLE_BUTTON_SIGNALS}
        )

    def do_set_properties(
        self: _ToggleButtonHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3ToggleButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ToggleButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_active(self.dic_properties["active"])  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
        self.set_inconsistent(self.dic_properties["inconsistent"])
        self.set_mode(self.dic_properties["draw_indicator"])

    def do_get_value(
        self: _ToggleButtonHost,
    ) -> bool | date | float | int | object | str | None:
        """Return the current value of the GTK3ToggleButton.

        Returns
        -------
        bool
            The current value of the GTK3ToggleButton.
        """
        return self.get_active()

    def do_set_value(
        self: _ToggleButtonHost,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3ToggleButton.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The value to set for the GTK3ToggleButton.
        """
        if not isinstance(value, (bool, float, int)):
            super().do_set_value(value)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long
        self.dic_properties["active"] = bool(value)
        self.set_active(bool(value))


class GTK3ToggleButton(Gtk.ToggleButton, GTK3ToggleButtonMixin):
    """Wrapper for version 3.0 Gtk.ToggleButton."""

    def __init__(self, label: str = "...") -> None:
        """Initialize an instance of the GTK3ToggleButton widget.

        Parameters
        ----------
        label : str
            The text to display in the GTK3ToggleButton label.  The default value is
            an ellipsis (...).
        """
        Gtk.ToggleButton.__init__(self, label=label)
        GTK3ToggleButtonMixin.__init__(self)

        self.dic_properties["label"] = label
