"""The pytkwrap GTK3 mixins module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from types import EllipsisType, FunctionType
from typing import TypedDict

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.common import ToolkitMixin
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, GLib, GObject, Gtk, Pango


class GTK3WidgetAttributes(TypedDict, total=False):
    """Type for GTK3 widget attributes."""

    column_types: list[EllipsisType] | list[GObject.GType] | None


class GTK3WidgetProperties(TypedDict, total=False):
    """Type for GTK3 widget properties."""

    accepts_tab: bool
    action: Gtk.FileChooserAction | None
    action_name: str | None
    action_target: GLib.Variant | None
    activates_default: bool
    active: bool | int  # datawidget property
    active_id: str | None
    activatable: bool
    adjustment: Gtk.Adjustment | None  # datawidget property
    alignment: Pango.Alignment | None  # datawidget property
    alpha: int
    always_show_image: bool
    angle: float
    app_paintable: bool
    attributes: Pango.AttrList | None  # datawidget property
    background: str
    background_rgba: Gdk.RGBA | None
    baseline_row: int
    bold: bool  # datawidget property
    border_width: int
    bottom_margin: int
    buffer: Gtk.EntryBuffer | Gtk.TextBuffer | None  # datawidget property
    button_sensitivity: Gtk.SensitivityType | None
    can_default: bool
    can_focus: bool
    can_target: bool
    caps_lock_warning: bool  # datawidget property
    cell_area: Gtk.CellArea | None
    cell_background: str | None
    cell_background_rgba: Gdk.RGBA | None
    cell_background_set: bool
    cell_foreground_rgba: Gdk.RGBA | None
    climb_rate: float  # datawidget property
    column_homogeneous: bool
    column_spacing: int
    column_span_column: int
    completion: Gtk.EntryCompletion | None  # datawidget property
    composite_child: bool
    create_folders: bool
    cursor_position: int
    cursor_visible: bool
    destroy_with_parent: bool
    dialog: Gtk.Dialog | None
    digits: int  # datawidget property
    do_overwrite_confirmation: bool  # datawidget property
    draw_indicator: bool
    editable: bool  # datawidget property
    editing_canceled: bool  # datawidget property
    ellipsize: Pango.EllipsizeMode | None  # datawidget property
    enable_emoji_completion: bool
    enable_grid_lines: Gtk.TreeViewGridLines | None
    enable_tree_lines: bool
    entry_text_column: int  # datawidget property
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
    has_entry: bool  # datawidget property
    has_focus: bool
    has_frame: bool
    has_tooltip: bool
    height: int
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
    indent: int  # datawidget property
    inner_border: Gtk.Border | None
    input_hints: Gtk.InputHints | None
    input_purpose: Gtk.InputPurpose | None
    invisible_char: str  # datawidget property
    invisible_char_set: bool  # datawidget property
    is_expanded: bool
    is_expander: bool
    is_focus: bool
    justification: Gtk.Justification | None  # datawidget property
    justify: Gtk.Justification | None  # datawidget property
    kinetic_scrolling: bool
    label: str | None  # datawidget property
    label_widget: Gtk.Widget | None
    label_xalign: float  # datawidget property
    label_yalign: float  # datawidget property
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
    max_width_chars: int  # datawidget property
    min_content_height: int
    min_content_width: int
    mnemonic_widget: Gtk.Widget | None  # datawidget property
    modal: bool
    mode: Gtk.CellRendererMode
    model: Gtk.TreeModel | None
    monospace: bool  # datawidget property
    name: str
    no_show_all: bool
    numeric: bool  # datawidget property
    opacity: float
    overlay_scrolling: bool
    overwrite: bool  # datawidget property
    overwrite_mode: bool  # datawidget property
    page_increment: float  # datawidget property
    page_size: float  # datawidget property
    parent: Gtk.Container | None
    pattern: str | None
    pixels_above_lines: int
    pixels_below_lines: int
    pixels_inside_wrap: int
    placeholder_text: str | None  # datawidget property
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
    progress_fraction: float  # datawidget property
    progress_pulse_step: float  # datawidget property
    propagate_natural_height: bool
    propagate_natural_width: bool
    receives_default: bool
    relief: Gtk.ReliefStyle | None
    rgba: Gdk.RGBA | None
    right_margin: int
    rotation: float  # datawidget property?
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
    show_editor: bool  # datawidget property
    show_emoji_icon: bool
    show_hidden: bool
    single_line_mode: bool
    snap: bool | None
    snap_to_ticks: bool
    step_increment: float  # datawidget property
    tabs: Pango.TabArray | None  # datawidget property
    text: str  # datawidget property
    text_column: int  # datawidget property
    text_length: int  # datawidget property
    title: str
    tooltip: str
    tooltip_column: int
    tooltip_markup: str
    tooltip_text: str
    top_margin: int
    track_visited_links: bool
    truncate_multiline: bool  # datawidget property
    update_policy: Gtk.SpinButtonUpdatePolicy | None
    upper: float
    use_alpha: bool
    use_markup: bool
    use_preview_label: bool
    use_underline: bool  # datawidget property
    vadjustment: Gtk.Adjustment | None
    valign: Gtk.Align | None
    value: float | int  # datawidget property
    vertical_alignment: str
    vexpand: bool
    vexpand_set: bool
    visible: bool
    visibility: bool
    vscroll_policy: Gtk.ScrollablePolicy | None
    vscrollbar_policy: Gtk.PolicyType | None
    weight: int
    weight_set: bool
    width: int
    width_chars: int  # datawidget property
    width_request: int
    window: Gdk.Window | None
    window_placement: Gtk.CornerType | None
    wrap: bool  # datawidget property
    wrap_mode: Gtk.WrapMode | Pango.WrapMode | None  # datawidget property
    wrap_width: int  # datawidget property
    xalign: float
    xpad: int
    yalign: float
    ypad: int


class GTK3GObjectMixin(GObject.Object, ToolkitMixin):
    """Adds GObject-specific attributes."""

    _GTK3_GOBJECT_SIGNALS: list[str] = [
        "notify",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GObjectMixin."""
        GObject.Object.__init__(self)
        ToolkitMixin.__init__(self)

        self.dic_handler_id: dict[str, int] = {
            _signal: -1 for _signal in self._GTK3_GOBJECT_SIGNALS
        }

    def do_set_callbacks(
        self,
        signal: str,
        callback: FunctionType,
        after: bool = False,
    ) -> None:
        """Set the callback method for the GObjectMixin.

        Parameters
        ----------
        signal : str
            The name of the signal to connect the callback to.
        callback : FunctionType
            The callback function or method to connect to the signal.
        after : bool
            Indicates whether the handler is added to the signal handler list before (
            default) or after the default class signal handler.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for this widget.
        """
        try:
            if after:
                self.dic_handler_id[signal] = self.connect_after(
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


def set_widget_sensitivity(widgets: list, sensitive: bool = True) -> None:
    """Set the sensitivity for a list of GTK3 widgets.

    Parameters
    ----------
    widgets : list
        The list of widget objects.
    sensitive : bool
        Whether to make the widgets in the list sensitive or not.
    """
    for _widget in widgets:
        _widget.set_sensitive(sensitive)
