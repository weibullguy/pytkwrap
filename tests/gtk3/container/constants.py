# Standard Library Imports
import sys

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
from gi.repository import Gtk

EXPECTED_BIN_METHODS = ["get_child"]

EXPECTED_BOX_METHODS = [
    "get_baseline_position",
    "get_center_widget",
    "get_homogeneous",
    "get_spacing",
    "pack_end",
    "pack_start",
    "query_child_packing",
    "reorder_child",
    "set_baseline_position",
    "set_center_widget",
    "set_child_packing",
    "set_homogeneous",
    "set_spacing",
]
EXPECTED_BOX_PROPERTIES = {
    "baseline_position": Gtk.BaselinePosition.CENTER,
    "homogeneous": False,
    "spacing": 0,
}

EXPECTED_BUTTONBOX_METHODS = [
    "get_child_non_homogeneous",
    "get_child_secondary",
    "get_layout",
    "set_child_non_homogeneous",
    "set_child_secondary",
    "set_layout",
]
EXPECTED_BUTTONBOX_PROPERTIES = {
    "layout_style": Gtk.ButtonBoxStyle.END,
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

EXPECTED_EXPANDER_HANDLER_IDS = {"activate": -1}
EXPECTED_EXPANDER_METHODS = [
    "get_expanded",
    "get_label",
    "get_label_fill",
    "get_label_widget",
    "get_resize_toplevel",
    "get_use_markup",
    "get_use_underline",
    "set_expanded",
    "set_label",
    "set_label_fill",
    "set_label_widget",
    "set_resize_toplevel",
    "set_use_markup",
    "set_use_underline",
]
EXPECTED_EXPANDER_PROPERTIES = {
    "expanded": False,
    "label": None,
    "label_fill": False,
    "label_widget": None,
    "resize_toplevel": False,
    "use_markup": False,
    "use_underline": False,
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

EXPECTED_LISTBOX_HANDLER_IDS = {
    "activate-cursor-row": -1,
    "move-cursor": -1,
    "row-activated": -1,
    "row-selected": -1,
    "select-all": -1,
    "selected-rows-changed": -1,
    "toggle-cursor-row": -1,
    "unselect-all": -1,
}
EXPECTED_LISTBOX_METHODS = [
    "bind_model",
    "drag_highlight_row",
    "drag_unhighlight_row",
    "get_activate_on_single_click",
    "get_adjustment",
    "get_row_at_index",
    "get_row_at_y",
    "get_selected_row",
    "get_selected_rows",
    "get_selection_mode",
    "insert",
    "invalidate_filter",
    "invalidate_headers",
    "invalidate_sort",
    "prepend",
    "select_all",
    "select_row",
    "selected_foreach",
    "set_activate_on_single_click",
    "set_adjustment",
    "set_filter_func",
    "set_header_func",
    "set_placeholder",
    "set_selection_mode",
    "set_sort_func",
    "unselect_all",
    "unselect_row",
]
EXPECTED_LISTBOX_PROPERTIES = {
    "activate_on_single_click": True,
    "selection_mode": Gtk.SelectionMode.SINGLE,
}

EXPECTED_STACKSWITCHER_METHODS = ["get_stack", "set_stack"]
EXPECTED_STACKSWITCHER_PROPERTIES = {"icon_size": 1, "stack": None}

EXPECTED_VIEWPORT_METHODS = [
    "get_bin_window",
    "get_shadow_type",
    "get_view_window",
    "set_shadow_type",
]
EXPECTED_VIEWPORT_PROPERTIES = {"shadow_type": Gtk.ShadowType.IN}
