"""The pytkwrap GTK3IconView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3IconView(Gtk.IconView, GTK3Container):
    """Wrapper for version 3.0 Gtk.IconView."""

    _GTK3_ICONVIEW_PROPERTIES = GTK3WidgetProperties(
        activate_on_single_click=False,
        cell_area=None,
        column_spacing=6,
        columns=-1,
        item_orientation=Gtk.Orientation.VERTICAL,
        item_padding=6,
        item_width=-1,
        markup_column=-1,
        model=None,
        pixbuf_column=-1,
        reorderable=False,
        row_spacing=6,
        selection_mode=Gtk.SelectionMode.SINGLE,
        spacing=0,
        text_column=-1,
        tooltip_column=-1,
    )
    _GTK3_ICONVIEW_SIGNALS = [
        "activate-cursor-item",
        "item-activated",
        "move-cursor",
        "select-all",
        "select-cursor-item",
        "selection-changed",
        "toggle-cursor-item",
        "unselect-all",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3IconView."""
        Gtk.IconView.__init__(self)
        GTK3Container.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ICONVIEW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_ICONVIEW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3IconView-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3IconView.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_activate_on_single_click(
            self.dic_properties["activate_on_single_click"]
        )
        self.set_column_spacing(self.dic_properties["column_spacing"])
        self.set_columns(self.dic_properties["columns"])
        self.set_item_orientation(self.dic_properties["item_orientation"])
        self.set_item_padding(self.dic_properties["item_padding"])
        self.set_item_width(self.dic_properties["item_width"])
        self.set_markup_column(self.dic_properties["markup_column"])
        self.set_model(self.dic_properties["model"])
        self.set_pixbuf_column(self.dic_properties["pixbuf_column"])
        self.set_reorderable(self.dic_properties["reorderable"])
        self.set_row_spacing(self.dic_properties["row_spacing"])
        self.set_selection_mode(self.dic_properties["selection_mode"])
        self.set_spacing(self.dic_properties["spacing"])
        self.set_text_column(self.dic_properties["text_column"])
        self.set_tooltip_column(self.dic_properties["tooltip_column"])
