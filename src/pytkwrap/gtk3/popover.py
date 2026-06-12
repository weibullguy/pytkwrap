"""The pytkwrap GTK3Popover module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Popover(Gtk.Popover, GTK3Bin):
    """Wrapper for version 3.0 Gtk.Popover."""

    _GTK3_POPOVER_PROPERTIES = GTK3WidgetProperties(
        constrain_to=Gtk.PopoverConstraint.WINDOW,
        modal=True,
        pointing_to=None,
        position=Gtk.PositionType.TOP,
        relative_to=None,
    )

    _GTK3_POPOVER_SIGNALS = ["closed"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Popover."""
        Gtk.Popover.__init__(self)
        GTK3Bin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_POPOVER_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_POPOVER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Popover-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Popover.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_constrain_to(self.dic_properties["constrain_to"])
        self.set_modal(self.dic_properties["modal"])

        if self.dic_properties["pointing_to"] is not None:
            self.set_pointing_to(self.dic_properties["pointing_to"])

        self.set_position(self.dic_properties["position"])
        self.set_relative_to(self.dic_properties["relative_to"])
