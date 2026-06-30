"""The pytkwrap GTK3Menu module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.menu.menushell import GTK3MenuShell
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Menu(Gtk.Menu, GTK3MenuShell):
    """Wrapper for version 3.0 Gtk.Menu."""

    _GTK3_MENU_PROPERTIES = GTK3WidgetProperties(
        accel_group=None,
        accel_path=None,
        active=-1,
        anchor_hints=(
            Gdk.AnchorHints.FLIP_X
            | Gdk.AnchorHints.FLIP_Y
            | Gdk.AnchorHints.SLIDE_X
            | Gdk.AnchorHints.SLIDE_Y
            | Gdk.AnchorHints.RESIZE_X
            | Gdk.AnchorHints.RESIZE_Y
            | Gdk.AnchorHints.FLIP  # pylint: disable=no-member
            | Gdk.AnchorHints.SLIDE  # pylint: disable=no-member
            | Gdk.AnchorHints.RESIZE  # pylint: disable=no-member
        ),
        attach_widget=None,
        menu_type_hint=Gdk.WindowTypeHint.POPUP_MENU,
        monitor=-1,
        rect_anchor_dx=0,
        rect_anchor_dy=0,
        reserve_toggle_size=True,
    )
    _GTK3_MENU_SIGNALS = [
        "move-scroll",
        "popped-up",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Menu."""
        Gtk.Menu.__init__(self)
        GTK3MenuShell.__init__(self)

        self.dic_handler_id.update({_signal: -1 for _signal in self._GTK3_MENU_SIGNALS})
        self.dic_properties.update(self._GTK3_MENU_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Menu-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Menu.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_accel_group(self.dic_properties["accel_group"])
        self.set_accel_path(self.dic_properties["accel_path"])

        if self.dic_properties["active"] >= 0:
            self.set_active(self.dic_properties["active"])

        self.set_monitor(self.dic_properties["monitor"])
        self.set_reserve_toggle_size(self.dic_properties["reserve_toggle_size"])

        for _property in [
            "anchor_hints",
            "attach_widget",
            "menu_type_hint",
            "rect_anchor_dx",
            "rect_anchor_dy",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
