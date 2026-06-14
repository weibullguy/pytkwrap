"""The pytkwrap GTK3Viewport module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Viewport(Gtk.Viewport, GTK3Bin):
    """Wrapper for version 3.0 Gtk.Viewport."""

    _GTK3_VIEWPORT_PROPERTIES = GTK3WidgetProperties(
        shadow_type=Gtk.ShadowType.IN,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Viewport."""
        Gtk.Viewport.__init__(self)
        GTK3Bin.__init__(self)

        self.dic_properties.update(self._GTK3_VIEWPORT_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Viewport-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Viewport.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_shadow_type(self.dic_properties["shadow_type"])
