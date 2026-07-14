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

EXPECTED_ACTIONBAR_METHODS = [
    "get_center_widget",
    "pack_end",
    "pack_start",
    "set_center_widget",
]

EXPECTED_HEADERBAR_METHODS = [
    "get_custom_title",
    "get_decoration_layout",
    "get_has_subtitle",
    "get_show_close_button",
    "get_subtitle",
    "get_title",
    "pack_end",
    "pack_start",
    "set_custom_title",
    "set_decoration_layout",
    "set_has_subtitle",
    "set_show_close_button",
    "set_subtitle",
    "set_title",
]
EXPECTED_HEADERBAR_PROPERTIES = {
    "custom_title": None,
    "decoration_layout": None,
    "decoration_layout_set": False,
    "has_subtitle": True,
    "show_close_button": False,
    "spacing": 6,
    "subtitle": None,
    "title": None,
}

EXPECTED_INFOBAR_HANDLER_IDS = {"close": -1, "response": -1}
EXPECTED_INFOBAR_METHODS = [
    "add_action_widget",
    "add_button",
    "get_action_area",
    "get_content_area",
    "get_message_type",
    "get_revealed",
    "get_show_close_button",
    "response",
    "set_default_response",
    "set_message_type",
    "set_response_sensitive",
    "set_revealed",
    "set_show_close_button",
]
EXPECTED_INFOBAR_PROPERTIES = {
    "message_type": Gtk.MessageType.INFO,
    "revealed": True,
    "show_close_button": False,
}

EXPECTED_LEVELBAR_HANDLER_IDS = {"offset-changed": -1}
EXPECTED_LEVELBAR_METHODS = [
    "add_offset_value",
    "get_inverted",
    "get_max_value",
    "get_min_value",
    "get_mode",
    "get_offset_value",
    "get_value",
    "remove_offset_value",
    "set_inverted",
    "set_max_value",
    "set_min_value",
    "set_mode",
    "set_value",
]
EXPECTED_LEVELBAR_PROPERTIES = {
    "inverted": False,
    "max_value": 1.0,
    "min_value": 0.0,
    "mode": Gtk.LevelBarMode.CONTINUOUS,
    "value": 0.0,
}

EXPECTED_PLACESSIDEBAR_HANDLER_IDS = {
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
EXPECTED_PLACESSIDEBAR_METHODS = [
    "add_shortcut",
    "get_local_only",
    "get_location",
    "get_nth_bookmark",
    "get_open_flags",
    "get_show_desktop",
    "get_show_enter_location",
    "get_show_other_locations",
    "get_show_recent",
    "get_show_starred_location",
    "get_show_trash",
    "list_shortcuts",
    "remove_shortcut",
    "set_drop_targets_visible",
    "set_local_only",
    "set_location",
    "set_open_flags",
    "set_show_desktop",
    "set_show_enter_location",
    "set_show_other_locations",
    "set_show_recent",
    "set_show_starred_location",
    "set_show_trash",
]
EXPECTED_PLACESSIDEBAR_PROPERTIES = {
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

EXPECTED_PROGRESSBAR_ATTRIBUTES = {"default_value": 0.0, "data_type": float}
EXPECTED_PROGRESSBAR_METHODS = [
    "get_ellipsize",
    "get_fraction",
    "get_inverted",
    "get_pulse_step",
    "get_show_text",
    "get_text",
    "pulse",
    "set_ellipsize",
    "set_fraction",
    "set_inverted",
    "set_pulse_step",
    "set_show_text",
    "set_text",
]
EXPECTED_PROGRESSBAR_PROPERTIES = {
    "ellipsize": Pango.EllipsizeMode.NONE,
    "fraction": 0.0,
    "inverted": False,
    "pulse_step": 0.1,
    "show_text": False,
    "text": None,
}

EXPECTED_SEARCHBAR_METHODS = [
    "connect_entry",
    "get_search_mode",
    "get_show_close_button",
    "handle_event",
    "set_search_mode",
    "set_show_close_button",
]
EXPECTED_SEARCHBAR_PROPERTIES = {
    "search_mode_enabled": False,
    "show_close_button": False,
}

EXPECTED_STATUSBAR_HANDLER_IDS = {"text-popped": -1, "text-pushed": -1}
EXPECTED_STATUSBAR_METHODS = [
    "get_context_id",
    "get_message_area",
    "pop",
    "push",
    "remove",
    "remove_all",
]
