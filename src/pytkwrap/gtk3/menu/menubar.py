"""The pytkwrap GTK3MenuBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.menushell import GTK3MenuShell
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MenuBar(Gtk.MenuBar, GTK3MenuShell):
    """Wrapper for version 3.0 Gtk.MenuBar."""

    _GTK3_MENUBAR_PROPERTIES = GTK3WidgetProperties(
        child_pack_direction=Gtk.PackDirection.LTR,
        pack_direction=Gtk.PackDirection.LTR,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuBar."""
        Gtk.MenuBar.__init__(self)
        GTK3MenuShell.__init__(self)

        self.dic_properties.update(self._GTK3_MENUBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MenuBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MenuBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_child_pack_direction(self.dic_properties["child_pack_direction"])
        self.set_pack_direction(self.dic_properties["pack_direction"])
