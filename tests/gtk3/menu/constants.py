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

EXPECTED_POPOVERMENU_METHODS = ["open_submenu"]
EXPECTED_POPOVERMENU_PROPERTIES = {"visible_submenu": None}

EXPECTED_RADIOMENUITEM_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIOMENUITEM_METHODS = ["get_group", "join_group", "set_group"]
EXPECTED_RADIOMENUITEM_PROPERTIES = {"group": None}
