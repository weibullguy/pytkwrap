"""The pytkwrap GTK3SeparatorToolItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolitem import GTK3ToolItem


class GTK3SeparatorToolItem(Gtk.SeparatorToolItem, GTK3ToolItem):
    """Wrapper for version 3.0 Gtk.SeparatorToolItem."""

    _GTK3_SEPARATORTOOLITEM_PROPERTIES = GTK3WidgetProperties(
        draw=True,
    )
    _GTK3_TOOLITEM_SIGNALS = ["create-menu-proxy", "toolbar-reconfigured"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3SeparatorToolItem."""
        Gtk.SeparatorToolItem.__init__(self)
        GTK3ToolItem.__init__(self)

        self.dic_properties.update(self._GTK3_SEPARATORTOOLITEM_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3SeparatorToolItem-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3SeparatorToolItem.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        # Set the value of each of the mixin properties.
        self.set_draw(self.dic_properties["draw"])
