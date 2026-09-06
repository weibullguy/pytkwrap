"""The pytkwrap GTK3FlowBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FlowBoxMixin(GTK3ContainerMixin):
    """Mixin class for GTK3FlowBox.

    Notes
    -----
    GTK3FlowBox passes no widgets to its callback function.
    """

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

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3FlowBox mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
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

    def do_populate_flowbox(self, widgets: list[tuple[Gtk.Widget, int]]) -> None:
        """Populate the GTK3FlowBox with the given widgets at the given positions.

        Parameters
        ----------
        widgets : list[tuple[Gtk.Widget, int]]
            A list of tuples containing the widget to add to the GTK3FlowBox and the
            position to add each widget.  Set position to -1 to append the widget.
        """
        for _widget in widgets:
            self.insert(_widget[0], _widget[1])

    def do_unpopulate_flowbox(self, index: list[int]) -> None:
        """Remove widget(s) at indices from the GTK3FlowBox.

        Parameters
        ----------
        index : list[int]
            A list of widget indices to remove from the GTK3FlowBox.  Indices should
            be listed in reverse order because the indices will update as each widget is
            removed.

        Examples
        --------
        do_unpopulate_flowbox([3, 2, 1]) will remove the first, second, and third
        widgets starting with index 3 in a GTK3FlowBox with four or more widgets.

        do_unpopulate_flowbox([2, 2]) will remove the last two widgets in a
        GTK3FlowBox with three or more widgets.
        """
        for _index in index:
            _child = self.get_child_at_index(_index)
            self.remove(_child)


class GTK3FlowBox(Gtk.FlowBox, GTK3FlowBoxMixin):
    """Wrapper for version 3.0 Gtk.FlowBox."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FlowBox."""
        Gtk.FlowBox.__init__(self)
        GTK3FlowBoxMixin.__init__(self)
