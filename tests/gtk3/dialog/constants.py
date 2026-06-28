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

EXPECTED_ABOUTDIALOG_HANDLER_IDS = {"activate-link": -1}
EXPECTED_ABOUTDIALOG_METHODS = [
    "add_credit_section",
    "get_artists",
    "get_authors",
    "get_comments",
    "get_copyright",
    "get_documenters",
    "get_license",
    "get_license_type",
    "get_logo",
    "get_logo_icon_name",
    "get_program_name",
    "get_translator_credits",
    "get_version",
    "get_website",
    "get_website_label",
    "get_wrap_license",
    "set_artists",
    "set_authors",
    "set_comments",
    "set_copyright",
    "set_documenters",
    "set_license",
    "set_license_type",
    "set_logo",
    "set_logo_icon_name",
    "set_program_name",
    "set_translator_credits",
    "set_version",
    "set_website",
    "set_website_label",
    "set_wrap_license",
]
EXPECTED_ABOUTDIALOG_PROPERTIES = {
    "artists": [],
    "authors": [],
    "comments": None,
    "copyright": None,
    "documenters": [],
    "license": None,
    "license_type": Gtk.License.UNKNOWN,
    "logo": None,
    "logo_icon_name": "image-missing",
    "program_name": None,
    "translator_credits": None,
    "version": None,
    "website": None,
    "website_label": None,
    "wrap_license": False,
}

EXPECTED_APPCHOOSERDIALOG_METHODS = ["get_heading", "get_widget", "set_heading"]
EXPECTED_APPCHOOSERDIALOG_PROPERTIES = {"gfile": None, "heading": None}

EXPECTED_DIALOG_HANDLER_IDS = {"close": -1, "response": -1}
EXPECTED_DIALOG_METHODS = [
    "add_action_widget",
    "add_button",
    "add_buttons",
    "get_action_area",
    "get_content_area",
    "get_header_bar",
    "get_response_for_widget",
    "get_widget_for_response",
    "response",
    "run",
    "set_alternative_button_order_from_array",
    "set_default_response",
    "set_response_sensitive",
]
EXPECTED_DIALOG_PROPERTIES = {"use_header_bar": -1}

EXPECTED_MESSAGEDIALOG_METHODS = [
    "format_secondary_markup",
    "format_secondary_text",
    "get_message_area",
    "set_markup",
]
EXPECTED_MESSAGEDIALOG_PROPERTIES = {
    "buttons": Gtk.ButtonsType.NONE,
    "message_area": None,
    "message_type": Gtk.MessageType.INFO,
    "secondary_text": None,
    "secondary_use_markup": False,
    "text": "",
    "use_markup": False,
}
