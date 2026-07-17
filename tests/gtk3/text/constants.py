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

EXPECTED_ENTRYBUFFER_HANDLER_IDS = {"deleted-text": -1, "inserted-text": -1}
EXPECTED_ENTRYBUFFER_METHODS = [
    "delete_text",
    "emit_deleted_text",
    "emit_inserted_text",
    "get_bytes",
    "get_length",
    "get_max_length",
    "get_text",
    "insert_text",
    "set_max_length",
    "set_text",
]
EXPECTED_ENTRYBUFFER_PROPERTIES = {"max_length": 0, "text": ""}
