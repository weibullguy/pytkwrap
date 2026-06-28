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

EXPECTED_FIXED_METHODS = ["move", "put"]

EXPECTED_FLOWBOX_HANDLER_IDS = {
    "activate-cursor-child": -1,
    "child-activated": -1,
    "move-cursor": -1,
    "select-all": -1,
    "selected-children-changed": -1,
    "toggle-cursor-child": -1,
    "unselect-all": -1,
}
EXPECTED_FLOWBOX_METHODS = [
    "bind_model",
    "get_activate_on_single_click",
    "get_child_at_index",
    "get_child_at_pos",
    "get_column_spacing",
    "get_homogeneous",
    "get_max_children_per_line",
    "get_min_children_per_line",
    "get_row_spacing",
    "get_selected_children",
    "get_selection_mode",
    "insert",
    "invalidate_filter",
    "invalidate_sort",
    "select_all",
    "select_child",
    "selected_foreach",
    "set_activate_on_single_click",
    "set_column_spacing",
    "set_filter_func",
    "set_hadjustment",
    "set_homogeneous",
    "set_max_children_per_line",
    "set_min_children_per_line",
    "set_row_spacing",
    "set_selection_mode",
    "set_sort_func",
    "set_vadjustment",
    "unselect_all",
    "unselect_child",
]
EXPECTED_FLOWBOX_PROPERTIES = {
    "activate_on_single_click": True,
    "column_spacing": 0,
    "homogeneous": False,
    "max_children_per_line": 7,
    "min_children_per_line": 0,
    "row_spacing": 0,
    "selection_mode": Gtk.SelectionMode.SINGLE,
}

EXPECTED_GRID_ATTRIBUTES = {"n_columns": 1, "n_rows": 1}
EXPECTED_GRID_METHODS = [
    "attach",
    "attach_next_to",
    "get_baseline_row",
    "get_child_at",
    "get_column_homogeneous",
    "get_column_spacing",
    "get_row_baseline_position",
    "get_row_homogeneous",
    "get_row_spacing",
    "insert_column",
    "insert_row",
    "remove_column",
    "remove_row",
    "set_baseline_row",
    "set_column_homogeneous",
    "set_column_spacing",
    "set_row_baseline_position",
    "set_row_homogeneous",
    "set_row_spacing",
]
EXPECTED_GRID_PROPERTIES = {
    "baseline_row": 0,
    "column_homogeneous": False,
    "column_spacing": 0,
    "row_homogeneous": False,
    "row_spacing": 0,
}

EXPECTED_LAYOUT_METHODS = [
    "get_bin_window",
    "get_size",
    "move",
    "put",
    "set_size",
]
EXPECTED_LAYOUT_PROPERTIES = {"height": 100, "width": 100}
