#       pytkwrap.gtk3.scrolledwindow.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 ScrolledWindow module."""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.widget import GTK3BaseWidget, GTK3WidgetProperties


class GTK3ScrolledWindow(Gtk.ScrolledWindow, GTK3BaseWidget):
    """The GTK3ScrolledWindow class."""

    _GTK3_SCROLLEDWINDOW_PROPERTIES = GTK3WidgetProperties(
        border_width=0,
        hadjustment=None,
        hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
        kinetic_scrolling=True,
        max_content_height=-1,
        max_content_width=-1,
        min_content_height=-1,
        min_content_width=-1,
        overlay_scrolling=True,
        propagate_natural_height=False,
        propagate_natural_width=False,
        shadow_type=Gtk.ShadowType.NONE,
        vadjustment=None,
        vscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
        window_placement=Gtk.CornerType.TOP_LEFT,
    )
    _GTK3_SCROLLEDWINDOW_SIGNALS = [
        "edge-overshot",
        "edge-reached",
        "move-focus-out",
        "scroll-child",
    ]

    def __init__(self, child: Gtk.Widget | GTK3BaseWidget | None = None) -> None:
        """Initialize an instance of the ScrolledWindow widget.

        Parameters
        ----------
        child : Gtk.Widget or GTK3BaseWidget
            The widget to add to the GTK3ScrolledWindow.
        """
        Gtk.ScrolledWindow.__init__(self)
        GTK3BaseWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_SCROLLEDWINDOW_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_SCROLLEDWINDOW_SIGNALS
        })

        if child is not None:
            self.add(child)  # type: ignore[attr-defined]

    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3ScrolledWindow widget.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3ScrolledWindow.
        """
        super().do_set_properties(properties)

        self.set_hadjustment(self.dic_properties["hadjustment"])
        self.set_kinetic_scrolling(self.dic_properties["kinetic_scrolling"])
        self.set_max_content_height(self.dic_properties["max_content_height"])
        self.set_max_content_width(self.dic_properties["max_content_width"])
        self.set_min_content_height(self.dic_properties["min_content_height"])
        self.set_min_content_width(self.dic_properties["min_content_width"])
        self.set_overlay_scrolling(self.dic_properties["overlay_scrolling"])
        self.set_placement(self.dic_properties["window_placement"])
        self.set_policy(
            self.dic_properties["hscrollbar_policy"],
            self.dic_properties["vscrollbar_policy"],
        )
        self.set_propagate_natural_height(
            self.dic_properties["propagate_natural_height"]
        )
        self.set_propagate_natural_width(self.dic_properties["propagate_natural_width"])
        self.set_shadow_type(self.dic_properties["shadow_type"])
        self.set_vadjustment(self.dic_properties["vadjustment"])
