"""The pytkwrap GTK3TreeView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3TreeView(Gtk.TreeView, GTK3Container):
    """Wrapper for version 3.0 Gtk.TreeView."""

    _GTK3_TREEVIEW_PROPERTIES = GTK3WidgetProperties(
        activate_on_single_click=False,
        enable_grid_lines=Gtk.TreeViewGridLines.NONE,
        enable_search=True,
        enable_tree_lines=False,
        expander_column=None,
        fixed_height_mode=False,
        headers_clickable=True,
        headers_visible=True,
        hover_expand=False,
        hover_selection=False,
        level_indentation=0,
        model=None,
        reorderable=False,
        rubber_banding=False,
        search_column=-1,
        show_expanders=True,
        tooltip_column=-1,
    )
    _GTK3_TREEVIEW_SIGNALS = [
        "columns-changed",
        "cursor-changed",
        "expand-collapse-cursor-row",
        "move-cursor",
        "row-activated",
        "row-collapsed",
        "row-expanded",
        "select-all",
        "select-cursor-parent",
        "select-cursor-row",
        "start-interactive-search",
        "test-collapse-row",
        "test-expand-row",
        "toggle-cursor-row",
        "unselect-all",
    ]

    def __init__(self, model: Gtk.TreeModel = None) -> None:
        """Initialize an instance of the GTK3TreeView."""
        Gtk.TreeView.__init__(self, model=model)
        GTK3Container.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TREEVIEW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TREEVIEW_PROPERTIES)
        self.dic_properties["model"] = model

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3TreeView-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3TreeView.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_activate_on_single_click(
            self.dic_properties["activate_on_single_click"]
        )
        self.set_grid_lines(self.dic_properties["enable_grid_lines"])
        self.set_enable_search(self.dic_properties["enable_search"])
        self.set_enable_tree_lines(self.dic_properties["enable_tree_lines"])
        self.set_fixed_height_mode(self.dic_properties["fixed_height_mode"])
        self.set_headers_clickable(self.dic_properties["headers_clickable"])
        self.set_headers_visible(self.dic_properties["headers_visible"])
        self.set_hover_expand(self.dic_properties["hover_expand"])
        self.set_hover_selection(self.dic_properties["hover_selection"])
        self.set_level_indentation(self.dic_properties["level_indentation"])
        self.set_model(self.dic_properties["model"])
        self.set_reorderable(self.dic_properties["reorderable"])
        self.set_rubber_banding(self.dic_properties["rubber_banding"])
        self.set_search_column(self.dic_properties["search_column"])
        self.set_show_expanders(self.dic_properties["show_expanders"])
        self.set_tooltip_column(self.dic_properties["tooltip_column"])
