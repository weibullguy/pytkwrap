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
from gi.repository import Gdk, Gtk

EXPECTED_ICONVIEW_HANDLER_IDS = {
    "activate-cursor-item": -1,
    "item-activated": -1,
    "move-cursor": -1,
    "select-all": -1,
    "select-cursor-item": -1,
    "selection-changed": -1,
    "toggle-cursor-item": -1,
    "unselect-all": -1,
}
EXPECTED_ICONVIEW_METHODS = [
    "convert_widget_to_bin_window_coords",
    "create_drag_icon",
    "enable_model_drag_dest",
    "enable_model_drag_source",
    "get_activate_on_single_click",
    "get_cell_rect",
    "get_column_spacing",
    "get_columns",
    "get_cursor",
    "get_dest_item_at_pos",
    "get_drag_dest_item",
    "get_item_at_pos",
    "get_item_column",
    "get_item_orientation",
    "get_item_padding",
    "get_item_row",
    "get_item_width",
    "get_margin",
    "get_markup_column",
    "get_model",
    "get_path_at_pos",
    "get_pixbuf_column",
    "get_reorderable",
    "get_row_spacing",
    "get_selected_items",
    "get_selection_mode",
    "get_spacing",
    "get_text_column",
    "get_tooltip_column",
    "get_tooltip_context",
    "get_visible_range",
    "item_activated",
    "path_is_selected",
    "scroll_to_path",
    "select_all",
    "select_path",
    "set_activate_on_single_click",
    "set_columns",
    "set_cursor",
    "set_drag_dest_item",
    "set_item_orientation",
    "set_item_padding",
    "set_item_width",
    "set_margin",
    "set_markup_column",
    "set_model",
    "set_pixbuf_column",
    "set_reorderable",
    "set_row_spacing",
    "set_selection_mode",
    "set_spacing",
    "set_text_column",
    "set_tooltip_cell",
    "set_tooltip_column",
    "unselect_all",
    "unselect_path",
    "unset_model_drag_dest",
    "unset_model_drag_source",
]
EXPECTED_ICONVIEW_PROPERTIES = {
    "activate_on_single_click": False,
    "cell_area": None,
    "column_spacing": 6,
    "columns": -1,
    "item_orientation": Gtk.Orientation.VERTICAL,
    "item_padding": 6,
    "item_width": -1,
    "markup_column": -1,
    "model": None,
    "pixbuf_column": -1,
    "reorderable": False,
    "row_spacing": 6,
    "selection_mode": Gtk.SelectionMode.SINGLE,
    "spacing": 0,
    "text_column": -1,
    "tooltip_column": -1,
}
