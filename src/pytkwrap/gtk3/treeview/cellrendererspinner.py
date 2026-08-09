"""The pytkwrap GTK3CellRendererSpinner module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRendererMixin


class GTK3CellRendererSpinnerMixin(GTK3CellRendererMixin):
    """Mixin class for GTK3CellRendererSpinner."""

    _GTK3_CELLRENDERERSPINNER_PROPERTIES = GTK3WidgetProperties(
        active=False,
        pulse=0,
        size=Gtk.IconSize.MENU,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CellRendererSpinner mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CELLRENDERERSPINNER_PROPERTIES)

    def do_get_value(self) -> int:
        """Get the value of the GTK3CellRendererSpinner.

        Returns
        -------
        The value of the GTK3CellRendererSpinner.  An integer representing the number
        of frames that are displayed.  There are a total of 12 frames in a
        Gtk.CellRendererSpinner.
        """
        return self.get_property("pulse")

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererSpinner-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererSpinner.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in [
            "active",
            "pulse",
            "size",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None:
        """Set the value of the GTK3CellRendererSpinner."""
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)
        self.dic_properties["pulse"] = int(value)  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
        self.set_property("pulse", int(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long


class GTK3CellRendererSpinner(Gtk.CellRendererSpinner, GTK3CellRendererSpinnerMixin):
    """Wrapper for version 3.0 Gtk.CellRendererSpinner."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererSpinner."""
        Gtk.CellRendererSpinner.__init__(self)
        GTK3CellRendererSpinnerMixin.__init__(self)
