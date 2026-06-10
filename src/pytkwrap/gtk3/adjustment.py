"""The pytkwrap GTK3Adjustment module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes

# noinspection PyUnresolvedReferences
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import (
    GTK3GObjectMixin,
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
)


class GTK3Adjustment(Gtk.Adjustment, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.Adjustment."""

    _GTK3_ADJUSTMENT_ATTRIBUTES = GTK3WidgetAttributes(
        default_value=0.0,
        edit_signal="value-changed",
    )
    _GTK3_ADJUSTMENT_PROPERTIES = GTK3WidgetProperties(
        lower=0.0,
        upper=0.0,
        value=0.0,
        step_increment=0.0,
        page_increment=0.0,
        page_size=0.0,
    )
    _GTK3_ADJUSTMENT_SIGNALS = [
        "changed",
        "value-changed",
    ]

    def __init__(
        self,
        value: float = 0.0,
        lower: float = 0.0,
        upper: float = 0.0,
        step_increment: float = 0.0,
        page_increment: float = 0.0,
        page_size: float = 0.0,
    ) -> None:
        """Initialize an instance of the GTK3Adjustment.

        Parameters
        ----------
        value : float
            The value between the lower and upper bound to set for the GTK3Adjustment.
        lower : float
            The smallest value the GTK3Adjustment can take.
        upper : float
            The largest value the GTK3Adjustment can take.
        step_increment : float
            The step increment for the GTK3Adjustment.
        page_increment : float
            The page increment for the GTK3Adjustment.
        page_size : float
            The page size of the GTK3Adjustment.
        """
        Gtk.Adjustment.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_attributes.update(self._GTK3_ADJUSTMENT_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_ADJUSTMENT_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ADJUSTMENT_SIGNALS}
        )

        self.do_set_properties(
            GTK3WidgetProperties(
                lower=lower,
                upper=upper,
                page_increment=page_increment,
                page_size=page_size,
                step_increment=step_increment,
                value=value,
            )
        )
        self.do_set_value(self.dic_properties["value"])

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
        if attribute in self._GTK3_ADJUSTMENT_ATTRIBUTES:
            return self.dic_attributes.get(attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: PyTkWrapAttributes) -> None:
        """Set the values of the GTK3Adjustment-specific attributes.

        Parameters
        ----------
        attributes : GTK3WidgetAttributes
            The typed dict (preferred), or non-typed dict with the attribute values to
            set for the GTK3Adjustment.
        """
        super().do_set_attributes(attributes)

        for _attr in self._GTK3_ADJUSTMENT_ATTRIBUTES:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Adjustment-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3Adjustment.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        self.set_lower(self.dic_properties["lower"])
        self.set_page_increment(self.dic_properties["page_increment"])
        self.set_page_size(self.dic_properties["page_size"])
        self.set_step_increment(self.dic_properties["step_increment"])
        self.set_upper(self.dic_properties["upper"])
        self.set_value(self.dic_properties["value"])

    def do_get_value(self) -> float:
        """Return the current value of the GTK3Adjustment.

        Returns
        -------
        float
            The current value of the GTK3Adjustment.
        """
        return self.get_value()

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3Adjustment.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The value to set for the GTK3Adjustment.
        """
        if value is None or isinstance(value, (date, tuple)):
            super().do_set_value(value)
        self.set_value(float(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
