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

EXPECTED_COLORBUTTON_ATTRIBUTES = {"default_value": None, "edit_signal": "color-set"}
EXPECTED_COLORBUTTON_HANDLER_IDS = {"color-set": -1}
EXPECTED_COLORBUTTON_METHODS = [
    "get_title",
    "set_title",
]
EXPECTED_COLORBUTTON_PROPERTIES = {
    "alpha": 65535,
    "rgba": None,
    "show_editor": False,
    "title": "Pick a Color",
    "use_alpha": True,
}

EXPECTED_COLORCHOOSERDIALOG_PROPERTIES = {"show_editor": False}

EXPECTED_COLORCHOOSERWIDGET_PROPERTIES = {"show_editor": False}

EXPECTED_COLORSELECTION_HANDLER_IDS = {"color-changed": -1}
EXPECTED_COLORSELECTION_METHODS = [
    "get_current_alpha",
    "get_current_rgba",
    "get_has_opacity_control",
    "get_has_palette",
    "get_previous_alpha",
    "get_previous_rgba",
    "is_adjusting",
    "set_current_alpha",
    "set_current_rgba",
    "set_has_opacity_control",
    "set_has_palette",
    "set_previous_alpha",
    "set_previous_rgba",
]
EXPECTED_COLORSELECTION_PROPERTIES = {
    "current_alpha": 65535,
    "current_rgba": None,
    "has_opacity_control": False,
    "has_palette": False,
}

EXPECTED_COLORSELECTIONDIALOG_METHODS = ["get_color_selection"]
EXPECTED_COLORSELECTIONDIALOG_PROPERTIES = {
    "cancel_button": Gtk.Widget,
    "color_selection": Gtk.Widget,
    "help_button": Gtk.Widget,
    "ok_button": Gtk.Widget,
}
