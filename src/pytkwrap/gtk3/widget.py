#       pytkwrap.gtk3.widget.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 BaseWidget module."""

# Future Imports
from __future__ import annotations

# Standard Library Imports
from abc import abstractmethod
from datetime import date
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    # Standard Library Imports
    from types import FunctionType

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.common import WidgetMixin
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, GLib, Gtk, Pango, _
from pytkwrap.gtk3.mixins import GTK3DataWidgetMixin
from pytkwrap.utilities import none_to_default


class GTK3WidgetProperties(TypedDict, total=False):
    """Type for GTK3 widget properties."""

    accepts_tab: bool
    action: Gtk.FileChooserAction | None
    action_name: str | None
    action_target: GLib.Variant | None
    activates_default: bool
    active: bool | int
    active_id: str | None
    activatable: bool
    adjustment: Gtk.Adjustment | None
    alignment: Pango.Alignment | None
    alpha: int
    always_show_image: bool
    angle: float
    app_paintable: bool
    attributes: Pango.AttrList | None
    background: str
    background_rgba: Gdk.RGBA | None
    baseline_row: int
    bold: bool
    border_width: int
    bottom_margin: int
    buffer: Gtk.TextBuffer | None
    button_sensitivity: Gtk.SensitivityType | None
    can_default: bool
    can_focus: bool
    caps_lock_warning: bool
    cell_area: Gtk.CellArea | None
    cell_background_rgba: Gdk.RGBA | None
    cell_foreground_rgba: Gdk.RGBA | None
    climb_rate: float
    column_homogeneous: bool
    column_spacing: int
    column_span_column: int
    completion: Gtk.EntryCompletion | None
    composite_child: bool
    create_folders: bool
    cursor_position: int
    cursor_visible: bool
    destroy_with_parent: bool
    dialog: Gtk.Dialog | None
    digits: int
    do_overwrite_confirmation: bool
    draw_indicator: bool
    editable: bool
    editing_canceled: bool
    ellipsize: Pango.EllipsizeMode | None
    enable_emoji_completion: bool
    enable_grid_lines: Gtk.TreeViewGridLines | None
    enable_tree_lines: bool
    entry_text_column: int
    events: Gdk.EventMask | None
    expand: bool
    extra_widget: Gtk.Widget | None
    filter: Gtk.FileFilter | None
    focus_on_click: bool
    foreground: str
    foreground_rgba: Gdk.RGBA | None
    group: Gtk.RadioButton | None
    hadjustment: Gtk.Adjustment | None
    halign: Gtk.Align | None
    has_default: bool
    has_entry: bool
    has_focus: bool
    has_frame: bool
    has_tooltip: bool
    height_request: int
    hexpand: bool
    hexpand_set: bool
    horizontal_alignment: str
    hscroll_policy: Gtk.ScrollablePolicy | None
    hscrollbar_policy: Gtk.PolicyType | None
    icon: str
    id_column: int
    image: Gtk.Widget | None
    image_position: Gtk.PositionType
    im_module: str | None
    inconsistent: bool
    indent: int
    inner_border: Gtk.Border | None
    input_hints: Gtk.InputHints | None
    input_purpose: Gtk.InputPurpose | None
    invisible_char: str
    invisible_char_set: bool
    is_focus: bool
    justification: Gtk.Justification | None
    justify: Gtk.Justification | None
    kinetic_scrolling: bool
    label: str | None
    label_widget: Gtk.Widget | None
    label_xalign: float
    label_yalign: float
    left_margin: int
    level_indentation: int
    lines: int
    local_only: bool
    lower: float
    margin: int
    margin_bottom: int
    margin_end: int
    margin_start: int
    margin_top: int
    max_content_height: int
    max_content_width: int
    max_length: int
    max_width_chars: int
    min_content_height: int
    min_content_width: int
    mnemonic_widget: Gtk.Widget | None
    modal: bool
    model: Gtk.TreeModel | None
    monospace: bool
    name: str
    no_show_all: bool
    numeric: bool
    opacity: float
    overlay_scrolling: bool
    overwrite: bool
    overwrite_mode: bool
    page_increment: float
    page_size: float
    parent: Gtk.Container | None
    pattern: str | None
    pixels_above_lines: int
    pixels_below_lines: int
    pixels_inside_wrap: int
    placeholder_text: str | None
    populate_all: bool
    popup_fixed_width: bool
    popup_shown: bool
    preview_widget: Gtk.Widget | None
    preview_widget_active: bool
    primary_icon_activatable: bool
    primary_icon_gicon: Gio.Icon | None
    primary_icon_name: str | None
    primary_icon_pixbuf: GdkPixbuf.Pixbuf | None
    primary_icon_sensitive: bool
    primary_icon_storage_type: Gtk.ImageType | None
    primary_icon_tooltip_markup: str | None
    primary_icon_tooltip_text: str | None
    progress_fraction: float
    progress_pulse_step: float
    propagate_natural_height: bool
    propagate_natural_width: bool
    receives_default: bool
    relief: Gtk.ReliefStyle.NORMAL
    rgba: Gdk.RGBA | None
    right_margin: int
    rotation: float
    row_homogeneous: bool
    row_spacing: int
    row_span_column: int
    rubber_banding: bool
    scale_factor: int
    scroll_offset: int
    secondary_icon_activatable: bool
    secondary_icon_gicon: Gio.Icon | None
    secondary_icon_name: str | None
    secondary_icon_pixbuf: GdkPixbuf.Pixbuf | None
    secondary_icon_sensitive: bool
    secondary_icon_storage_type: Gtk.ImageType | None
    secondary_icon_tooltip_markup: str | None
    secondary_icon_tooltip_text: str | None
    selectable: bool
    select_multiple: bool
    selection_bound: int
    sensitive: bool
    shadow_type: Gtk.ShadowType | None
    show_editor: bool
    show_emoji_icon: bool
    show_hidden: bool
    single_line_mode: bool
    snap: bool | None
    snap_to_ticks: bool
    step_increment: float
    tabs: Pango.TabArray | None
    text: str
    text_column: int
    text_length: int
    title: str
    tooltip: str
    tooltip_column: int
    tooltip_markup: str
    tooltip_text: str
    top_margin: int
    track_visited_links: bool
    truncate_multiline: bool
    upper: float
    use_alpha: bool
    use_markup: bool
    use_preview_label: bool
    use_underline: bool
    vadjustment: Gtk.Adjustment | None
    valign: Gtk.Align | None
    vertical_alignment: str
    vexpand: bool
    vexpand_set: bool
    visible: bool
    visibility: bool
    vscroll_policy: Gtk.ScrollablePolicy | None
    vscrollbar_policy: Gtk.PolicyType | None
    weight: int
    weight_set: bool
    width_chars: int
    width_request: int
    window: Gdk.Window | None
    window_placement: Gtk.CornerType | None
    wrap: bool
    wrap_mode: Gtk.WrapMode | None
    wrap_width: int
    xalign: float
    yalign: float


class GTK3BaseWidget(Gtk.Widget, WidgetMixin):
    """Base for ALL GTK3 widgets - structural and data."""

    # Define private class attributes.
    _GTK3_BASE_PROPERTIES = GTK3WidgetProperties(
        app_paintable=True,
        can_default=True,
        can_focus=True,
        events=Gdk.EventMask.ALL_EVENTS_MASK,
        expand=True,
        focus_on_click=True,
        halign=Gtk.Align.FILL,
        has_default=False,
        has_focus=False,
        has_tooltip=True,
        height_request=-1,
        hexpand=True,
        hexpand_set=True,
        is_focus=False,
        margin=0,
        margin_bottom=0,
        margin_end=0,
        margin_start=0,
        margin_top=0,
        name="pytkwrap widget",
        no_show_all=False,
        opacity=1.0,
        parent=None,
        receives_default=False,
        sensitive=True,
        tooltip_markup=_("Missing tooltip, please file an issue to have one added."),
        tooltip_text=_("Missing tooltip, please file an issue to have one added."),
        valign=Gtk.Align.BASELINE,
        vexpand=True,
        vexpand_set=True,
        visible=True,
        width_request=-1,
    )
    _GTK3_BASE_SIGNALS: list[str] = [
        "accel-closures-changed",
        "button-press-event",
        "button-release-event",
        "can-activate-accel",
        "child-notify",
        "configure-event",
        "damage-event",
        "delete-event",
        "destroy",
        "destroy-event",
        "direction-changed",
        "drag-begin",
        "drag-data-delete",
        "drag-data-get",
        "drag-data-received",
        "drag-drop",
        "drag-end",
        "drag-failed",
        "drag-leave",
        "drag-motion",
        "draw",
        "enter-notify-event",
        "event",
        "event-after",
        "focus",
        "focus-in-event",
        "focus-out-event",
        "grab-broken-event",
        "grab-focus",
        "grab-notify",
        "hide",
        "hierarchy-changed",
        "key-press-event",
        "key-release-event",
        "keynav-failed",
        "leave-notify-event",
        "map",
        "map-event",
        "mnemonic-activate",
        "motion-notify-event",
        "move-focus",
        "notify",
        "parent-set",
        "popup-menu",
        "property-notify-event",
        "proximity-in-event",
        "proximity-out-event",
        "query-tooltip",
        "realize",
        "screen-changed",
        "scroll-event",
        "selection-clear-event",
        "selection-get",
        "selection-notify-event",
        "selection-received",
        "selection-request-event",
        "show",
        "show-help",
        "size-allocate",
        "state-flags-changed",
        "style-updated",
        "touch-event",
        "unmap",
        "unmap-event",
        "unrealize",
        "visibility-notify-event",
        "window-state-event",
    ]
    _DEFAULT_HEIGHT: int = -1
    _DEFAULT_WIDTH: int = -1

    def __init__(self) -> None:
        """Initialize an instance of the GTK3BaseWidget."""
        Gtk.Widget.__init__(self)
        WidgetMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id: dict[str, int] = {
            _signal: -1 for _signal in self._GTK3_BASE_SIGNALS
        }
        self.dic_properties = dict(self._GTK3_BASE_PROPERTIES)

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_callbacks(self, signal: str, callback: FunctionType) -> None:
        """Set the callback method for the GTK3BaseWidget.

        Parameters
        ----------
        signal : str
            The name of the signal to connect the callback to.
        callback : FunctionType
            The callback function or method to connect to the signal.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for this widget.
        """
        try:
            # RAMSTKTextViews need to connect their Gtk.TextBuffer to the callback.
            if (
                "buffer" in self.dic_properties
                and self.dic_properties["buffer"] is not None
            ):
                self.dic_handler_id[signal] = self.dic_properties["buffer"].connect(
                    signal,
                    callback,
                )
            else:
                self.dic_handler_id[signal] = self.connect(
                    signal,
                    callback,
                )
        except TypeError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.do_set_callbacks()",
                signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3BaseWidget.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3BaseWidget.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        if self.dic_properties["height_request"] == 0:
            self.dic_properties["height_request"] = self._DEFAULT_HEIGHT
        if self.dic_properties["width_request"] == 0:
            self.dic_properties["width_request"] = self._DEFAULT_WIDTH

        # Set the value of each of the widget properties.
        self.set_app_paintable(self.dic_properties["app_paintable"])  # type: ignore[attr-defined]
        self.set_can_default(self.dic_properties["can_default"])  # type: ignore[attr-defined]
        self.set_can_focus(self.dic_properties["can_focus"])
        self.set_focus_on_click(self.dic_properties["focus_on_click"])
        self.set_halign(self.dic_properties["halign"])  # type: ignore[arg-type]
        self.set_has_tooltip(self.dic_properties["has_tooltip"])
        self.set_hexpand(self.dic_properties["hexpand"])
        self.set_hexpand_set(self.dic_properties["hexpand_set"])
        self.set_margin_bottom(self.dic_properties["margin_bottom"])
        self.set_margin_end(self.dic_properties["margin_end"])
        self.set_margin_start(self.dic_properties["margin_start"])
        self.set_margin_top(self.dic_properties["margin_top"])
        self.set_name(self.dic_properties["name"])
        self.set_no_show_all(self.dic_properties["no_show_all"])  # type: ignore[attr-defined]
        self.set_opacity(self.dic_properties["opacity"])
        self.set_receives_default(self.dic_properties["receives_default"])
        self.set_sensitive(self.dic_properties["sensitive"])
        self.set_size_request(
            self.dic_properties["width_request"],
            self.dic_properties["height_request"],
        )
        # TODO: Change this so that if either the tooltip_markup or tooltip_text
        #  properties are not the default value, both will be set to the non-default
        #  value.
        self.set_tooltip_markup(self.dic_properties["tooltip_markup"])
        self.set_tooltip_text(self.dic_properties["tooltip_text"])
        self.set_valign(self.dic_properties["valign"])  # type: ignore[arg-type]
        self.set_vexpand(self.dic_properties["vexpand"])
        self.set_vexpand_set(self.dic_properties["vexpand_set"])
        self.set_visible(self.dic_properties["visible"])


class GTK3BaseDataWidget(GTK3BaseWidget, GTK3DataWidgetMixin):
    """Base for GTK3 widgets that display and/or manipulate data."""

    def __init__(self):
        """Initialize and instance of the GTK3BaseDataWidget."""
        GTK3BaseWidget.__init__(self)
        GTK3DataWidgetMixin.__init__(self)

    @abstractmethod
    def do_get_value(self) -> None:
        """Return the current value of the widget."""
        raise NotImplementedError

    @abstractmethod
    def do_set_value(self, value) -> None:
        """Set the current value of the widget."""
        raise NotImplementedError

    def do_update(
        self,
        package: dict[str, bool | date | float | int | str | None],
    ) -> None:
        """Update the widget with a new value.

        Parameters
        ----------
        package : dict
            The data package to use to update the widget.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for the widget.
        """
        _field, _value = next(iter(package.items()))
        _value = none_to_default(_value, self.default)

        if _field != self.field:
            return

        try:
            _hid = self.dic_handler_id[self.edit_signal]
            with self.handler_block(_hid):
                self.do_set_value(_value)
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.do_update()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def on_changed(self, __widget: GTK3BaseWidget) -> None:
        """Retrieve the data package for the widget on value changes.

        This method also sends a PyPubSub message along with the data package for
        listeners to update with the new value.

        Parameters
        ----------
        __widget : GTK3BaseWidget
            The widget that was changed. Unused but required to satisfy the Gtk.Widget()
            callback method structure.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for this widget.
        """
        _package = {self.field: self.do_get_value()}
        try:
            _hid = self.dic_handler_id[self.edit_signal]
            with self.handler_block(_hid):
                pub.sendMessage(
                    self.send_topic,
                    node_id=self.record_id,
                    package=_package,
                )
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.on_changed()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc
