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

EXPECTED_ENTRYCOMPLETION_HANDLER_IDS = {
    "action-activated": -1,
    "cursor-on-match": -1,
    "insert-prefix": -1,
    "match-selected": -1,
    "no-matches": -1,
}
EXPECTED_ENTRYCOMPLETION_METHODS = [
    "complete",
    "compute_prefix",
    "delete_action",
    "get_completion_prefix",
    "get_entry",
    "get_inline_completion",
    "get_inline_selection",
    "get_minimum_key_length",
    "get_model",
    "get_popup_completion",
    "get_popup_set_width",
    "get_popup_single_match",
    "get_text_column",
    "insert_action_markup",
    "insert_action_text",
    "insert_prefix",
    "set_inline_completion",
    "set_inline_selection",
    "set_match_func",
    "set_minimum_key_length",
    "set_model",
    "set_popup_completion",
    "set_popup_set_width",
    "set_popup_single_match",
    "set_text_column",
]
EXPECTED_ENTRYCOMPLETION_PROPERTIES = {
    "cell_area": None,
    "inline_completion": False,
    "inline_selection": False,
    "minimum_key_length": 1,
    "model": None,
    "popup_completion": True,
    "popup_set_width": True,
    "popup_single_match": True,
    "text_column": -1,
}
