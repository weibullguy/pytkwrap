"""The pytkwrap GTK3StackSwitcher module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3StackSwitcher(Gtk.StackSwitcher, GTK3Box):
    """Wrapper for version 3.0 Gtk.StackSwitcher."""

    _GTK3_STACKSWITCHER_PROPERTIES = GTK3WidgetProperties(
        icon_size=1,
        stack=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3StackSwitcher."""
        Gtk.StackSwitcher.__init__(self)
        GTK3Box.__init__(self)

        self.dic_properties.update(self._GTK3_STACKSWITCHER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3StackSwitcher-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3StackSwitcher.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_stack(self.dic_properties["stack"])

        for _property in ["icon_size"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
