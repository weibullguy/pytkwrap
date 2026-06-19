"""The pytkwrap GTK3ButtonBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ButtonBox(Gtk.ButtonBox, GTK3Box):
    """Wrapper for version 3.0 Gtk.ButtonBox."""

    _GTK3_BUTTONBOX_PROPERTIES = GTK3WidgetProperties(
        layout_style=Gtk.ButtonBoxStyle.END,
    )

    def __init__(
        self,
        orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
    ) -> None:
        """Initialize an instance of the GTK3ButtonBox."""
        Gtk.ButtonBox.__init__(self, orientation=orientation)
        GTK3Box.__init__(self)

        self.dic_properties.update(self._GTK3_BUTTONBOX_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ButtonBox-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ButtonBox.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_layout(self.dic_properties["layout_style"])
