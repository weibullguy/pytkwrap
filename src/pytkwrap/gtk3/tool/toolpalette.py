"""The pytkwrap GTK3ToolPalette module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ToolPalette(Gtk.ToolPalette, GTK3Container):
    """Wrapper for version 3.0 Gtk.ToolPalette."""

    _GTK3_TOOLPALETTE_PROPERTIES = GTK3WidgetProperties(
        icon_size=Gtk.IconSize.SMALL_TOOLBAR,
        icon_size_set=False,
        toolbar_style=Gtk.ToolbarStyle.ICONS,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ToolPalette."""
        Gtk.ToolPalette.__init__(self)
        GTK3Container.__init__(self)

        self.dic_properties.update(self._GTK3_TOOLPALETTE_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ToolPalette-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ToolPalette.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_icon_size(self.dic_properties["icon_size"])
        self.set_style(self.dic_properties["toolbar_style"])
