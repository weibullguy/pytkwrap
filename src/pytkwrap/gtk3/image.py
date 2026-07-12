"""The pytkwrap GTKImage module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3Image(Gtk.Image, GTK3Widget):
    """Wrapper for version 3.0 Gtk.Image."""

    _GTK3_IMAGE_PROPERTIES = GTK3WidgetProperties(
        file=None,
        gicon=None,
        icon_name=None,
        icon_size=4,
        pixbuf=None,
        pixbuf_animation=None,
        pixel_size=-1,
        resource=None,
        surface=None,
        use_fallback=False,
    )

    def __init__(
        self,
        size: int = 4,
    ) -> None:
        """Initialize an instance of the GTK3Image."""
        Gtk.Image.__init__(self)
        GTK3Widget.__init__(self)

        self.dic_properties.update(self._GTK3_IMAGE_PROPERTIES)
        self.size = size

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Image-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Image.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["gicon"] is not None:
            self.set_from_gicon(self.dic_properties["gicon"], self.size)
        elif self.dic_properties["icon_name"] is not None:
            self.set_from_icon_name(self.dic_properties["icon_name"], self.size)
        elif self.dic_properties["pixbuf"] is not None:
            self.set_from_pixbuf(self.dic_properties["pixbuf"])
        elif self.dic_properties["pixbuf_animation"] is not None:
            self.set_from_animation(self.dic_properties["pixbuf_animation"])
        elif self.dic_properties["resource"] is not None:
            self.set_from_resource(self.dic_properties["resource"])
        elif self.dic_properties["surface"] is not None:
            self.set_from_surface(self.dic_properties["surface"])
        elif self.dic_properties["file"] is not None:
            self.set_from_file(self.dic_properties["file"])

        self.set_pixel_size(self.dic_properties["pixel_size"])

        for _property in ["icon_size", "use_fallback"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
