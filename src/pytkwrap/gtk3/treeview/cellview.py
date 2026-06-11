"""The pytkwrap GTK3CellView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3CellView(Gtk.CellView, GTK3Widget):
    """Wrapper for version 3.0 Gtk.CellView."""

    _DEFAULT_HEIGHT = -1
    _DEFAULT_WIDTH = -1
    _GTK3_CELLVIEW_PROPERTIES = GTK3WidgetProperties(
        background=None,
        background_rgba=None,
        background_set=False,
        cell_area=None,
        cell_area_context=None,
        draw_sensitive=False,
        fit_model=False,
        model=None,
    )

    def __init__(
        self,
        cell_area_context: Gtk.CellAreaContext = None,
    ) -> None:
        """Initialize an instance of the GTK3CellView."""
        Gtk.CellView.__init__(
            self,
            cell_area_context=cell_area_context,
        )
        GTK3Widget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CELLVIEW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellView-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3CellView.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["background_rgba"] is not None:
            self.set_background_rgba(self.dic_properties["background_rgba"])

        self.set_draw_sensitive(self.dic_properties["draw_sensitive"])
        self.set_fit_model(self.dic_properties["fit_model"])
        self.set_model(self.dic_properties["model"])

        for _property in ["background", "background_set"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
