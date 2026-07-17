"""The pytkwrap GTK3 mixins module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import date
from types import EllipsisType, FunctionType
from typing import TypedDict

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.common import PyTkWrapAttributes, PyTkWrapMixin
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, GLib, GObject, Gtk, Pango, cairo
from pytkwrap.utilities import none_to_default


class GTK3WidgetAttributes(PyTkWrapAttributes, total=False):
    """Type for GTK3 widget attributes."""

    column_types: list[EllipsisType] | list[GObject.GType] | None


class GTK3WidgetProperties(TypedDict, total=False):
    """Type for GTK3 widget properties."""

    accel_group: Gtk.AccelGroup
    accel_path: str | None
    accel_size_group: Gtk.SizeGroup | None
    accelerator: str | None
    accept_focus: bool
    accepts_tab: bool
    action: Gtk.FileChooserAction | None
    action_name: str | None
    action_target: GLib.Variant | None
    activate_on_single_click: bool
    activates_default: bool
    active: bool | int
    active_id: str | None
    activatable: bool
    adjustment: Gtk.Adjustment | None
    align_set: bool
    align_widget: Gtk.Container | None
    alignment: float | Pango.Alignment | None
    alpha: int
    always_show_image: bool
    anchor_hints: Gdk.AnchorHints
    angle: float
    app_paintable: bool
    application: Gtk.Application | None
    artists: list
    attach_widget: Gtk.Widget | None
    attached_to: Gtk.Widget | None
    attributes: Pango.AttrList | None
    authors: list
    auto_render: bool
    background: str | None
    background_rgba: Gdk.RGBA | None
    background_set: bool
    baseline_position: Gtk.BaselinePosition
    baseline_row: int
    bold: bool
    border_width: int
    bottom_margin: int
    buffer: Gtk.EntryBuffer | Gtk.TextBuffer | None
    button_sensitivity: Gtk.SensitivityType | None
    buttons: Gtk.ButtonsType
    can_default: bool
    can_focus: bool
    can_target: bool
    caps_lock_warning: bool
    cell_area: Gtk.CellArea | None
    cell_area_context: Gtk.CellAreaContext | None
    cell_background: str | None
    cell_background_rgba: Gdk.RGBA | None
    cell_background_set: bool
    cell_foreground_rgba: Gdk.RGBA | None
    child: Gtk.Widget | None
    child_pack_direction: Gtk.PackDirection
    clickable: bool
    climb_rate: float
    collapsed: bool
    column_homogeneous: bool
    column_spacing: int
    column_span_column: int
    columns: int
    comments: str | None
    completion: Gtk.EntryCompletion | None
    composite_child: bool
    constrain_to: Gtk.PopoverConstraint
    copyright: str | None
    create_folders: bool
    current_alpha: int
    current_rgba: Gdk.RGBA | None
    cursor_position: int
    cursor_visible: bool
    custom_title: str | None
    day: int
    decorated: bool
    decoration_layout: Gtk.DecorationLayout | None
    decoration_layout_set: bool
    default_height: int
    default_width: int
    deletable: bool
    destroy_with_parent: bool
    detail_height_rows: int
    detail_width_chars: int
    dialog: Gtk.Dialog | None
    digits: int
    direction: Gtk.ArrowType
    disabled_text: str | None
    do_overwrite_confirmation: bool
    documenters: list
    draw: bool
    draw_as_radio: bool
    draw_indicator: bool
    draw_sensitive: bool
    draw_value: bool
    editable: bool
    editable_set: bool
    editing_canceled: bool
    ellipsize: Pango.EllipsizeMode | None
    ellipsize_set: bool
    enable_emoji_completion: bool
    enable_grid_lines: Gtk.TreeViewGridLines | None
    enable_popup: bool
    enable_search: bool
    enable_tree_lines: bool
    entry_text_column: int
    events: Gdk.EventMask | None
    expand: bool
    expanded: bool
    expander_column: Gtk.TreeViewColumn | None
    extra_widget: Gtk.Widget | None
    family: str | None
    family_set: bool
    file: str | None
    fill_level: float
    filter: Gtk.FileFilter | None
    fit_model: bool
    fixed_height_mode: bool
    fixed_width: int
    focus_on_click: bool
    focus_on_map: bool
    focus_visible: bool
    font: str | None
    font_desc: Pango.FontDescription | None
    font_name: str
    foreground: str | None
    foreground_rgba: Gdk.RGBA | None
    foreground_set: bool
    fraction: float
    gfile: Gio.File | None
    gicon: Gio.Icon | None
    gravity: Gdk.Gravity
    group: Gtk.RadioButton | Gtk.RadioToolButton | None
    group_name: str | None
    hadjustment: Gtk.Adjustment | None
    halign: Gtk.Align | None
    has_alpha: bool
    has_default: bool
    has_depth_buffer: bool
    has_entry: bool
    has_focus: bool
    has_frame: bool
    has_opacity_control: bool
    has_origin: bool
    has_palette: bool
    has_resize_grip: bool
    has_stencil_buffer: bool
    has_subtitle: bool
    has_tooltip: bool
    has_toplevel_focus: bool
    header_relief: Gtk.ReliefStyle
    headers_clickable: bool
    headers_visible: bool
    heading: str | None
    height: int
    height_request: int
    hexpand: bool
    hexpand_set: bool
    hide_titlebar_when_maximized: bool
    hhomogeneous: bool
    homogeneous: bool
    horizontal_alignment: str
    hover_expand: bool
    hover_selection: bool
    hscroll_policy: Gtk.ScrollablePolicy | None
    hscrollbar_policy: Gtk.PolicyType | None
    icon: str | None
    icons: list[str]
    icon_name: str | None
    icon_set: bool
    icon_size: Gtk.IconSize | int
    icon_size_set: bool
    icon_widget: Gtk.Widget | None
    id_column: int
    image: Gtk.Widget | None
    image_position: Gtk.PositionType
    im_module: str | None
    inconsistent: bool
    indent: int
    inner_border: Gtk.Border | None
    input_hints: Gtk.InputHints | None
    input_purpose: Gtk.InputPurpose | None
    interpolate_size: bool
    inverted: bool
    invisible_char: int | str
    invisible_char_set: bool
    is_active: bool
    is_expanded: bool
    is_expander: bool
    is_focus: bool
    is_important: bool
    is_maximized: bool
    item_orientation: Gtk.Orientation | None
    item_padding: int
    item_width: int
    justification: Gtk.Justification | None
    justify: Gtk.Justification | None
    kinetic_scrolling: bool
    label: str | None
    label_fill: bool
    label_widget: Gtk.Widget | None
    label_xalign: float
    label_yalign: float
    language: str | None
    language_set: bool
    layout_style: Gtk.ButtonBoxStyle
    left_margin: int
    level_indentation: int
    license: str | None
    license_type: Gtk.License
    lines: int
    local_only: bool
    location: Gio.File | None
    logo: GdkPixbuf.Pixbuf | None
    logo_icon_name: str
    lower: float
    margin: int
    margin_bottom: int
    margin_end: int
    margin_start: int
    margin_top: int
    markup: str | None
    markup_column: int
    max_children_per_line: int
    max_content_height: int
    max_content_width: int
    max_height: int
    max_length: int
    max_value: float | int
    max_width: int
    max_width_chars: int
    menu: Gtk.Menu | None
    menu_model: Gio.MenuModel | None
    menu_type_hint: Gdk.WindowTypeHint
    message_area: Gtk.Widget
    message_type: Gtk.MessageType
    min_children_per_line: int
    min_content_height: int
    min_content_width: int
    min_width: int
    min_value: float | int
    mnemonic_widget: Gtk.Widget | None
    mnemonics_visible: bool
    modal: bool
    mode: Gtk.CellRendererMode | Gtk.LevelBarMode
    model: Gtk.TreeModel | None
    monitor: int
    monospace: bool
    month: int
    name: str
    no_month_change: bool
    no_show_all: bool
    numeric: bool
    opacity: float
    open_flags: Gtk.PlacesOpenFlags
    overlay_scrolling: bool
    overwrite: bool
    overwrite_mode: bool
    pack_direction: Gtk.PackDirection
    page: int
    page_increment: float
    page_size: float
    parent: Gtk.Container | None
    pattern: str | None
    pixbuf: Gdk.Pixbuf.Pixbuf | None
    pixbuf_animation: Gdk.PixbufAnimation | None
    pixbuf_column: int
    pixbuf_expander_closed: Gdk.Pixbuf.Pixbuf | None
    pixbuf_expander_open: Gdk.Pixbuf.Pixbuf | None
    pixel_size: int
    pixels_above_lines: int
    pixels_below_lines: int
    pixels_inside_wrap: int
    placeholder_text: str | None
    pointing_to: Gdk.Rectangle | None
    popover: Gtk.Popover | None
    populate_all: bool
    popup: Gtk.Menu | None
    popup_fixed_width: bool
    popup_shown: bool
    position: Gtk.PositionType | int
    position_set: bool
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
    program_name: str | None
    progress_fraction: float
    progress_pulse_step: float
    propagate_natural_height: bool
    propagate_natural_width: bool
    pulse: int
    pulse_step: float
    radio: bool
    receives_default: bool
    rect_anchor_dx: int
    rect_anchor_dy: int
    relative_to: Gtk.Widget | None
    relief: Gtk.ReliefStyle | None
    reorderable: bool
    reserve_toggle_size: bool
    resizable: bool
    resize_toplevel: bool
    resource: str | None
    restrict_to_fill: bool
    revealed: bool
    rgba: Gdk.RGBA | None
    right_margin: int
    rise: int
    rise_set: bool
    role: str | None
    rotation: float
    round_digits: int
    row_homogeneous: bool
    row_spacing: int
    row_span_column: int
    rubber_banding: bool
    scale: float
    scale_factor: int
    scale_set: bool
    screen: Gdk.Screen | None
    scroll_offset: int
    scrollable: bool
    search_column: int
    search_mode: bool
    search_mode_enabled: bool
    secondary_icon_activatable: bool
    secondary_icon_gicon: Gio.Icon | None
    secondary_icon_name: str | None
    secondary_icon_pixbuf: GdkPixbuf.Pixbuf | None
    secondary_icon_sensitive: bool
    secondary_icon_storage_type: Gtk.ImageType | None
    secondary_icon_tooltip_markup: str | None
    secondary_icon_tooltip_text: str | None
    secondary_text: str | None
    secondary_use_markup: bool
    section_name: str | None
    selectable: bool
    select_multiple: bool
    selection_bound: int
    selection_mode: Gtk.SelectionMode
    sensitive: bool
    shadow_type: Gtk.ShadowType | None
    shortcut_type: Gtk.ShortcutType | None
    show_arrow: bool
    show_border: bool
    show_close_button: bool
    show_day_names: bool
    show_default_item: bool
    show_desktop: bool
    show_details: bool
    show_dialog_item: bool
    show_editor: bool
    show_emoji_icon: bool
    show_enter_location: bool
    show_expanders: bool
    show_fill_level: bool
    show_heading: bool
    show_hidden: bool
    show_menubar: bool
    show_numbers: bool
    show_other_locations: bool
    show_recent: bool
    show_size: bool
    show_starred_location: bool
    show_style: bool
    show_tabs: bool
    show_text: bool
    show_trash: bool
    show_week_numbers: bool
    single_line_mode: bool
    single_paragraph_mode: bool
    size: Gtk.IconSize | int | None
    size_points: float
    size_set: bool
    sizing: Gtk.TreeViewColumnSizing | None
    skip_pager_hint: bool
    skip_taskbar_hint: bool
    snap: bool | None
    snap_to_ticks: bool
    sort_column_id: int
    sort_indicator: bool
    sort_order: Gtk.SortType | None
    spacing: int
    stack: Gtk.Stack | None
    startup_id: str | None
    state: bool
    step_increment: float
    stock_detail: str | None
    stock_size: int
    stretch: Pango.Stretch | None
    stretch_set: bool
    strikethrough: bool
    strikethrough_set: bool
    style: Gtk.Style | Pango.Style | None
    style_set: bool
    submenu: Gtk.Menu | None
    subtitle: str | None
    subtitle_set: bool
    surface: cairo.Surface | None
    tabs: Pango.TabArray | None
    tab_position: Gtk.PositionType
    take_focus: bool
    text: str | None
    text_column: int
    text_length: int
    text_xalign: float
    text_yalign: float
    title: str | None
    title_size_group: Gtk.SizeGroup | None
    toolbar_style: Gtk.ToolbarStyle
    tooltip: str
    tooltip_column: int
    tooltip_markup: str
    tooltip_text: str
    top_margin: int
    track_visited_links: bool
    transient_for: Gtk.Window | None
    transition_duration: int
    transition_type: Gtk.StackTransitionType
    translator_credits: str | None
    truncate_multiline: bool
    type: Gtk.WindowType
    type_hint: Gdk.WindowTypeHint
    underline: Pango.Underline | None
    underline_set: bool
    update_policy: Gtk.SpinButtonUpdatePolicy | None
    upper: float
    urgency_hint: bool
    use_alpha: bool
    use_es: bool
    use_fallback: bool
    use_font: bool
    use_header_bar: bool | int
    use_markup: bool
    use_popover: bool
    use_preview_label: bool
    use_size: bool
    use_style: bool
    use_symbolic: bool
    use_underline: bool
    vadjustment: Gtk.Adjustment | None
    valign: Gtk.Align | None
    value: float | int
    value_pos: Gtk.PositionType
    variant: Pango.Variant | None
    variant_set: bool
    version: str | None
    vertical_alignment: str
    vexpand: bool
    vexpand_set: bool
    vhomogeneous: bool
    view: str | None
    view_name: str | None
    visible: bool
    visible_child: Gtk.Widget | None
    visible_child_name: str | None
    visible_horizontal: bool
    visible_submenu: str | None
    visible_vertical: bool
    visibility: bool
    vscroll_policy: Gtk.ScrollablePolicy | None
    vscrollbar_policy: Gtk.PolicyType | None
    website: str | None
    website_label: str | None
    weight: int
    weight_set: bool
    wide_handle: bool
    widget: object
    width: int
    width_chars: int
    width_request: int
    window: Gdk.Window | None
    window_placement: Gtk.CornerType | None
    window_position: Gtk.WindowPosition
    wrap: bool
    wrap_license: bool
    wrap_mode: Gtk.WrapMode | Pango.WrapMode | None
    wrap_width: int
    x_offset: int
    xalign: float
    xpad: int
    yalign: float
    year: int
    ypad: int


class GTK3GObjectMixin(GObject.Object, PyTkWrapMixin):
    """Adds GObject-specific attributes."""

    _GTK3_GOBJECT_ATTRIBUTES = GTK3WidgetAttributes(
        column_types=None,
        index=-1,
        listen_topic="listen-topic",
        send_topic="send-topic",
    )
    _GTK3_GOBJECT_SIGNALS: list[str] = [
        "notify",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3GObjectMixin."""
        GObject.Object.__init__(self)
        PyTkWrapMixin.__init__(self)

        self.dic_attributes |= self._GTK3_GOBJECT_ATTRIBUTES
        self.dic_handler_id: dict[str, int] = {
            _signal: -1 for _signal in self._GTK3_GOBJECT_SIGNALS
        }

    def do_set_callbacks(
        self,
        signal: list[str] | str,
        callback: FunctionType,
        after: bool = False,
    ) -> None:
        """Set the callback method for the GTK3GObjectMixin.

        Parameters
        ----------
        signal : list[str] | str
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
        if not isinstance(signal, list):
            signal = [signal]

        for _signal in signal:
            try:
                if after:
                    self.dic_handler_id[_signal] = self.connect_after(
                        _signal,
                        callback,
                    )
                else:
                    self.dic_handler_id[_signal] = self.connect(
                        _signal,
                        callback,
                    )
            except TypeError as exc:
                _error_msg = self.dic_error_message["unk_signal"].format(
                    f"{type(self).__name__}.do_set_callbacks()",
                    _signal,
                )
                pub.sendMessage(
                    "do_log_error",
                    message=_error_msg,
                )
                raise UnkSignalError(_error_msg) from exc

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
        _index, _value = next(iter(package.items()))
        _value = none_to_default(_value, self.dic_attributes["default_value"])

        if _index != self.dic_attributes["index"]:
            return

        try:
            with self._block_edit_handlers():
                self.do_set_value(_value)
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.do_update()",
                self.dic_attributes["edit_signal"],
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def on_changed(self, __widget: object) -> None:
        """Retrieve the data package for the widget on value changes.

        This method also sends a PyPubSub message along with the data package for
        listeners to update with the new value.

        Parameters
        ----------
        __widget : GTK3Widget
            The widget that was changed. Unused but required to satisfy the Gtk.Widget()
            callback method structure.
        """
        _package = {self.dic_attributes["index"]: self.do_get_value()}
        pub.sendMessage(
            self.dic_attributes["send_topic"],
            package=_package,
        )

    def _block_edit_handlers(self) -> GObject._HandlerBlockManager:
        """Block the signal handlers for the widget.

        Returns
        -------
        GObject._HandlerBlockManager | None
        """
        _signals = self.dic_attributes["edit_signal"]
        if not isinstance(_signals, list):
            _signals = [self.dic_attributes["edit_signal"]]

        _blockmgr: GObject._HandlerBlockManager = None
        for _signal in _signals:
            _hid = self.dic_handler_id[_signal]
            _blockmgr = self._get_signal_owner().handler_block(_hid)

        return _blockmgr

    def _get_signal_owner(self) -> Gtk.Widget:
        """Return the object whose signal handler should be blocked.

        Override in subclasses where the signal is owned by a child object rather than
        the widget itself (e.g. GTK3TextView's TextBuffer).

        Returns
        -------
        GTK3Widget
        """
        return self


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
