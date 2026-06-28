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

EXPECTED_APPCHOOSERBUTTON_HANDLER_IDS = {"custom-item-activated": -1}
EXPECTED_APPCHOOSERBUTTON_METHODS = [
    "append_custom_item",
    "append_separator",
    "get_heading",
    "get_show_default_item",
    "get_show_dialog_item",
    "set_active_custom_item",
    "set_heading",
    "set_show_default_item",
    "set_show_dialog_item",
]
EXPECTED_APPCHOOSERBUTTON_PROPERTIES = {
    "heading": None,
    "show_default_item": False,
    "show_dialog_item": False,
}

EXPECTED_BUTTON_HANDLER_IDS = {"activate": -1, "check-resize": -1, "clicked": -1}
EXPECTED_BUTTON_METHODS = [
    "clicked",
    "get_always_show_image",
    "get_event_window",
    "get_image",
    "get_image_position",
    "get_label",
    "get_relief",
    "get_use_underline",
    "set_always_show_image",
    "set_image",
    "set_image_position",
    "set_label",
    "set_relief",
    "set_use_underline",
]
EXPECTED_BUTTON_PROPERTIES = {
    "always_show_image": False,
    "image": None,
    "image_position": Gtk.PositionType.LEFT,
    "label": "...",
    "relief": Gtk.ReliefStyle.NORMAL,
    "use_underline": False,
}

EXPECTED_RADIOBUTTON_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIOBUTTON_METHODS = [
    "get_group",
    "join_group",
    "set_group",
]
EXPECTED_RADIOBUTTON_PROPERTIES = {"group": None}

EXPECTED_SCALEBUTTON_ATTRIBUTES = {
    "default_value": 0.0,
    "edit_signal": "value-changed",
}
EXPECTED_SCALEBUTTON_HANDLER_IDS = {"popdown": -1, "popup": -1, "value-changed": -1}
EXPECTED_SCALEBUTTON_METHODS = [
    "get_adjustment",
    "get_minus_button",
    "get_plus_button",
    "get_popup",
    "get_value",
    "set_adjustment",
    "set_icons",
    "set_value",
]
EXPECTED_SCALEBUTTON_PROPERTIES = {
    "adjustment": None,
    "icons": [],
    "size": Gtk.IconSize.SMALL_TOOLBAR,
    "value": 0.0,
}

EXPECTED_TOGGLEBUTTON_ATTRIBUTES = {"default_value": False, "edit_signal": "toggled"}
EXPECTED_TOGGLEBUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLEBUTTON_METHODS = [
    "get_active",
    "get_inconsistent",
    "get_mode",
    "set_active",
    "set_inconsistent",
    "set_mode",
    "toggled",
]
EXPECTED_TOGGLEBUTTON_PROPERTIES = {
    "active": False,
    "draw_indicator": False,
    "inconsistent": False,
    "use_underline": False,
}

EXPECTED_VOLUMEBUTTON_PROPERTIES = {"use_symbolic": True}
