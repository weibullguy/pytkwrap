# Standard Library Imports
import abc
from abc import abstractmethod
from datetime import date
from types import FunctionType
from typing import TypedDict

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common import WidgetMixin as WidgetMixin
from pytkwrap.exceptions import UnkSignalError as UnkSignalError
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import GLib as GLib
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3._libs import _ as _
from pytkwrap.gtk3.mixins import GTK3DataWidgetMixin as GTK3DataWidgetMixin
from pytkwrap.utilities import none_to_default as none_to_default

class GTK3WidgetProperties(TypedDict, total=False):
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
    update_policy: Gtk.SpinButtonUpdatePolicy | None
    upper: float
    use_alpha: bool
    use_markup: bool
    use_preview_label: bool
    use_underline: bool
    vadjustment: Gtk.Adjustment | None
    valign: Gtk.Align | None
    value: float | int
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
    _GTK3_BASE_PROPERTIES: Incomplete
    _GTK3_BASE_SIGNALS: list[str]
    dic_properties: Incomplete
    dic_handler_id: dict[str, int]
    def __init__(self) -> None: ...
    def do_set_callbacks(self, signal: str, callback: FunctionType) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...

class GTK3BaseDataWidget(GTK3BaseWidget, GTK3DataWidgetMixin, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def do_get_value(self) -> bool | date | float | int | str | None: ...
    @abstractmethod
    def do_set_value(self, value) -> None: ...
    def do_update(
        self, package: dict[str, bool | date | float | int | str | None]
    ) -> None: ...
    def on_changed(self, /, __widget: GTK3BaseWidget) -> None: ...
    def _get_signal_owner(self) -> GTK3BaseDataWidget: ...
