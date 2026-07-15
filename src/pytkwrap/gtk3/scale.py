"""The pytkwrap GTK3Scale module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.range import GTK3Range


class GTK3Scale(Gtk.Scale, GTK3Range):
    """Wrapper for version 3.0 Gtk.Scale."""

    _GTK3_SCALE_PROPERTIES = GTK3WidgetProperties(
        digits=1, draw_value=True, has_origin=True, value_pos=Gtk.PositionType.TOP
    )
    _GTK3_SCALE_SIGNALS = [
        "format-value",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Scale."""
        Gtk.Scale.__init__(self)
        GTK3Range.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SCALE_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SCALE_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Scale-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Scale.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_digits(self.dic_properties["digits"])
        self.set_draw_value(self.dic_properties["draw_value"])
        self.set_has_origin(self.dic_properties["has_origin"])
        self.set_value_pos(self.dic_properties["value_pos"])
