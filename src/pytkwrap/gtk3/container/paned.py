"""The pytkwrap GTK3Paned module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Paned(Gtk.Paned, GTK3Container):
    """Wrapper for version 3.0 Gtk.Paned."""

    _GTK3_PANED_PROPERTIES = GTK3WidgetProperties(
        position=0,
        position_set=False,
        wide_handle=False,
    )
    _GTK3_PANED_SIGNALS = [
        "accept-position",
        "cancel-position",
        "cycle-child-focus",
        "cycle-handle-focus",
        "move-handle",
        "toggle-handle-focus",
    ]

    def __init__(
        self, orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL
    ) -> None:
        """Initialize an instance of the GTK3Paned."""
        Gtk.Paned.__init__(self, orientation=orientation)
        GTK3Container.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_PANED_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_PANED_PROPERTIES)

        self.orientation = orientation

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Paned-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Paned.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_position(self.dic_properties["position"])
        self.set_wide_handle(self.dic_properties["wide_handle"])

        for _property in ["position_set"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
