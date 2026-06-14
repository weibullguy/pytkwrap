"""The pytkwrap GTK3MenuToolButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolbutton import GTK3ToolButton


class GTK3MenuToolButton(Gtk.MenuToolButton, GTK3ToolButton):
    """Wrapper for version 3.0 Gtk.MenuToolButton."""

    _GTK3_MENUTOOLBUTTON_PROPERTIES = GTK3WidgetProperties(
        menu=None,
    )
    _GTK3_MENUTOOLBUTTON_SIGNALS = ["show-menu"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuToolButton."""
        Gtk.MenuToolButton.__init__(self)
        GTK3ToolButton.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_MENUTOOLBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_MENUTOOLBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MenuToolButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MenuToolButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["menu"] is not None:
            self.set_menu(self.dic_properties["menu"])
