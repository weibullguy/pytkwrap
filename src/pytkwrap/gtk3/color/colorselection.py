"""The pytkwrap GTK3ColorSelection module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ColorSelection(Gtk.ColorSelection, GTK3Box):
    """Wrapper for version 3.0 Gtk.ColorSelection."""

    _GTK3_COLORSELECTION_PROPERTIES = GTK3WidgetProperties(
        current_alpha=65535,
        current_rgba=None,
        has_opacity_control=False,
        has_palette=False,
    )
    _GTK3_COLORSELECTION_SIGNALS = ["color-changed"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorSelection."""
        Gtk.ColorSelection.__init__(self)
        GTK3Box.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_COLORSELECTION_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_COLORSELECTION_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ColorSelection-specific properties.

        Note
        ----
        has_opacity_control must be set to set the alpha channel either through
        current_alpha or current_rgba.  If has_opacity_control is False, then the
        alpha will always be 65535 (100% opaque).

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ColorSelection.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["has_opacity_control"]:
            self.set_has_opacity_control(self.dic_properties["has_opacity_control"])
            self.set_current_alpha(self.dic_properties["current_alpha"])

        if self.dic_properties["current_rgba"] is not None:
            self.set_current_rgba(self.dic_properties["current_rgba"])

        self.set_has_palette(self.dic_properties["has_palette"])
