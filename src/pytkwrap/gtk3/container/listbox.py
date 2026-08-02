"""The pytkwrap GTK3ListBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ListBoxMixin(GTK3ContainerMixin):
    """Mixin class for GTK3ListBox."""

    _GTK3_LISTBOX_PROPERTIES = GTK3WidgetProperties(
        activate_on_single_click=True,
        selection_mode=Gtk.SelectionMode.SINGLE,
    )
    _GTK3_LISTBOX_SIGNALS = [
        "activate-cursor-row",
        "move-cursor",
        "row-activated",
        "row-selected",
        "select-all",
        "selected-rows-changed",
        "toggle-cursor-row",
        "unselect-all",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ListBox mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_LISTBOX_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_LISTBOX_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ListBox-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ListBox.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_activate_on_single_click(
            self.dic_properties["activate_on_single_click"]
        )
        self.set_selection_mode(self.dic_properties["selection_mode"])


class GTK3ListBox(Gtk.ListBox, GTK3ListBoxMixin):
    """Wrapper for version 3.0 Gtk.ListBox."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ListBox."""
        # GTK3ListBox does not initialize when calling super().__init__().
        Gtk.ListBox.__init__(self)
        GTK3ListBoxMixin.__init__(self)
