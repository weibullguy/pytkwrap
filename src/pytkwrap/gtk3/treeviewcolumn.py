"""The pytkwrap GTK3 TreeViewColumn module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.cellrenderer import GTK3CellRenderer
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3TreeViewColumn(Gtk.TreeViewColumn, GTK3GObjectMixin):
    """Wrapper for Gtk.TreeViewColumnt."""

    _GTK3_TREEVIEWCOLUMN_PROPERTIES = GTK3WidgetProperties(
        alignment=0.0,
        cell_area=None,
        clickable=False,
        expand=False,
        fixed_width=-1,
        max_width=-1,
        min_width=-1,
        reorderable=False,
        resizable=False,
        sizing=Gtk.TreeViewColumnSizing.GROW_ONLY,
        sort_column_id=-1,
        sort_indicator=False,
        sort_order=Gtk.SortType.ASCENDING,
        spacing=0,
        title="",
        visible=True,
        widget=None,
        width=0,
        x_offset=0,
    )
    _GTK3_TREEVIEWCOLUMN_SIGNALS = [
        "clicked",
    ]

    def __init__(
        self,
        title: str = "",
        cell_renderer: GTK3CellRenderer | None = None,
        cell_area: Gtk.CellArea | None = None,
    ) -> None:
        Gtk.TreeViewColumn.__init__(self, title, cell_renderer)
        GTK3GObjectMixin.__init__(self)

        self.dic_properties.update(self._GTK3_TREEVIEWCOLUMN_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TREEVIEWCOLUMN_SIGNALS}
        )

        self.dic_properties["cell_area"] = cell_area
        self.dic_properties["title"] = title

    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
        """
        if property_name in self._GTK3_TREEVIEWCOLUMN_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3TreeViewColumn.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict, preferred, non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3Adjustment.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        self.set_alignment(self.dic_properties["alignment"])
        self.set_clickable(self.dic_properties["clickable"])
        self.set_expand(self.dic_properties["expand"])
        self.set_fixed_width(self.dic_properties["fixed_width"])
        self.set_max_width(self.dic_properties["max_width"])
        self.set_min_width(self.dic_properties["min_width"])
        self.set_reorderable(self.dic_properties["reorderable"])
        self.set_resizable(self.dic_properties["resizable"])
        self.set_sizing(self.dic_properties["sizing"])
        self.set_sort_column_id(self.dic_properties["sort_column_id"])
        self.set_sort_indicator(self.dic_properties["sort_indicator"])
        self.set_sort_order(self.dic_properties["sort_order"])
        self.set_spacing(self.dic_properties["spacing"])
        self.set_title(self.dic_properties["title"])
        self.set_visible(self.dic_properties["visible"])
        self.set_widget(self.dic_properties["widget"])
