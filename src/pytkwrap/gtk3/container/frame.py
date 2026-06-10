"""The pytkwrap GTK3Frame module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Frame(Gtk.Frame, GTK3Bin):
    """Wrapper for version 3.0 Gtk.Frame."""

    _GTK3_FRAME_PROPERTIES = GTK3WidgetProperties(
        label=None,
        label_widget=None,
        label_xalign=0.0,
        label_yalign=0.5,
        shadow_type=Gtk.ShadowType.ETCHED_IN,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Frame."""
        Gtk.Frame.__init__(self)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_FRAME_PROPERTIES)

    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None:
        """Set the values of the GTK3Frame-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Frame.
        """
        super().do_set_properties(properties)

        if self.dic_properties["label_widget"] is not None:
            self.set_label_widget(self.dic_properties["label_widget"])
        if self.dic_properties["label"] is not None:
            self.set_label(self.dic_properties["label"])

        self.set_label_align(
            self.dic_properties["label_xalign"],
            self.dic_properties["label_yalign"],
        )
        self.set_shadow_type(self.dic_properties["shadow_type"])
