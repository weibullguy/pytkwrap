"""The pytkwrap GTK3 CellRenderer module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3CellRenderer(Gtk.CellRenderer, GTK3GObjectMixin):
    """Wrapper for Gtk.CellRenderert."""

    _GTK3_CELLRENDERER_PROPERTIES = GTK3WidgetProperties(
        cell_background=None,
        cell_background_rgba=None,
        cell_background_set=False,
        height=-1,
        is_expanded=False,
        is_expander=False,
        mode=Gtk.CellRendererMode.INERT,
        sensitive=True,
        visible=True,
        width=-1,
        xalign=0.0,
        xpad=0,
        yalign=0.0,
        ypad=0,
    )
    _GTK3_CELLRENDERER_SIGNALS = [
        "editing-canceled",
        "editing-started",
    ]

    def __init__(self) -> None:
        Gtk.CellRenderer.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERER_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CELLRENDERER_SIGNALS}
        )

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
        if property_name in self._GTK3_CELLRENDERER_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3CellRenderer.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict, preferred, non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3Adjustment.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        self.set_alignment(self.dic_properties["xalign"], self.dic_properties["yalign"])
        self.set_fixed_size(self.dic_properties["width"], self.dic_properties["height"])
        self.set_padding(self.dic_properties["xpad"], self.dic_properties["ypad"])
        self.set_sensitive(self.dic_properties["sensitive"])
        self.set_visible(self.dic_properties["visible"])

        for _property in [
            "cell_background",
            "cell_background_rgba",
            "is_expanded",
            "is_expander",
            "mode",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
