"""The pytkwrap GTK3MenuShell module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MenuShell(Gtk.MenuShell, GTK3Container):
    """Wrapper for version 3.0 Gtk.MenuShell."""

    _GTK3_MENUSHELL_PROPERTIES = GTK3WidgetProperties(
        take_focus=True,
    )
    _GTK3_MENUSHELL_SIGNALS = [
        "activate-current",
        "cancel",
        "cycle-focus",
        "deactivate",
        "insert",
        "move-current",
        "move-selected",
        "selection-done",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuShell."""
        Gtk.MenuShell.__init__(self)
        GTK3Container.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_MENUSHELL_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_MENUSHELL_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MenuShell-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MenuShell.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_take_focus(self.dic_properties["take_focus"])
