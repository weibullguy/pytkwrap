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
from gi.repository import Gtk, Pango

EXPECTED_MENUTOOLBUTTON_HANDLER_IDS = {"show-menu": -1}
EXPECTED_MENUTOOLBUTTON_METHODS = [
    "get_menu",
    "set_arrow_tooltip_markup",
    "set_arrow_tooltip_text",
    "set_menu",
]
EXPECTED_MENUTOOLBUTTON_PROPERTIES = {"menu": None}

EXPECTED_RADIOTOOLBUTTON_METHODS = ["get_group", "set_group"]
EXPECTED_RADIOTOOLBUTTON_PROPERTIES = {"group": None}

EXPECTED_SEPARATORTOOLITEM_METHODS = ["get_draw", "set_draw"]
EXPECTED_SEPARATORTOOLITEM_PROPERTIES = {"draw": True}

EXPECTED_TOGGLETOOLBUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLETOOLBUTTON_METHODS = ["get_active", "set_active"]
EXPECTED_TOGGLETOOLBUTTON_PROPERTIES = {"active": False}

EXPECTED_TOOLBAR_HANDLER_IDS = {
    "focus-home-or-end": -1,
    "orientation-changed": -1,
    "popup-context-menu": -1,
    "style-changed": -1,
}
EXPECTED_TOOLBAR_METHODS = [
    "get_drop_index",
    "get_icon_size",
    "get_item_index",
    "get_n_items",
    "get_nth_item",
    "get_relief_style",
    "get_show_arrow",
    "get_style",
    "insert",
    "set_drop_highlight_item",
    "set_icon_size",
    "set_show_arrow",
    "set_style",
    "unset_icon_size",
    "unset_style",
]
EXPECTED_TOOLBAR_PROPERTIES = {
    "icon_size": Gtk.IconSize.LARGE_TOOLBAR,
    "icon_size_set": False,
    "show_arrow": True,
    "toolbar_style": Gtk.ToolbarStyle.BOTH_HORIZ,
}

EXPECTED_TOOLBUTTON_HANDLER_IDS = {"clicked": -1}
EXPECTED_TOOLBUTTON_METHODS = [
    "get_icon_name",
    "get_icon_widget",
    "get_label",
    "get_label_widget",
    "get_use_underline",
    "set_icon_name",
    "set_icon_widget",
    "set_label",
    "set_label_widget",
    "set_use_underline",
]
EXPECTED_TOOLBUTTON_PROPERTIES = {
    "icon_name": None,
    "icon_widget": None,
    "label": None,
    "label_widget": None,
    "use_underline": False,
}

EXPECTED_TOOLITEM_HANDLER_IDS = {"create-menu-proxy": -1, "toolbar-reconfigured": -1}
EXPECTED_TOOLITEM_METHODS = [
    "get_ellipsize_mode",
    "get_expand",
    "get_homogeneous",
    "get_icon_size",
    "get_is_important",
    "get_orientation",
    "get_proxy_menu_item",
    "get_relief_style",
    "get_text_alignment",
    "get_text_orientation",
    "get_text_size_group",
    "get_toolbar_style",
    "get_use_drag_window",
    "get_visible_horizontal",
    "get_visible_vertical",
    "rebuild_menu",
    "retrieve_proxy_menu_item",
    "set_expand",
    "set_homogeneous",
    "set_is_important",
    "set_proxy_menu_item",
    "set_tooltip_markup",
    "set_tooltip_text",
    "set_use_drag_window",
    "set_visible_horizontal",
    "set_visible_vertical",
    "toolbar_reconfigured",
]
EXPECTED_TOOLITEM_PROPERTIES = {
    "is_important": False,
    "visible_horizontal": True,
    "visible_vertical": True,
}

EXPECTED_TOOLITEMGROUP_METHODS = [
    "get_collapsed",
    "get_drop_item",
    "get_ellipsize",
    "get_header_relief",
    "get_item_position",
    "get_label",
    "get_label_widget",
    "get_n_items",
    "get_nth_item",
    "insert",
    "set_collapsed",
    "set_ellipsize",
    "set_header_relief",
    "set_item_position",
    "set_label",
    "set_label_widget",
]
EXPECTED_TOOLITEMGROUP_PROPERTIES = {
    "collapsed": False,
    "ellipsize": Pango.EllipsizeMode.NONE,
    "header_relief": Gtk.ReliefStyle.NORMAL,
    "label": "",
    "label_widget": None,
}

EXPECTED_TOOLPALETTE_METHODS = [
    "add_drag_dest",
    "get_drag_item",
    "get_drop_group",
    "get_drop_item",
    "get_exclusive",
    "get_expand",
    "get_group_position",
    "get_icon_size",
    "get_style",
    "set_drag_source",
    "set_exclusive",
    "set_expand",
    "set_group_position",
    "set_icon_size",
    "set_style",
    "unset_icon_size",
    "unset_style",
]
EXPECTED_TOOLPALETTE_PROPERTIES = {
    "icon_size": Gtk.IconSize.SMALL_TOOLBAR,
    "icon_size_set": False,
    "toolbar_style": Gtk.ToolbarStyle.ICONS,
}
