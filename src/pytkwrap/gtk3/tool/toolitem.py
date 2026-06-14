"""The pytkwrap GTK3ToolItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ToolItem(Gtk.ToolItem, GTK3Bin):
    """Wrapper for version 3.0 Gtk.ToolItem."""

    _GTK3_TOOLITEM_PROPERTIES = GTK3WidgetProperties(
        is_important=False,
        visible_horizontal=True,
        visible_vertical=True,
    )
    _GTK3_TOOLITEM_SIGNALS = ["create-menu-proxy", "toolbar-reconfigured"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ToolItem."""
        Gtk.ToolItem.__init__(self)
        GTK3Bin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOOLITEM_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TOOLITEM_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Widget-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Widget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        # Set the value of each of the mixin properties.
        self.set_is_important(self.dic_properties["is_important"])
        self.set_visible_horizontal(self.dic_properties["visible_horizontal"])
        self.set_visible_vertical(self.dic_properties["visible_vertical"])
