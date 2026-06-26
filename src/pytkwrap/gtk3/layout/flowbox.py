"""The pytkwrap GTK3FlowBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FlowBox(Gtk.FlowBox, GTK3Container):
    """Wrapper for version 3.0 Gtk.FlowBox."""

    _GTK3_FLOWBOX_PROPERTIES = GTK3WidgetProperties(
        activate_on_single_click=True,
        column_spacing=0,
        homogeneous=False,
        max_children_per_line=7,
        min_children_per_line=0,
        row_spacing=0,
        selection_mode=Gtk.SelectionMode.SINGLE,
    )
    _GTK3_FLOWBOX_SIGNALS = [
        "activate-cursor-child",
        "child-activated",
        "move-cursor",
        "select-all",
        "selected-children-changed",
        "toggle-cursor-child",
        "unselect-all",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FlowBox."""
        Gtk.FlowBox.__init__(self)
        GTK3Container.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_FLOWBOX_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_FLOWBOX_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3FlowBox-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3FlowBox.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_activate_on_single_click(
            self.dic_properties["activate_on_single_click"]
        )
        self.set_column_spacing(self.dic_properties["column_spacing"])
        self.set_homogeneous(self.dic_properties["homogeneous"])
        self.set_max_children_per_line(self.dic_properties["max_children_per_line"])
        self.set_min_children_per_line(self.dic_properties["min_children_per_line"])
        self.set_row_spacing(self.dic_properties["row_spacing"])
        self.set_selection_mode(self.dic_properties["selection_mode"])
