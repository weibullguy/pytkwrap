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

EXPECTED_TEXTBUFFER_HANDLER_IDS = {
    "apply-tag": -1,
    "begin-user-action": -1,
    "changed": -1,
    "delete-range": -1,
    "end-user-action": -1,
    "insert-child-anchor": -1,
    "insert-pixbuf": -1,
    "insert-text": -1,
    "mark-deleted": -1,
    "mark-set": -1,
    "modified-changed": -1,
    "paste-done": -1,
    "remove-tag": -1,
}
EXPECTED_TEXTBUFFER_METHODS = [
    "add_mark",
    "add_selection_clipboard",
    "apply_tag",
    "apply_tag_by_name",
    "backspace",
    "begin_user_action",
    "copy_clipboard",
    "create_child_anchor",
    "create_mark",
    "create_tag",
    "cut_clipboard",
    "delete",
    "delete_interactive",
    "delete_mark",
    "delete_mark_by_name",
    "delete_selection",
    "deserialize",
    "deserialize_get_can_create_tags",
    "deserialize_set_can_create_tags",
    "end_user_action",
    "get_bounds",
    "get_char_count",
    "get_copy_target_list",
    "get_deserialize_formats",
    "get_end_iter",
    "get_has_selection",
    "get_insert",
    "get_iter_at_child_anchor",
    "get_iter_at_line",
    "get_iter_at_line_index",
    "get_iter_at_line_offset",
    "get_iter_at_mark",
    "get_iter_at_offset",
    "get_line_count",
    "get_mark",
    "get_modified",
    "get_paste_target_list",
    "get_selection_bound",
    "get_selection_bounds",
    "get_serialize_formats",
    "get_start_iter",
    "get_tag_table",
    "get_text",
    "insert",
    "insert_at_cursor",
    "insert_child_anchor",
    "insert_interactive",
    "insert_interactive_at_cursor",
    "insert_markup",
    "insert_pixbuf",
    "insert_range",
    "insert_range_interactive",
    "insert_with_tags",
    "insert_with_tags_by_name",
    "move_mark",
    "move_mark_by_name",
    "paste_clipboard",
    "place_cursor",
    "register_deserialize_format",
    "register_deserialize_tagset",
    "register_serialize_format",
    "register_serialize_tagset",
    "remove_all_tags",
    "remove_selection_clipboard",
    "remove_tag",
    "remove_tag_by_name",
    "select_range",
    "serialize",
    "set_modified",
    "set_text",
    "unregister_deserialize_format",
    "unregister_serialize_format",
]
EXPECTED_TEXTBUFFER_PROPERTIES = {"tag_table": None, "text": ""}

EXPECTED_TEXTMARK_METHODS = [
    "get_buffer",
    "get_deleted",
    "get_left_gravity",
    "get_name",
    "get_visible",
    "set_visible",
]
EXPECTED_TEXTMARK_PROPERTIES = {"left_gravity": False, "name": None}
