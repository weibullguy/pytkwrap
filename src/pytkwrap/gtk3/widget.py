"""The pytkwrap GTK3 Widget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import (
    GTK3GObjectMixin,
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
)


class GTK3Widget(Gtk.Widget, GTK3GObjectMixin):
    """Adds GTK3-specific widget attributes."""

    _DEFAULT_HEIGHT = -1
    _DEFAULT_WIDTH = -1
    _GTK3_WIDGET_ATTRIBUTES = GTK3WidgetAttributes(
        x_pos=0,
        y_pos=0,
    )
    _GTK3_WIDGET_PROPERTIES = GTK3WidgetProperties(
        app_paintable=False,
        can_default=False,
        can_focus=False,
        composite_child=False,
        events=Gdk.EventMask.ALL_EVENTS_MASK,  # pylint: disable=no-member
        expand=False,
        focus_on_click=True,
        halign=Gtk.Align.FILL,
        has_default=False,
        has_focus=False,
        has_tooltip=False,
        height_request=-1,
        hexpand=False,
        hexpand_set=False,
        is_focus=False,
        margin=0,
        margin_bottom=0,
        margin_end=0,
        margin_start=0,
        margin_top=0,
        name="pytkwrap GTK3 widget",
        no_show_all=False,
        opacity=1.0,
        parent=None,
        receives_default=False,
        scale_factor=1,
        sensitive=True,
        style=None,
        tooltip_markup="Missing tooltip, please file an issue to have one added.",
        tooltip_text="Missing tooltip, please file an issue to have one added.",
        valign=Gtk.Align.FILL,
        vexpand=False,
        vexpand_set=False,
        visible=False,
        width_request=-1,
        window=None,
    )
    _GTK3_WIDGET_SIGNALS = [
        "destroy",
        "direction-changed",
        "hide",
        "keynav-failed",
        "map",
        "mnemonic-activate",
        "move-focus",
        "query-tooltip",
        "realize",
        "show",
        "state-flags-changed",
        "unmap",
        "unrealize",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3WidgetMixin."""
        Gtk.Widget.__init__(self)
        GTK3GObjectMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_WIDGET_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_WIDGET_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_WIDGET_PROPERTIES)
        self.dic_properties["tooltip_markup"] = self._DEFAULT_TOOLTIP
        self.dic_properties["tooltip_text"] = self._DEFAULT_TOOLTIP

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
        if property_name in self._GTK3_WIDGET_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | list[list | tuple]
            The typed dict (preferred) or list of lists or list of tuples with the
            property values to set for the GTK3Widget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["height_request"] == 0:
            self.dic_properties["height_request"] = self._DEFAULT_HEIGHT

        if self.dic_properties["width_request"] == 0:
            self.dic_properties["width_request"] = self._DEFAULT_WIDTH

        # We want the tooltip markup and the tooltip text to be the same value.
        if (
            self.dic_properties["tooltip_markup"] == self._DEFAULT_TOOLTIP
            and self.dic_properties["tooltip_text"] != self._DEFAULT_TOOLTIP
        ):
            self.dic_properties["tooltip_markup"] = self.dic_properties["tooltip_text"]

        if (
            self.dic_properties["tooltip_text"] == self._DEFAULT_TOOLTIP
            and self.dic_properties["tooltip_markup"] != self._DEFAULT_TOOLTIP
        ):
            self.dic_properties["tooltip_text"] = self.dic_properties["tooltip_markup"]

        # Set the value of each of the mixin properties.
        self.set_can_default(self.dic_properties["can_default"])
        self.set_can_focus(self.dic_properties["can_focus"])
        self.set_halign(self.dic_properties["halign"])  # type: ignore[arg-type]
        self.set_has_tooltip(self.dic_properties["has_tooltip"])
        self.set_hexpand(self.dic_properties["hexpand"])
        self.set_hexpand_set(self.dic_properties["hexpand_set"])
        self.set_margin_bottom(self.dic_properties["margin_bottom"])
        self.set_margin_end(self.dic_properties["margin_end"])
        self.set_margin_start(self.dic_properties["margin_start"])
        self.set_margin_top(self.dic_properties["margin_top"])
        self.set_name(self.dic_properties["name"])
        self.set_opacity(self.dic_properties["opacity"])
        self.set_receives_default(self.dic_properties["receives_default"])
        self.set_sensitive(self.dic_properties["sensitive"])
        self.set_size_request(
            self.dic_properties["width_request"],
            self.dic_properties["height_request"],
        )
        self.set_tooltip_markup(self.dic_properties["tooltip_markup"])
        self.set_tooltip_text(self.dic_properties["tooltip_text"])
        self.set_valign(self.dic_properties["valign"])  # type: ignore[arg-type]
        self.set_vexpand(self.dic_properties["vexpand"])
        self.set_vexpand_set(self.dic_properties["vexpand_set"])
        self.set_visible(self.dic_properties["visible"])

        for _property in ["focus_on_click", "parent"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
