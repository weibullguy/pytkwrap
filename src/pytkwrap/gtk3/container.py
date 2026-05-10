"""The pytkwrap GTK3 Container module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3Container(Gtk.Container, GTK3Widget):
    """Wrapper for Gtk.Container."""

    _GTK3_CONTAINER_PROPERTIES = GTK3WidgetProperties(
        border_width=0,
    )
    _GTK3_CONTAINER_SIGNALS = [
        "add",
        "check-resize",
        "remove",
        "set-focus-child",
    ]

    def __init__(self) -> None:
        Gtk.Container.__init__(self)
        GTK3Widget.__init__(self)

        self.dic_properties.update(self._GTK3_CONTAINER_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CONTAINER_SIGNALS}
        )

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
        if property_name in self._GTK3_CONTAINER_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3Calendar.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict, preferred, non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3Container.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_border_width(self.dic_properties["border_width"])
