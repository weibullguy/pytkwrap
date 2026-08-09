"""The pytkwrap GTK3CellRendererPixbuf module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRendererMixin


class GTK3CellRendererPixbufMixin(GTK3CellRendererMixin):
    """Mixin class for GTK3CellRendererPixbuf."""

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

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CellRendererPixbuf mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
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
        super().do_set_properties(properties)

        if self.dic_properties["gicon"] is not None:
            self.dic_properties["icon_name"] = self.dic_properties["gicon"].to_string()
            self.set_property("gicon", self.dic_properties["gicon"])
        elif self.dic_properties["icon_name"] is not None:
            self.set_property("icon_name", self.dic_properties["icon_name"])
        elif self.dic_properties["pixbuf"] is not None:
            self.set_property("pixbuf", self.dic_properties["pixbuf"])
        elif self.dic_properties["surface"] is not None:
            self.set_property("surface", self.dic_properties["surface"])

        for _property in [
            "pixbuf_expander_closed",
            "pixbuf_expander_open",
            "stock_detail",
            "stock_size",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )


class GTK3CellRendererPixbuf(Gtk.CellRendererPixbuf, GTK3CellRendererPixbufMixin):
    """Wrapper for version 3.0 Gtk.CellRendererPixbuf."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererPixbuf."""
        Gtk.CellRendererPixbuf.__init__(self)
        GTK3CellRendererPixbufMixin.__init__(self)
