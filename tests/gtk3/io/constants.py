# Standard Library Imports
import sys
from datetime import date

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
from gi.repository import GObject, Gtk

EXPECTED_CALENDAR_ATTRIBUTES = {
    "default_value": date.today(),
    "edit_signal": [
        "day-selected",
        "month-changed",
        "next-month",
        "next-year",
        "prev-month",
        "prev-year",
    ],
}
EXPECTED_CALENDAR_HANDLER_IDS = {
    "day-selected": -1,
    "day-selected-double-click": -1,
    "month-changed": -1,
    "next-month": -1,
    "next-year": -1,
    "prev-month": -1,
    "prev-year": -1,
}
EXPECTED_CALENDAR_METHODS = [
    "clear_marks",
    "get_date",
    "get_day_is_marked",
    "get_detail_height_rows",
    "get_detail_width_chars",
    "get_display_options",
    "mark_day",
    "select_day",
    "select_month",
    "set_detail_func",
    "set_detail_height_rows",
    "set_detail_width_chars",
    "set_display_options",
    "unmark_day",
]
EXPECTED_CALENDAR_PROPERTIES = {
    "day": 0,
    "detail_height_rows": 0,
    "detail_width_chars": 0,
    "month": 0,
    "no_month_change": False,
    "show_day_names": True,
    "show_details": True,
    "show_heading": True,
    "show_week_numbers": False,
    "year": 0,
}

EXPECTED_COMBOBOX_ATTRIBUTES = {
    "column_types": [GObject.TYPE_STRING],
    "default_value": -1,
    "edit_signal": "changed",
}
EXPECTED_COMBOBOX_HANDLER_IDS = {
    "changed": -1,
    "editing-done": -1,
    "format-entry-text": -1,
    "move-active": -1,
    "popdown": -1,
    "popup": -1,
    "remove-widget": -1,
}
EXPECTED_COMBOBOX_METHODS = [
    "get_active",
    "get_active_id",
    "get_active_iter",
    "get_add_tearoffs",
    "get_button_sensitivity",
    "get_column_span_column",
    "get_entry_text_column",
    "get_has_entry",
    "get_id_column",
    "get_model",
    "get_popup_accessible",
    "get_popup_fixed_width",
    "get_row_span_column",
    "get_wrap_width",
    "popdown",
    "popup",
    "popup_for_device",
    "set_active",
    "set_active_id",
    "set_active_iter",
    "set_button_sensitivity",
    "set_column_span_column",
    "set_entry_text_column",
    "set_id_column",
    "set_model",
    "set_popup_fixed_width",
    "set_row_separator_func",
    "get_row_span_column",
    "set_wrap_width",
]
EXPECTED_COMBOBOX_PROPERTIES = {
    "active": -1,
    "active_id": None,
    "button_sensitivity": Gtk.SensitivityType.AUTO,
    "cell_area": None,
    "column_span_column": -1,
    "editing_canceled": False,
    "entry_text_column": -1,
    "has_entry": False,
    "has_frame": True,
    "id_column": -1,
    "model": None,
    "popup_fixed_width": True,
    "popup_shown": False,
    "row_span_column": -1,
    "wrap_width": 0,
}

EXPECTED_COMBOBOXTEXT_METHODS = [
    "append",
    "append_text",
    "get_active_text",
    "insert",
    "insert_text",
    "prepend",
    "prepend_text",
    "remove",
    "remove_all",
]

SIMPLE_TEST_LIST = [
    "Index 1",
    "Index 2",
    "Index 3",
]
COMPOUND_TEST_LIST = [
    ["This", "is", "a"],
    ["test", "of", "the"],
    ["ComboBox", "not", "simple"],
]
