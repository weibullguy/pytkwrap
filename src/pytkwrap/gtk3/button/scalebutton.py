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
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.button.button import GTK3ButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ScaleButtonMixin(GTK3ButtonMixin):
    """Mixin for GTK3ScaleButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
    _GTK3_SCALE_BUTTON_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        default_value=0.0,
        edit_signal="value-changed",
    )
    _GTK3_SCALE_BUTTON_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        icons=None,
        size=4,  # Button sized.
        value=0.0,
    )
    _GTK3_SCALE_BUTTON_SIGNALS = [
        "popdown",
        "popup",
        "value-changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ScaleButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_SCALE_BUTTON_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SCALE_BUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SCALE_BUTTON_PROPERTIES)

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

        if (
            self.dic_properties["icons"] is not None
            and len(self.dic_properties["icons"]) > 0
        ):
            self.set_icons(self.dic_properties["icons"])

        self.set_value(self.dic_properties["value"])

        self.set_property("size", self.dic_properties["size"])

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
        self.dic_properties["value"] = float(value)  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
        self.set_value(float(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long


class GTK3ScaleButton(Gtk.ScaleButton, GTK3ScaleButtonMixin):
    """Wrapper for version 3.0 Gtk.ScaleButton."""

    def __init__(
        self,
        size: int,
        min_value: float = 0.0,
        max_value: float = 100.0,
        step: float = 2,
        icons: list | None = None,
    ) -> None:
        """Initialize an instance of the GTK3ScaleButton widget."""
        super().__init__(
            adjustment=GTK3Adjustment(min_value, min_value, max_value, step),
            icons=icons,
            size=size,
        )
        GTK3ScaleButtonMixin.__init__(self)

        self.dic_properties["adjustment"] = GTK3Adjustment(
            min_value,
            min_value,
            max_value,
            step,
        )
        self.dic_properties["icons"] = icons
        self.dic_properties["size"] = size
