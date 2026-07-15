"""The pytkwrap GTK3Range module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3Range(Gtk.Range, GTK3Widget):
    """Wrapper for version 3.0 Gtk.Range."""

    _GTK3_RANGE_ATTRIBUTES = GTK3WidgetAttributes(
        edit_signal="value-changed",
    )
    _GTK3_RANGE_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        fill_level=1.7976931348623157e308,
        inverted=False,
        restrict_to_fill_level=True,
        round_digits=-1,
        show_fill_level=False,
    )
    _GTK3_RANGE_SIGNALS = [
        "adjust-bounds",
        "change-value",
        "move-slider",
        "value-changed",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Range."""
        Gtk.Range.__init__(self)
        GTK3Widget.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_RANGE_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_RANGE_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_RANGE_PROPERTIES)

    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
            The value of the requested attribute.
        """
        if attribute in self._GTK3_RANGE_ATTRIBUTES:
            return self.dic_attributes.get(attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: Mapping[str, object]) -> None:
        """Set the values of the GTK3Range-specific attributes.

        Parameters
        ----------
        attributes : GTK3WidgetAttributes
            The typed dict (preferred), or non-typed dict with the attribute values to
            set for the GTK3Range.
        """
        super().do_set_attributes(attributes)

        for _attr in self._GTK3_RANGE_ATTRIBUTES:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Range-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Range.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["adjustment"] is not None:
            self.set_adjustment(self.dic_properties["adjustment"])

        self.set_fill_level(self.dic_properties["fill_level"])
        self.set_inverted(self.dic_properties["inverted"])
        self.set_restrict_to_fill_level(self.dic_properties["restrict_to_fill_level"])
        self.set_round_digits(self.dic_properties["round_digits"])
        self.set_show_fill_level(self.dic_properties["show_fill_level"])

    def do_get_value(self) -> float:
        """Return the current value of the GTK3Range.

        Returns
        -------
        float
            The current value of the GTK3Range.
        """
        return self.get_value()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3Range.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The value to set for the GTK3Range.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)
        self.set_value(float(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
