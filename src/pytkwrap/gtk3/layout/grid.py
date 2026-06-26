"""The pytkwrap GTK3Grid module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Grid(Gtk.Grid, GTK3Container):
    """Wrapper for version 3.0 Gtk.Grid."""

    _GTK3_GRID_ATTRIBUTES = {"n_columns": 1, "n_rows": 1}
    _GTK3_GRID_PROPERTIES = GTK3WidgetProperties(
        baseline_row=0,
        column_homogeneous=False,
        column_spacing=0,
        row_homogeneous=False,
        row_spacing=0,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Grid."""
        Gtk.Grid.__init__(self)
        GTK3Container.__init__(self)

        self.dic_attributes.update(self._GTK3_GRID_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_GRID_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Grid-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Grid.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_baseline_row(self.dic_properties["baseline_row"])
        self.set_column_homogeneous(self.dic_properties["column_homogeneous"])
        self.set_column_spacing(self.dic_properties["column_spacing"])
        self.set_row_homogeneous(self.dic_properties["row_homogeneous"])
        self.set_row_spacing(self.dic_properties["row_spacing"])
