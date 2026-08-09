"""The pytkwrap GTK3CellRendererProgress module.

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


class GTK3CellRendererProgressMixin(GTK3CellRendererMixin):
    """Mixin class for GTK3CellRendererProgress."""

    _GTK3_CELLRENDERERPROGRESS_PROPERTIES = GTK3WidgetProperties(
        inverted=False,
        pulse=-1,
        text=None,
        text_xalign=0.5,
        text_yalign=0.5,
        value=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CellRendererProgress mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CELLRENDERERPROGRESS_PROPERTIES)

    def do_get_value(self) -> int:
        """Get the value of the GTK3CellRendererProgress.

        Returns
        -------
        The value of the GTK3CellRendererProgress.  An integer representing the
        percent fill.
        """
        return self.get_property("value")

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererProgress-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererProgress.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in [
            "inverted",
            "pulse",
            "text",
            "text_xalign",
            "text_yalign",
            "value",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None:
        """Set the value of the GTK3CellRendererProgress.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The number to set the value of the GTK3CellRendererProgress.
        """
        if not isinstance(value, (int, float)):
            super().do_set_value(value)
        self.dic_properties["value"] = int(value)  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
        self.set_property("value", int(value))  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long


class GTK3CellRendererProgress(Gtk.CellRendererProgress, GTK3CellRendererProgressMixin):
    """Wrapper for version 3.0 Gtk.CellRenderer."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererProgress."""
        Gtk.CellRendererProgress.__init__(self)
        GTK3CellRendererProgressMixin.__init__(self)
