#       pytkwrap.gtk3.frame.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 Frame module."""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.widget import GTK3BaseWidget, GTK3WidgetProperties


class GTK3Frame(Gtk.Frame, GTK3BaseWidget):
    """The GTK3Frame class."""

    _GTK3_FRAME_PROPERTIES = GTK3WidgetProperties(
        border_width=0,
        label="",
        label_widget=None,
        label_xalign=0.0,
        label_yalign=0.5,
        shadow_type=Gtk.ShadowType.ETCHED_IN,
    )
    _GTK3_FRAME_SIGNALS = [
        "add",
        "set-focus-child",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Frame widget."""
        Gtk.Frame.__init__(self)
        GTK3BaseWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_FRAME_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_FRAME_SIGNALS
        })

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3Frame.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            THe typed dict with the property values to set for the GTK3Frame.
        """
        super().do_set_properties(properties)

        if self.dic_properties["label_widget"] is not None:
            self.set_label_widget(self.dic_properties["label_widget"])
        self.set_label(self.dic_properties["label"])
        self.set_label_align(
            self.dic_properties["label_xalign"],
            self.dic_properties["label_yalign"],
        )
        self.set_shadow_type(self.dic_properties["shadow_type"])
