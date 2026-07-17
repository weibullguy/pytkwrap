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

EXPECTED_CSSPROVIDER_HANDLER_IDS = {"parsing-error": -1}
EXPECTED_CSSPROVIDER_METHODS = [
    "load_from_data",
    "load_from_file",
    "load_from_path",
    "load_from_resource",
    "to_string",
]
