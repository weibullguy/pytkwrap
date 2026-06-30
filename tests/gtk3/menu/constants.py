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

EXPECTED_CHECKMENUITEM_HANDLER_IDS = {"toggled": -1}
EXPECTED_CHECKMENUITEM_METHODS = [
    "get_active",
    "get_draw_as_radio",
    "get_inconsistent",
    "set_active",
    "set_draw_as_radio",
    "set_inconsistent",
    "toggled",
]
EXPECTED_CHECKMENUITEM_PROPERTIES = {
    "active": False,
    "draw_as_radio": False,
    "inconsistent": False,
}

EXPECTED_MENU_HANDLER_IDS = {"move-scroll": -1, "popped-up": -1}
EXPECTED_MENU_METHODS = [
    "attach",
    "attach_to_widget",
    "detach",
    "get_accel_group",
    "get_accel_path",
    "get_active",
    "get_attach_widget",
    "get_monitor",
    "get_reserve_toggle_size",
    "place_on_monitor",
    "popdown",
    "popup_at_pointer",
    "popup_at_rect",
    "popup_at_widget",
    "reorder_child",
    "reposition",
    "set_accel_group",
    "set_accel_path",
    "set_active",
    "set_monitor",
    "set_reserve_toggle_size",
    "set_screen",
]
EXPECTED_MENU_PROPERTIES = {
    "accel_group": None,
    "accel_path": None,
    "active": -1,
    "anchor_hints": (
        Gdk.AnchorHints.FLIP_X
        | Gdk.AnchorHints.FLIP_Y
        | Gdk.AnchorHints.SLIDE_X
        | Gdk.AnchorHints.SLIDE_Y
        | Gdk.AnchorHints.RESIZE_X
        | Gdk.AnchorHints.RESIZE_Y
        | Gdk.AnchorHints.FLIP
        | Gdk.AnchorHints.SLIDE
        | Gdk.AnchorHints.RESIZE
    ),
    "attach_widget": None,
    "menu_type_hint": Gdk.WindowTypeHint.POPUP_MENU,
    "monitor": -1,
    "rect_anchor_dx": 0,
    "rect_anchor_dy": 0,
    "reserve_toggle_size": True,
}

EXPECTED_MENUBUTTON_METHODS = [
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
EXPECTED_MENUBUTTON_PROPERTIES = {
    "align_widget": None,
    "direction": Gtk.ArrowType.DOWN,
    "menu_model": None,
    "popover": None,
    "popup": None,
    "use_popover": True,
}

EXPECTED_MENUITEM_HANDLER_IDS = {
    "activate": -1,
    "activate-item": -1,
    "deselect": -1,
    "select": -1,
    "toggle-size-allocate": -1,
    "toggle-size-request": -1,
}
EXPECTED_MENUITEM_METHODS = [
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
EXPECTED_MENUITEM_PROPERTIES = {
    "accel_path": None,
    "label": "",
    "submenu": None,
    "use_underline": False,
}

EXPECTED_MENUSHELL_HANDLER_IDS = {
    "activate-current": -1,
    "cancel": -1,
    "cycle-focus": -1,
    "deactivate": -1,
    "insert": -1,
    "move-current": -1,
    "move-selected": -1,
    "selection-done": -1,
}
EXPECTED_MENUSHELL_METHODS = [
    "activate_item",
    "append",
    "bind_model",
    "cancel",
    "deactivate",
    "deselect",
    "get_parent_shell",
    "get_selected_item",
    "get_take_focus",
    "insert",
    "prepend",
    "select_first",
    "select_item",
    "set_take_focus",
]
EXPECTED_MENUSHELL_PROPERTIES = {"take_focus": True}

EXPECTED_POPOVERMENU_METHODS = ["open_submenu"]
EXPECTED_POPOVERMENU_PROPERTIES = {"visible_submenu": None}

EXPECTED_RADIOMENUITEM_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIOMENUITEM_METHODS = ["get_group", "join_group", "set_group"]
EXPECTED_RADIOMENUITEM_PROPERTIES = {"group": None}

EXPECTED_RECENTCHOOSERMENU_METHODS = ["get_show_numbers", "set_show_numbers"]
EXPECTED_RECENTCHOOSERMENU_PROPERTIES = {"show_numbers": False}
