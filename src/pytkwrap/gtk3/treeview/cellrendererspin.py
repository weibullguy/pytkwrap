"""The pytkwrap GTK3CellRendererSpin module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderertext import GTK3CellRendererTextMixin


class GTK3CellRendererSpinMixin(GTK3CellRendererTextMixin):
    """Mixin class for GTK3CellRendererSpin."""

    _GTK3_CELLRENDERERSPIN_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        climb_rate=0.0,
        digits=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CellRendererSpin mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CELLRENDERERSPIN_PROPERTIES)

    def do_get_value(self) -> float:
        """Get the value of the GTK3CellRendererSpin.

        Returns
        -------
        The value of the GTK3CellRendererSpin.  A float representing the value.
        """
        return self.get_property("adjustment").get_value()

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererSpin-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererSpin.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in [
            "adjustment",
            "climb_rate",
            "digits",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None:
        """Set the value of the GTK3CellRendererSpin.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The number to set the value of the GTK3CellRendererSpin.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)
        self.get_property("adjustment").set_value(float(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long


class GTK3CellRendererSpin(Gtk.CellRendererSpin, GTK3CellRendererSpinMixin):
    """Wrapper for version 3.0 Gtk.CellRendererSpin."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRenderer."""
        Gtk.CellRendererSpin.__init__(self)
        GTK3CellRendererSpinMixin.__init__(self)
