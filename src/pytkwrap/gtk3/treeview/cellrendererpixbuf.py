"""The pytkwrap GTK3CellRendererPixbuf module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer


class GTK3CellRendererPixbuf(Gtk.CellRendererPixbuf, GTK3CellRenderer):
    """Wrapper for version 3.0 Gtk.CellRendererPixbuf."""

    _GTK3_CELLRENDERERPIXBUF_PROPERTIES = GTK3WidgetProperties(
        gicon=None,
        icon_name=None,
        pixbuf=None,
        pixbuf_expander_closed=None,
        pixbuf_expander_open=None,
        stock_detail=None,
        stock_size=1,
        surface=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererPixbuf."""
        Gtk.CellRendererPixbuf.__init__(self)
        GTK3CellRenderer.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERERPIXBUF_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererPixbuf-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererPixbuf.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        for _property in [
            "gicon",
            "icon_name",
            "pixbuf",
            "pixbuf_expander_closed",
            "pixbuf_expander_open",
            "stock_detail",
            "stock_size",
            "surface",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
