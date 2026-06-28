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

EXPECTED_SHORTCUTSGROUP_PROPERTIES = {
    "accel_size_group": None,
    "title": "",
    "title_size_group": None,
    "view": None,
}

EXPECTED_SHORTCUTLABEL_METHODS = [
    "get_accelerator",
    "get_disabled_text",
    "set_accelerator",
    "set_disabled_text",
]
EXPECTED_SHORTCUTLABEL_PROPERTIES = {"accelerator": None, "disabled_text": None}


EXPECTED_SHORTCUTSSECTION_HANDLER_IDS = {"change-current-page": -1}
EXPECTED_SHORTCUTSSECTION_PROPERTIES = {
    "max_height": 15,
    "section_name": None,
    "title": None,
    "view_name": None,
}

EXPECTED_SHORTCUTSSHORTCUT_PROPERTIES = {
    "accel_size_group": None,
    "accelerator": None,
    "action_name": None,
    "direction": Gtk.TextDirection.NONE,
    "icon": None,
    "icon_set": False,
    "shortcut_type": Gtk.ShortcutType.ACCELERATOR,
    "subtitle": "",
    "subtitle_set": False,
    "title": "",
    "title_size_group": None,
}

EXPECTED_SHORTCUTSWINDOW_HANDLER_IDS = {"close": -1, "search": -1}
EXPECTED_SHORTCUTSWINDOW_PROPERTIES = {
    "section_name": "internal-search",
    "view_name": None,
}
