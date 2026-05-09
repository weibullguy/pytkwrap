"""The pytkwrap GTK3 Adjustment module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3Adjustment(Gtk.Adjustment, GTK3GObjectMixin):
    """Wrapper for Gtk.Adjustment."""

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
        Gtk.Adjustment.__init__(self)
        GTK3GObjectMixin.__init__(self)

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

    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
        """
        if property_name in self._GTK3_ADJUSTMENT_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3Adjustment.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict, preferred, non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3Adjustment.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        self.set_lower(self.dic_properties["lower"])
        self.set_page_increment(self.dic_properties["page_increment"])
        self.set_page_size(self.dic_properties["page_size"])
        self.set_step_increment(self.dic_properties["step_increment"])
        self.set_upper(self.dic_properties["upper"])

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
        value: bool | date | float | int | str | tuple | None,
    ) -> None:
        """Set the current value of the GTK3Adjustment.

        Parameters
        ----------
        value : bool | date | float | int | str | None
            The value to set for the GTK3Adjustment.
        """
        if value is None or isinstance(value, date):
            super().do_set_value(value)
            return
        self.set_value(float(value))
