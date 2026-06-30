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

EXPECTED_NOTEBOOK_HANDLER_IDS = {
    "change-current-page": -1,
    "create-window": -1,
    "focus-tab": -1,
    "move-focus-out": -1,
    "page-added": -1,
    "page-removed": -1,
    "page-reordered": -1,
    "reorder-tab": -1,
    "select-page": -1,
    "switch-page": -1,
}
EXPECTED_NOTEBOOK_METHODS = [
    "append_page",
    "append_page_menu",
    "detach_tab",
    "get_action_widget",
    "get_current_page",
    "get_group_name",
    "get_menu_label",
    "get_menu_label_text",
    "get_n_pages",
    "get_nth_page",
    "get_scrollable",
    "get_show_border",
    "get_show_tabs",
    "get_tab_detachable",
    "get_tab_hborder",
    "get_tab_label",
    "get_tab_label_text",
    "get_tab_pos",
    "get_tab_reorderable",
    "get_tab_vborder",
    "insert_page",
    "insert_page_menu",
    "next_page",
    "page_num",
    "popup_disable",
    "popup_enable",
    "prepend_page",
    "prepend_page_menu",
    "prev_page",
    "remove_page",
    "reorder_child",
    "set_action_widget",
    "set_current_page",
    "set_group_name",
    "set_menu_label",
    "set_menu_label_text",
    "set_scrollable",
    "set_show_border",
    "set_show_tabs",
    "set_tab_detachable",
    "set_tab_label",
    "set_tab_label_text",
    "set_tab_pos",
    "set_tab_reorderable",
]
EXPECTED_NOTEBOOK_PROPERTIES = {
    "enable_popup": False,
    "group_name": None,
    "page": -1,
    "scrollable": False,
    "show_border": True,
    "show_tabs": True,
    "tab_pos": Gtk.PositionType.TOP,
}
