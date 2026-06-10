"""The pytkwrap GTK3CellRendererProgress module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer


class GTK3CellRendererProgress(Gtk.CellRendererProgress, GTK3CellRenderer):
    """Wrapper for version 3.0 Gtk.CellRenderer."""

    _GTK3_CELLRENDERERPROGRESS_PROPERTIES = GTK3WidgetProperties(
        inverted=False,
        pulse=-1,
        text=None,
        text_xalign=0.5,
        text_yalign=0.5,
        value=0,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererProgress."""
        Gtk.CellRendererProgress.__init__(self)
        GTK3CellRenderer.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERERPROGRESS_PROPERTIES)

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
        self.dic_properties |= properties

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
