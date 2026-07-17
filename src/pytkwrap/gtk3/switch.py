"""The pytkwrap GTK3Switch module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3Switch(Gtk.Switch, GTK3Widget):
    """Wrapper for version 3.0 Gtk.Switch."""

    _GTK3_SWITCH_PROPERTIES = GTK3WidgetProperties(
        active=False,
        state=False,
    )
    _GTK3_SWITCH_SIGNALS = [
        "activate",
        "state-set",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Switch."""
        Gtk.Switch.__init__(self)
        GTK3Widget.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SWITCH_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SWITCH_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Switch-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Switch.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_active(self.dic_properties["active"])
        self.set_state(self.dic_properties["state"])
