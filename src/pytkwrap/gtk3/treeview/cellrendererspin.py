"""The pytkwrap GTK3CellRendererSpin module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderertext import GTK3CellRendererText


class GTK3CellRendererSpin(Gtk.CellRendererSpin, GTK3CellRendererText):
    """Wrapper for version 3.0 Gtk.CellRendererSpin."""

    _GTK3_CELLRENDERERSPIN_PROPERTIES = GTK3WidgetProperties(
        adjustment=None,
        climb_rate=0.0,
        digits=0,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRenderer."""
        Gtk.CellRendererSpin.__init__(self)
        GTK3CellRendererText.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERERSPIN_PROPERTIES)

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
        self.dic_properties |= properties

        for _property in [
            "adjustment",
            "climb_rate",
            "digits",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
