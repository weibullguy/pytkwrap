EXPECTED_FILECHOOSERBUTTON_HANDLER_IDS = {"file-set": -1}
EXPECTED_FILECHOOSERBUTTON_METHODS = [
    "get_title",
    "get_width_chars",
    "set_title",
    "set_width_chars",
]
EXPECTED_FILECHOOSERBUTTON_PROPERTIES = {
    "dialog": None,
    "title": "Select a File",
    "width_chars": -1,
}

EXPECTED_FILECHOOSERNATIVE_METHODS = [
    "get_accept_label",
    "get_cancel_label",
    "set_accept_label",
    "set_cancel_label",
]
EXPECTED_FILECHOOSERNATIVE_PROPERTIES = {"accept_label": None, "cancel_label": None}

EXPECTED_FILECHOOSERWIDGET_HANDLER_IDS = {
    "desktop-folder": -1,
    "down-folder": -1,
    "home-folder": -1,
    "location-popup": -1,
    "location-popup-on-paste": -1,
    "location-toggle-popup": -1,
    "places-shortcut": -1,
    "quick-bookmark": -1,
    "recent-shortcut": -1,
    "search-shortcut": -1,
    "show-hidden": -1,
    "up-folder": -1,
}
EXPECTED_FILECHOOSERWIDGET_PROPERTIES = {"search_mode": False}

EXPECTED_FILEFILTER_METHODS = [
    "add_custom",
    "add_mime_type",
    "add_pattern",
    "add_pixbuf_formats",
    "filter",
    "get_name",
    "get_needed",
    "set_name",
    "to_gvariant",
]

EXPECTED_RECENTFILTER_METHODS = [
    "add_age",
    "add_application",
    "add_custom",
    "add_group",
    "add_mime_type",
    "add_pattern",
    "add_pixbuf_formats",
    "filter",
    "get_name",
    "get_needed",
    "set_name",
]

EXPECTED_RECENTMANAGER_HANDLER_IDS = {"changed": -1}
EXPECTED_RECENTMANAGER_METHODS = [
    "add_full",
    "add_item",
    "get_items",
    "has_item",
    "lookup_item",
    "move_item",
    "purge_items",
    "remove_item",
]
