"""The pytkwrap GTK3CellRendererSpinner module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer


class GTK3CellRendererSpinner(Gtk.CellRendererSpinner, GTK3CellRenderer):
    """Wrapper for version 3.0 Gtk.CellRendererSpinner."""

    _GTK3_CELLRENDERERSPINNER_PROPERTIES = GTK3WidgetProperties(
        active=False,
        pulse=0,
        size=Gtk.IconSize.MENU,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererSpinner."""
        Gtk.CellRendererSpinner.__init__(self)
        GTK3CellRenderer.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERERSPINNER_PROPERTIES)

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
        self.dic_properties |= properties

        for _property in [
            "active",
            "pulse",
            "size",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
