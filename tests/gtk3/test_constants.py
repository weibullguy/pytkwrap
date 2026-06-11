# Standard Library Imports
import sys
from datetime import date

try:
    # Third Party Imports
    import gi

    gi.require_version("Gdk", "3.0")
    gi.require_version("GLib", "2.0")
    gi.require_version("Gtk", "3.0")
except ImportError:
    print("Failed to import package gi; exiting.")
    sys.exit(1)
# Third Party Imports
from gi.repository import Gdk, GObject, Gtk, Pango

EXPECTED_GOBJECT_ATTRIBUTES: dict[str, int | str | None] = {
    "axis": None,
    "canvas": None,
    "column_types": None,
    "data_type": None,
    "default_value": None,
    "edit_signal": None,
    "figure": None,
    "font_description": None,
    "format": None,
    "index": -1,
    "listen_topic": "listen-topic",
    "n_columns": None,
    "n_rows": None,
    "send_topic": "send-topic",
    "x_pos": None,
    "y_pos": None,
}
EXPECTED_GOBJECT_HANDLER_IDS = {"notify": -1}
EXPECTED_GOBJECT_METHODS = [
    "bind_property",
    "bind_property_full",
    "connect",
    "connect_after",
    "disconnect",
    "emit",
    "force_floating",
    "freeze_notify",
    "get_data",
    "get_property",
    "get_qdata",
    "getv",
    "handler_block",
    "handler_unblock",
    "is_floating",
    "notify",
    "notify_by_pspec",
    "ref",
    "ref_sink",
    "run_dispose",
    "set_data",
    "set_property",
    "steal_data",
    "steal_qdata",
    "thaw_notify",
    "unref",
    "watch_closure",
]

EXPECTED_ADJUSTMENT_ATTRIBUTES = {"default_value": 0.0, "edit_signal": "value-changed"}
EXPECTED_ADJUSTMENT_HANDLER_IDS = {"changed": -1, "value-changed": -1}
EXPECTED_ADJUSTMENT_METHODS = [
    "clamp_page",
    "configure",
    "get_lower",
    "get_minimum_increment",
    "get_page_increment",
    "get_page_size",
    "get_step_increment",
    "get_upper",
    "get_value",
    "set_lower",
    "set_page_increment",
    "set_page_size",
    "set_step_increment",
    "set_upper",
    "set_value",
]
EXPECTED_ADJUSTMENT_PROPERTIES = {
    "lower": 0.0,
    "page_increment": 0.0,
    "page_size": 0.0,
    "step_increment": 0.0,
    "upper": 0.0,
    "value": 0.0,
}

EXPECTED_CELL_RENDERER_HANDLER_IDS = {"editing-canceled": -1, "editing-started": -1}
EXPECTED_CELL_RENDERER_METHODS = [
    "activate",
    "get_aligned_area",
    "get_alignment",
    "get_fixed_size",
    "get_padding",
    "get_preferred_height",
    "get_preferred_height_for_width",
    "get_preferred_size",
    "get_preferred_width",
    "get_preferred_width_for_height",
    "get_request_mode",
    "get_sensitive",
    "get_state",
    "get_visible",
    "is_activatable",
    "render",
    "set_alignment",
    "set_fixed_size",
    "set_padding",
    "set_sensitive",
    "set_visible",
    "start_editing",
    "stop_editing",
]
EXPECTED_CELL_RENDERER_PROPERTIES = {
    "cell_background": None,
    "cell_background_rgba": None,
    "cell_background_set": False,
    "height": -1,
    "is_expanded": False,
    "is_expander": False,
    "mode": Gtk.CellRendererMode.INERT,
    "sensitive": True,
    "visible": True,
    "width": -1,
    "xalign": 0.5,
    "xpad": 0,
    "yalign": 0.5,
    "ypad": 0,
}

EXPECTED_CELLRENDERERPIXBUF_PROPERTIES = {
    "gicon": None,
    "icon_name": None,
    "pixbuf": None,
    "pixbuf_expander_closed": None,
    "pixbuf_expander_open": None,
    "stock_detail": None,
    "stock_size": 1,
    "surface": None,
}

EXPECTED_CELLRENDERERPROGRESS_PROPERTIES = {
    "inverted": False,
    "pulse": -1,
    "text": None,
    "text_xalign": 0.5,
    "text_yalign": 0.5,
    "value": 0,
}

EXPECTED_CELLRENDERESPINNER_PROPERTIES = {
    "active": False,
    "pulse": 0,
    "size": Gtk.IconSize.MENU,
}

EXPECTED_CELLRENDERERTEXT_HANDLER_IDS = {"edited": -1}
EXPECTED_CELLRENDERERTEXT_METHODS = ["set_fixed_height_from_font"]
EXPECTED_CELLRENDERERTEXT_PROPERTIES = {
    "align_set": False,
    "alignment": Pango.Alignment.LEFT,
    "attributes": None,
    "background": None,
    "background_rgba": None,
    "background_set": False,
    "editable": False,
    "editable_set": False,
    "ellipsize": Pango.EllipsizeMode.NONE,
    "ellipsize_set": False,
    "family": None,
    "family_set": False,
    "font": None,
    "font_desc": None,
    "foreground": None,
    "foreground_rgba": None,
    "foreground_set": False,
    "language": None,
    "language_set": False,
    "markup": None,
    "max_width_chars": -1,
    "placeholder_text": None,
    "rise": 0,
    "rise_set": False,
    "scale": 1.0,
    "scale_set": False,
    "single_paragraph_mode": False,
    "size": 0,
    "size_points": 0.0,
    "size_set": False,
    "stretch": Pango.Stretch.NORMAL,
    "stretch_set": False,
    "strikethrough": False,
    "strikethrough_set": False,
    "style": Pango.Style.NORMAL,
    "style_set": False,
    "text": None,
    "underline": Pango.Underline.NONE,
    "underline_set": False,
    "variant": Pango.Variant.NORMAL,
    "variant_set": False,
    "weight": 400,
    "weight_set": False,
    "width_chars": -1,
    "wrap_mode": Pango.WrapMode.CHAR,
    "wrap_width": -1,
}

EXPECTED_CELLRENDERERCOMBO_HANDLER_IDS = {"changed": -1}
EXPECTED_CELLRENDERERCOMBO_PROPERTIES = {
    "has_entry": True,
    "model": None,
    "text_column": -1,
}

EXPECTED_TREEVIEW_COLUMN_HANDLER_IDS = {"clicked": -1}
EXPECTED_TREEVIEW_COLUMN_METHODS = [
    "add_attribute",
    "cell_get_position",
    "cell_get_size",
    "cell_is_visible",
    "cell_set_cell_data",
    "clear",
    "clear_attributes",
    "clicked",
    "focus_cell",
    "get_alignment",
    "get_button",
    "get_clickable",
    "get_expand",
    "get_fixed_width",
    "get_max_width",
    "get_min_width",
    "get_reorderable",
    "get_resizable",
    "get_sizing",
    "get_sort_column_id",
    "get_sort_indicator",
    "get_sort_order",
    "get_spacing",
    "get_title",
    "get_tree_view",
    "get_visible",
    "get_widget",
    "get_width",
    "get_x_offset",
    "pack_end",
    "pack_start",
    "queue_resize",
    "set_alignment",
    "set_attributes",
    "set_cell_data_func",
    "set_clickable",
    "set_expand",
    "set_fixed_width",
    "set_max_width",
    "set_min_width",
    "set_reorderable",
    "set_resizable",
    "set_sizing",
    "set_sort_column_id",
    "set_sort_indicator",
    "set_sort_order",
    "set_spacing",
    "set_title",
    "set_visible",
    "set_widget",
]
EXPECTED_TREEVIEW_COLUMN_PROPERTIES = {
    "alignment": 0.0,
    "cell_area": None,
    "clickable": False,
    "expand": False,
    "fixed_width": -1,
    "max_width": -1,
    "min_width": -1,
    "reorderable": False,
    "resizable": False,
    "sizing": Gtk.TreeViewColumnSizing.GROW_ONLY,
    "sort_column_id": -1,
    "sort_indicator": False,
    "sort_order": Gtk.SortType.ASCENDING,
    "spacing": 0,
    "title": "",
    "visible": True,
    "widget": None,
    "width": 0,
    "x_offset": 0,
}

EXPECTED_WIDGET_ATTRIBUTES: dict[str, int | str | None] = {
    "axis": None,
    "canvas": None,
    "column_types": None,
    "data_type": None,
    "default_value": None,
    "edit_signal": None,
    "figure": None,
    "font_description": None,
    "format": None,
    "n_columns": None,
    "n_rows": None,
    "x_pos": 0,
    "y_pos": 0,
}
EXPECTED_WIDGET_HANDLER_IDS = {
    "destroy": -1,
    "direction-changed": -1,
    "hide": -1,
    "keynav-failed": -1,
    "map": -1,
    "mnemonic-activate": -1,
    "move-focus": -1,
    "query-tooltip": -1,
    "realize": -1,
    "show": -1,
    "state-flags-changed": -1,
    "unmap": -1,
    "unrealize": -1,
}
EXPECTED_WIDGET_METHODS = [
    "activate",
    "add_accelerator",
    "add_device_events",
    "add_events",
    "add_mnemonic_label",
    "add_tick_callback",
    "can_activate_accel",
    "child_focus",
    "child_notify",
    "compute_expand",
    "create_pango_context",
    "create_pango_layout",
    "destroy",
    "destroyed",
    "device_is_shadowed",
    "drag_begin_with_coordinates",
    "drag_check_threshold",
    "drag_dest_add_image_targets",
    "drag_dest_add_text_targets",
    "drag_dest_add_uri_targets",
    "drag_dest_find_target",
    "drag_dest_get_target_list",
    "drag_dest_get_track_motion",
    "drag_dest_set",
    "drag_dest_set_target_list",
    "drag_dest_set_track_motion",
    "drag_dest_unset",
    "drag_get_data",
    "drag_highlight",
    "drag_source_add_image_targets",
    "drag_source_add_text_targets",
    "drag_source_add_uri_targets",
    "drag_source_get_target_list",
    "drag_source_set",
    "drag_source_set_icon_gicon",
    "drag_source_set_icon_name",
    "drag_source_set_icon_pixbuf",
    "drag_source_set_target_list",
    "drag_source_unset",
    "drag_unhighlight",
    "draw",
    "error_bell",
    "event",
    "freeze_child_notify",
    "get_accessible",
    "get_action_group",
    "get_allocated_baseline",
    "get_allocated_height",
    "get_allocated_size",
    "get_allocated_width",
    "get_allocation",
    "get_ancestor",
    "get_app_paintable",
    "get_can_default",
    "get_can_focus",
    "get_child_visible",
    "get_clip",
    "get_clipboard",
    "get_device_enabled",
    "get_device_events",
    "get_direction",
    "get_display",
    "get_double_buffered",
    "get_events",
    "get_focus_on_click",
    "get_font_map",
    "get_font_options",
    "get_frame_clock",
    "get_halign",
    "get_has_tooltip",
    "get_has_window",
    "get_hexpand",
    "get_hexpand_set",
    "get_mapped",
    "get_margin_bottom",
    "get_margin_end",
    "get_margin_start",
    "get_margin_top",
    "get_modifier_mask",
    "get_name",
    "get_no_show_all",
    "get_opacity",
    "get_pango_context",
    "get_parent",
    "get_parent_window",
    "get_path",
    "get_preferred_height",
    "get_preferred_height_and_baseline_for_width",
    "get_preferred_height_for_width",
    "get_preferred_size",
    "get_preferred_width",
    "get_preferred_width_for_height",
    "get_realized",
    "get_receives_default",
    "get_request_mode",
    "get_scale_factor",
    "get_screen",
    "get_sensitive",
    "get_settings",
    "get_size_request",
    "get_state_flags",
    "get_style_context",
    "get_support_multidevice",
    "get_template_child",
    "get_tooltip_markup",
    "get_tooltip_text",
    "get_tooltip_window",
    "get_toplevel",
    "get_valign",
    "get_valign_with_baseline",
    "get_vexpand",
    "get_vexpand_set",
    "get_visible",
    "get_visual",
    "get_window",
    "grab_add",
    "grab_default",
    "grab_focus",
    "grab_remove",
    "has_default",
    "has_focus",
    "has_grab",
    "has_visible_focus",
    "hide",
    "hide_on_delete",
    "in_destruction",
    "init_template",
    "input_shape_combine_region",
    "insert_action_group",
    "intersect",
    "is_ancestor",
    "is_drawable",
    "is_focus",
    "is_sensitive",
    "is_toplevel",
    "is_visible",
    "keynav_failed",
    "list_accel_closures",
    "list_action_prefixes",
    "list_mnemonic_labels",
    "map",
    "mnemonic_activate",
    "queue_allocate",
    "queue_draw",
    "queue_draw_area",
    "queue_resize",
    "queue_resize_no_redraw",
    "realize",
    "register_window",
    "remove_accelerator",
    "remove_mnemonic_label",
    "remove_tick_callback",
    "reset_style",
    "send_focus_change",
    "set_accel_path",
    "set_allocation",
    "set_app_paintable",
    "set_can_default",
    "set_can_focus",
    "set_child_visible",
    "set_clip",
    "set_device_enabled",
    "set_device_events",
    "set_direction",
    "set_events",
    "set_focus_on_click",
    "set_font_map",
    "set_font_options",
    "set_halign",
    "set_has_tooltip",
    "set_has_window",
    "set_hexpand",
    "set_hexpand_set",
    "set_mapped",
    "set_margin_bottom",
    "set_margin_end",
    "set_margin_start",
    "set_margin_top",
    "set_name",
    "set_no_show_all",
    "set_opacity",
    "set_parent",
    "set_parent_window",
    "set_realized",
    "set_receives_default",
    "set_redraw_on_allocate",
    "set_sensitive",
    "set_size_request",
    "set_state_flags",
    "set_support_multidevice",
    "set_tooltip_markup",
    "set_tooltip_text",
    "set_tooltip_window",
    "set_valign",
    "set_vexpand",
    "set_vexpand_set",
    "set_visible",
    "set_visual",
    "set_window",
    "shape_combine_region",
    "show",
    "show_all",
    "show_now",
    "size_allocate",
    "size_allocate_with_baseline",
    "size_request",
    "style_get_property",
    "thaw_child_notify",
    "translate_coordinates",
    "trigger_tooltip_query",
    "unmap",
    "unparent",
    "unrealize",
    "unregister_window",
    "unset_state_flags",
]
EXPECTED_WIDGET_PROPERTIES = {
    "app_paintable": False,
    "can_default": False,
    "can_focus": False,
    "composite_child": False,
    "events": Gdk.EventMask.ALL_EVENTS_MASK,
    "expand": False,
    "focus_on_click": True,
    "halign": Gtk.Align.FILL,
    "has_default": False,
    "has_focus": False,
    "has_tooltip": False,
    "height_request": -1,
    "hexpand": False,
    "hexpand_set": False,
    "is_focus": False,
    "margin": 0,
    "margin_bottom": 0,
    "margin_end": 0,
    "margin_start": 0,
    "margin_top": 0,
    "name": "pytkwrap GTK3 widget",
    "no_show_all": False,
    "opacity": 1.0,
    "parent": None,
    "receives_default": False,
    "scale_factor": 1,
    "sensitive": True,
    "style": None,
    "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
    "tooltip_text": "Missing tooltip, please file an issue to have one added.",
    "valign": Gtk.Align.FILL,
    "vexpand": False,
    "vexpand_set": False,
    "visible": False,
    "width_request": -1,
    "window": None,
}

EXPECTED_CALENDAR_ATTRIBUTES = {
    "default_value": date.today(),
    "edit_signal": [
        "day-selected",
        "month-changed",
        "next-month",
        "next-year",
        "prev-month",
        "prev-year",
    ],
}
EXPECTED_CALENDAR_HANDLER_IDS = {
    "day-selected": -1,
    "day-selected-double-click": -1,
    "month-changed": -1,
    "next-month": -1,
    "next-year": -1,
    "prev-month": -1,
    "prev-year": -1,
}
EXPECTED_CALENDAR_METHODS = [
    "clear_marks",
    "get_date",
    "get_day_is_marked",
    "get_detail_height_rows",
    "get_detail_width_chars",
    "get_display_options",
    "mark_day",
    "select_day",
    "select_month",
    "set_detail_func",
    "set_detail_height_rows",
    "set_detail_width_chars",
    "set_display_options",
    "unmark_day",
]
EXPECTED_CALENDAR_PROPERTIES = {
    "day": 0,
    "detail_height_rows": 0,
    "detail_width_chars": 0,
    "month": 0,
    "no_month_change": False,
    "show_day_names": True,
    "show_details": True,
    "show_heading": True,
    "show_week_numbers": False,
    "year": 0,
}

EXPECTED_CONTAINER_HANDLER_IDS = {
    "add": -1,
    "check-resize": -1,
    "remove": -1,
    "set-focus-child": -1,
}
EXPECTED_CONTAINER_METHODS = [
    "add",
    "check_resize",
    "child_get",
    "child_get_property",
    "child_notify",
    "child_notify_by_pspec",
    "child_set",
    "child_set_property",
    "child_type",
    "forall",
    "foreach",
    "get_border_width",
    "get_children",
    "get_focus_child",
    "get_focus_hadjustment",
    "get_focus_vadjustment",
    "get_path_for_child",
    "propagate_draw",
    "remove",
    "set_border_width",
    "set_focus_child",
    "set_focus_hadjustment",
    "set_focus_vadjustment",
]
EXPECTED_CONTAINER_PROPERTIES = {"border_width": 0}

EXPECTED_BIN_METHODS = ["get_child"]

EXPECTED_BUTTON_HANDLER_IDS = {"activate": -1, "check-resize": -1, "clicked": -1}
EXPECTED_BUTTON_METHODS = [
    "clicked",
    "get_always_show_image",
    "get_event_window",
    "get_image",
    "get_image_position",
    "get_label",
    "get_relief",
    "get_use_underline",
    "set_always_show_image",
    "set_image",
    "set_image_position",
    "set_label",
    "set_relief",
    "set_use_underline",
]
EXPECTED_BUTTON_PROPERTIES = {
    "always_show_image": False,
    "image": None,
    "image_position": Gtk.PositionType.LEFT,
    "label": "...",
    "relief": Gtk.ReliefStyle.NORMAL,
    "use_underline": False,
}

EXPECTED_COLOR_BUTTON_ATTRIBUTES = {"default_value": None, "edit_signal": "color-set"}
EXPECTED_COLOR_BUTTON_HANDLER_IDS = {"color-set": -1}
EXPECTED_COLOR_BUTTON_METHODS = [
    "get_title",
    "set_title",
]
EXPECTED_COLOR_BUTTON_PROPERTIES = {
    "alpha": 65535,
    "rgba": None,
    "show_editor": False,
    "title": "Pick a Color",
    "use_alpha": True,
}

EXPECTED_FONT_BUTTON_ATTRIBUTES = {
    "default_value": "Sans 12",
    "edit_signal": "font-set",
}
EXPECTED_FONT_BUTTON_HANDLER_IDS = {"font-set": -1}
EXPECTED_FONT_BUTTON_METHODS = [
    "get_show_size",
    "get_show_style",
    "get_title",
    "get_use_font",
    "get_use_size",
    "set_show_size",
    "set_show_style",
    "set_title",
    "set_use_font",
    "set_use_size",
]
EXPECTED_FONT_BUTTON_PROPERTIES = {
    "font_name": "Sans 12",
    "show_size": True,
    "show_style": True,
    "title": "Pick a Font",
    "use_font": False,
    "use_size": False,
}

EXPECTED_SCALE_BUTTON_ATTRIBUTES = {
    "default_value": 0.0,
    "edit_signal": "value-changed",
}
EXPECTED_SCALE_BUTTON_HANDLER_IDS = {"popdown": -1, "popup": -1, "value-changed": -1}
EXPECTED_SCALE_BUTTON_METHODS = [
    "get_adjustment",
    "get_minus_button",
    "get_plus_button",
    "get_popup",
    "get_value",
    "set_adjustment",
    "set_icons",
    "set_value",
]
EXPECTED_SCALE_BUTTON_PROPERTIES = {
    "adjustment": None,
    "icons": [],
    "size": Gtk.IconSize.SMALL_TOOLBAR,
    "value": 0.0,
}

EXPECTED_VOLUME_BUTTON_PROPERTIES = {"use_symbolic": True}

EXPECTED_TOGGLE_BUTTON_ATTRIBUTES = {"default_value": False, "edit_signal": "toggled"}
EXPECTED_TOGGLE_BUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLE_BUTTON_METHODS = [
    "get_active",
    "get_inconsistent",
    "get_mode",
    "set_active",
    "set_inconsistent",
    "set_mode",
    "toggled",
]
EXPECTED_TOGGLE_BUTTON_PROPERTIES = {
    "active": False,
    "draw_indicator": False,
    "inconsistent": False,
    "use_underline": False,
}

EXPECTED_RADIO_BUTTON_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIO_BUTTON_METHODS = [
    "get_group",
    "join_group",
    "set_group",
]
EXPECTED_RADIO_BUTTON_PROPERTIES = {"group": None}

EXPECTED_MENU_BUTTON_METHODS = [
    "get_align_widget",
    "get_direction",
    "get_menu_model",
    "get_popover",
    "get_popup",
    "get_use_popover",
    "set_align_widget",
    "set_direction",
    "set_menu_model",
    "set_popover",
    "set_popup",
    "set_use_popover",
]
EXPECTED_MENU_BUTTON_PROPERTIES = {
    "align_widget": None,
    "direction": Gtk.ArrowType.DOWN,
    "menu_model": None,
    "popover": None,
    "popup": None,
    "use_popover": True,
}

EXPECTED_COMBOBOX_ATTRIBUTES = {
    "column_types": [GObject.TYPE_STRING],
    "default_value": -1,
    "edit_signal": "changed",
}
EXPECTED_COMBOBOX_HANDLER_IDS = {
    "changed": -1,
    "editing-done": -1,
    "format-entry-text": -1,
    "move-active": -1,
    "popdown": -1,
    "popup": -1,
    "remove-widget": -1,
}
EXPECTED_COMBOBOX_METHODS = [
    "get_active",
    "get_active_id",
    "get_active_iter",
    "get_add_tearoffs",
    "get_button_sensitivity",
    "get_column_span_column",
    "get_entry_text_column",
    "get_has_entry",
    "get_id_column",
    "get_model",
    "get_popup_accessible",
    "get_popup_fixed_width",
    "get_row_span_column",
    "get_wrap_width",
    "popdown",
    "popup",
    "popup_for_device",
    "set_active",
    "set_active_id",
    "set_active_iter",
    "set_button_sensitivity",
    "set_column_span_column",
    "set_entry_text_column",
    "set_id_column",
    "set_model",
    "set_popup_fixed_width",
    "set_row_separator_func",
    "get_row_span_column",
    "set_wrap_width",
]
EXPECTED_COMBOBOX_PROPERTIES = {
    "active": -1,
    "active_id": None,
    "button_sensitivity": Gtk.SensitivityType.AUTO,
    "cell_area": None,
    "column_span_column": -1,
    "editing_canceled": False,
    "entry_text_column": -1,
    "has_entry": False,
    "has_frame": True,
    "id_column": -1,
    "model": None,
    "popup_fixed_width": True,
    "popup_shown": False,
    "row_span_column": -1,
    "wrap_width": 0,
}

EXPECTED_APP_CHOOSER_BUTTON_HANDLER_IDS = {"custom-item-activated": -1}
EXPECTED_APP_CHOOSER_BUTTON_METHODS = [
    "append_custom_item",
    "append_separator",
    "get_heading",
    "get_show_default_item",
    "get_show_dialog_item",
    "set_active_custom_item",
    "set_heading",
    "set_show_default_item",
    "set_show_dialog_item",
]
EXPECTED_APP_CHOOSER_BUTTON_PROPERTIES = {
    "heading": None,
    "show_default_item": False,
    "show_dialog_item": False,
}

EXPECTED_FRAME_METHODS = [
    "get_label",
    "get_label_align",
    "get_label_widget",
    "get_shadow_type",
    "set_label",
    "set_label_align",
    "set_label_widget",
    "set_shadow_type",
]
EXPECTED_FRAME_PROPERTIES = {
    "label": None,
    "label_widget": None,
    "label_xalign": 0.0,
    "label_yalign": 0.5,
    "shadow_type": Gtk.ShadowType.ETCHED_IN,
}

EXPECTED_MENU_ITEM_HANDLER_IDS = {
    "activate": -1,
    "activate-item": -1,
    "deselect": -1,
    "select": -1,
    "toggle-size-allocate": -1,
    "toggle-size-request": -1,
}
EXPECTED_MENU_ITEM_METHODS = [
    "activate",
    "deselect",
    "get_accel_path",
    "get_label",
    "get_reserve_indicator",
    "get_submenu",
    "get_use_underline",
    "select",
    "set_accel_path",
    "set_label",
    "set_reserve_indicator",
    "set_submenu",
    "set_use_underline",
    "toggle_size_allocate",
    "toggle_size_request",
]
EXPECTED_MENU_ITEM_PROPERTIES = {
    "accel_path": None,
    "label": "",
    "submenu": None,
    "use_underline": False,
}

EXPECTED_CHECK_MENU_ITEM_HANDLER_IDS = {"toggled": -1}
EXPECTED_CHECK_MENU_ITEM_METHODS = [
    "get_active",
    "get_draw_as_radio",
    "get_inconsistent",
    "set_active",
    "set_draw_as_radio",
    "set_inconsistent",
    "toggled",
]
EXPECTED_CHECK_MENU_ITEM_PROPERTIES = {
    "active": False,
    "draw_as_radio": False,
    "inconsistent": False,
}

EXPECTED_RADIO_MENU_ITEM_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIO_MENU_ITEM_METHODS = ["get_group", "join_group", "set_group"]
EXPECTED_RADIO_MENU_ITEM_PROPERTIES = {"group": None}

EXPECTED_POPOVER_HANDLER_IDS = {"closed": -1}
EXPECTED_POPOVER_METHODS = [
    "bind_model",
    "get_constrain_to",
    "get_default_widget",
    "get_modal",
    "get_pointing_to",
    "get_position",
    "get_relative_to",
    "popdown",
    "popup",
    "set_constrain_to",
    "set_default_widget",
    "set_modal",
    "set_pointing_to",
    "set_position",
    "set_relative_to",
]
EXPECTED_POPOVER_PROPERTIES = {
    "constrain_to": Gtk.PopoverConstraint.WINDOW,
    "modal": True,
    "pointing_to": None,
    "position": Gtk.PositionType.TOP,
    "relative_to": None,
}

EXPECTED_POPOVER_MENU_PROPERTIES = {"visible_submenu": None}

EXPECTED_SCROLLED_WINDOW_HANDLER_IDS = {
    "edge-overshot": -1,
    "edge-reached": -1,
    "move-focus-out": -1,
    "scroll-child": -1,
}
EXPECTED_SCROLLED_WINDOW_PROPERTIES = {
    "hadjustment": None,
    "hscrollbar_policy": Gtk.PolicyType.AUTOMATIC,
    "kinetic_scrolling": True,
    "max_content_height": -1,
    "max_content_width": -1,
    "min_content_height": -1,
    "min_content_width": -1,
    "overlay_scrolling": True,
    "propogate_natural_height": False,
    "propogate_natural_width": False,
    "shadow_type": Gtk.ShadowType.NONE,
    "vadjustment": None,
    "vscrollbar_policy": Gtk.PolicyType.AUTOMATIC,
    "window_placement": Gtk.CornerType.TOP_LEFT,
}

EXPECTED_PLACES_SIDEBAR_HANDLER_IDS = {
    "drag-action-ask": -1,
    "drag-action-requested": -1,
    "drag-perform-drop": -1,
    "mount": -1,
    "open-location": -1,
    "populate-popup": -1,
    "show-connect-to-server": -1,
    "show-enter-location": -1,
    "show-error-message": -1,
    "show-other-locations": -1,
    "show-other-locations-with-flags": -1,
    "show-starred-location": -1,
    "unmount": -1,
}
EXPECTED_PLACES_SIDEBAR_PROPERTIES = {
    "local_only": False,
    "location": None,
    "open_flags": Gtk.PlacesOpenFlags.NORMAL,
    "populate_all": False,
    "show_desktop": True,
    "show_enter_location": False,
    "show_other_locations": False,
    "show_recent": True,
    "show_starred_location": False,
    "show_trash": True,
}

EXPECTED_SEARCHBAR_PROPERTIES = {
    "search_mode_enabled": False,
    "show_close_button": False,
}

EXPECTED_TOOL_ITEM_HANDLER_IDS = {"create-menu-proxy": -1, "toolbar-reconfigured": -1}
EXPECTED_TOOL_ITEM_PROPERTIES = {
    "is_important": False,
    "visible_horizontal": True,
    "visible_vertical": True,
}

EXPECTED_SEPARATOR_TOOL_ITEM_PROPERTIES = {"draw": True}

EXPECTED_TOOL_BUTTON_HANDLER_IDS = {"clicked": -1}
EXPECTED_TOOL_BUTTON_PROPERTIES = {
    "icon_name": None,
    "icon_widget": None,
    "label": None,
    "label_widget": None,
    "use_underline": False,
}

EXPECTED_MENU_TOOL_BUTTON_HANDLER_IDS = {"show-menu": -1}
EXPECTED_MENU_TOOL_BUTTON_PROPERTIES = {"menu": None}

EXPECTED_TOGGLE_TOOL_BUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLE_TOOL_BUTTON_PROPERTIES = {"active": False}

EXPECTED_RADIO_TOOL_BUTTON_PROPERTIES = {"group": None}

EXPECTED_VIEWPORT_PROPERTIES = {"shadow_type": Gtk.ShadowType.IN}

EXPECTED_WINDOW_HANDLER_IDS = {
    "activate-default": -1,
    "activate-focus": -1,
    "enable-debugging": -1,
    "keys-changed": -1,
    "set-focus": -1,
}
EXPECTED_WINDOW_PROPERTIES = {
    "accept_focus": True,
    "application": None,
    "attached_to": None,
    "decorated": True,
    "default_height": -1,
    "default_width": -1,
    "deletable": True,
    "destroy_with_parent": False,
    "focus_on_map": True,
    "focus_visible": True,
    "gravity": Gdk.Gravity.NORTH_WEST,
    "has_toplevel_focus": False,
    "hide_titlebar_when_maximized": False,
    "icon": None,
    "icon_name": None,
    "mnemonics_visible": True,
    "modal": False,
    "resizable": True,
    "role": None,
    "screen": None,
    "skip_taskbar_hint": False,
    "startup_id": None,
    "title": "pytkwrap GTK3 window",
    "transient_for": None,
    "type": Gdk.WindowType.TOPLEVEL,
    "type_hint": Gdk.WindowTypeHint.NORMAL,
    "urgency_hint": False,
    "window_position": Gtk.WindowPosition.NONE,
}

EXPECTED_ASSISTANT_HANDLER_IDS = {
    "apply": -1,
    "cancel": -1,
    "close": -1,
    "escape": -1,
    "prepare": -1,
}
EXPECTED_ASSISTANT_PROPERTIES = {"use_header_bar": -1}

EXPECTED_DIALOG_HANDLER_IDS = {"close": -1, "response": -1}
EXPECTED_DIALOG_PROPERTIES = {"use_header_bar": -1}

EXPECTED_ABOUT_DIALOG_HANDLER_IDS = {"activate-link": -1}
EXPECTED_ABOUT_DIALOG_PROPERTIES = {
    "artists": [],
    "authors": [],
    "comments": None,
    "copyright": None,
    "documenters": [],
    "license": None,
    "license_type": Gtk.License.UNKNOWN,
    "logo": None,
    "logo_icon_name": "image-missing",
    "program_name": None,
    "translator_credits": None,
    "version": None,
    "website": None,
    "website_label": None,
    "wrap_license": False,
}

EXPECTED_APP_CHOOSER_DIALOG_PROPERTIES = {"gfile": None, "heading": None}

EXPECTED_COLOR_CHOOSER_DIALOG_PROPERTIES = {"show_editor": False}

EXPECTED_MESSAGE_DIALOG_PROPERTIES = {
    "buttons": Gtk.ButtonsType.NONE,
    "message_area": None,
    "message_type": Gtk.MessageType.INFO,
    "secondary_text": None,
    "secondary_use_markup": False,
    "text": "",
    "use_markup": False,
}

EXPECTED_SHORTCUTS_WINDOW_HANDLER_IDS = {"close": -1, "search": -1}
EXPECTED_SHORTCUTS_WINDOW_PROPERTIES = {
    "section_name": "internal-search",
    "view_name": None,
}
