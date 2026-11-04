"""The pytkwrap GTK3Widget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk, Pango
from pytkwrap.gtk3.mixins import (
    GTK3GObjectMixin,
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
)


class GTK3WidgetMixin(GTK3GObjectMixin):
    """Mixin for GTK3Widget.

    Attributes
    ----------
    _DEFAULT_HEIGHT : int
        The default height for the GTK3Widget.
    _DEFAULT_WIDTH : int
        The default width for the GTK3Widget.
    _GTK3_WIDGET_ATTRIBUTES : GTK3WidgetAttributes
        Attributes unique to the GTK3Widget.
    _GTK3_WIDGET_PROPERTIES : GTK3WidgetProperties
        Properties unique to the GTK3Widget.
    _GTK3_WIDGET_SIGNALS : list[str]
        Signals unique to the GTK3Widget.
    """

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

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3WidgetMixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_WIDGET_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_WIDGET_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_WIDGET_PROPERTIES)
        self.dic_properties["tooltip_markup"] = self._DEFAULT_TOOLTIP
        self.dic_properties["tooltip_text"] = self._DEFAULT_TOOLTIP

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Widget-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Widget.
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
        self.set_tooltip_markup(self.dic_properties["tooltip_markup"])
        self.set_tooltip_text(self.dic_properties["tooltip_text"])
        self.set_valign(self.dic_properties["valign"])  # type: ignore[arg-type]
        self.set_vexpand(self.dic_properties["vexpand"])
        self.set_vexpand_set(self.dic_properties["vexpand_set"])
        self.set_visible(self.dic_properties["visible"])

        if isinstance(self, Gtk.Widget):
            self.set_size_request(
                self.dic_properties["width_request"],
                self.dic_properties["height_request"],
            )

        self.set_property("focus-on-click", self.dic_properties["focus_on_click"])

        if self.dic_properties["parent"] is not None:
            self.set_property("parent", self.dic_properties["parent"])

    @property
    def accessible(self) -> object:
        """Get the accessible object for the widget.

        Returns
        -------
        object
            The accessible object for the widget.
        """
        return self.get_accessible()

    @property
    def allocated_baseline(self) -> int:
        """Get the allocated baseline of the widget.

        Returns
        -------
        int
            The allocated baseline of the widget.
        """
        return self.get_allocated_baseline()

    @property
    def allocated_height(self) -> int:
        """Get the allocated height of the widget.

        Returns
        -------
        int
            The allocated height of the widget.
        """
        return self.get_allocated_height()

    @property
    def allocated_width(self) -> int:
        """Get the allocated width of the widget.

        Returns
        -------
        int
            The allocated width of the widget.
        """
        return self.get_allocated_width()

    @property
    def display(self) -> Gdk.Display:
        """Get the display for the widget.

        Returns
        -------
        Gdk.Display
            The display for the widget.
        """
        return self.get_display()

    @property
    def frame_clock(self) -> Gdk.FrameClock | None:
        """Get the frame clock for the widget.

        Returns
        -------
        Gdk.FrameClock | None
            The frame clock for the widget or None if the widget is unrealized.
        """
        return self.get_frame_clock()

    @property
    def pango_context(self) -> Pango.Context:
        """Get the Pango context for the widget.

        Returns
        -------
        Pango.Context
            The Pango context for the widget.
        """
        return self.get_pango_context()

    @property
    def parent_window(self) -> Gdk.Window | None:
        """Get the parent window for the widget.

        Returns
        -------
        Gdk.Window | None
            The parent window for the widget or None if the widget has no parent window.
        """
        return self.get_parent_window()

    @property
    def preferred_height(self) -> tuple[int, int]:
        """Get the preferred height of the widget.

        Returns
        -------
        tuple[int, int]
            The minimum and natural height of the widget.
        """
        return self.get_preferred_height()

    @property
    def preferred_size(self) -> tuple[Gtk.Requisition, Gtk.Requisition]:
        """Get the preferred size of the widget.

        Returns
        -------
        tuple[Gtk.Requisition, Gtk.Requisition]
            The minimum size and natural size of the widget.
        """
        return self.get_preferred_size()

    @property
    def preferred_width(self) -> tuple[int, int]:
        """Get the preferred width of the widget.

        Returns
        -------
        tuple[int, int]
            The minimum and natural width of the widget.
        """
        return self.get_preferred_width()

    @property
    def request_mode(self) -> Gtk.SizeRequestMode:
        """Get the request mode of the widget.

        Returns
        -------
        Gtk.SizeRequestMode
            The request mode of the widget.
        """
        return self.get_request_mode()

    @property
    def scale_factor(self) -> int:
        """Get the internal scale factor for the widget.

        Returns
        -------
        int
            The scale factor for the widget.
        """
        return self.get_scale_factor()

    @property
    def screen(self) -> Gdk.Screen:
        """Get the Gdk.Screen for the toplevel for the widget.

        Returns
        -------
        Gdk.Screen
            The Gdk.Screen for the toplevel of the widget.
        """
        return self.get_screen()

    @property
    def settings(self) -> Gtk.Settings:
        """Get the Gtk.Settings holding the settings for the widget.

        Returns
        -------
        Gtk.Settings
            The settings for the widget.
        """
        return self.get_settings()

    @property
    def style_context(self) -> Gtk.StyleContext:
        """Get the style context associated with the widget.

        Returns
        -------
        Gtk.StyleContext
            The style context for the widget.
        """
        return self.get_style_context()

    @property
    def toplevel(self) -> Gtk.Widget:
        """Get the topmost ancestor of the widget or the widget itself.

        Returns
        -------
        Gtk.Widget
            The topmost ancestor of the widget or the widget itself when there is no
            ancestor.
        """
        return self.get_toplevel()

    @property
    def valign_with_baseline(self) -> Gtk.Align:
        """Get the vertical alignment of the widget.

        Returns
        -------
        Gtk.Align
            The value of the align property including Gtk.Align.BASELINE.
        """
        return self.get_valign_with_baseline()


class GTK3Widget(Gtk.Widget, GTK3WidgetMixin):
    """Wrapper for version 3.0 Gtk.Widget."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Widget."""
        Gtk.Widget.__init__(self)
        GTK3WidgetMixin.__init__(self)

        self.show_all()
