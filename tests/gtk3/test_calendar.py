"""Test module for the GTK3Calendar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import date

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.calendar import GTK3Calendar

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


@pytest.mark.order(3)
class TestGTK3Calendar(BaseGTK3WidgetTests):
    """Test class for the GTK3Calendar class."""

    widget_class = GTK3Calendar
    expected_attributes = [
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
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = {
        "day-selected": -1,
        "day-selected-double-click": -1,
        "destroy": -1,
        "direction-changed": -1,
        "hide": -1,
        "keynav-failed": -1,
        "map": -1,
        "mnemonic-activate": -1,
        "month-changed": -1,
        "move-focus": -1,
        "next-month": -1,
        "next-year": -1,
        "notify": -1,
        "prev-month": -1,
        "prev-year": -1,
        "query-tooltip": -1,
        "realize": -1,
        "show": -1,
        "state-flags-changed": -1,
        "unmap": -1,
        "unrealize": -1,
    }
    expected_properties = {
        "can_default": False,
        "can_focus": False,
        "day": 0,
        "detail_height_rows": 0,
        "detail_width_chars": 0,
        "focus_on_click": True,
        "halign": Gtk.Align.FILL,
        "has_default": False,
        "has_focus": False,
        "has_tooltip": False,
        "height_request": -1,
        "hexpand": False,
        "hexpand_set": False,
        "is_focus": False,
        "margin": 0,
        "margin_bottom": 0,
        "margin_end": 0,
        "margin_start": 0,
        "margin_top": 0,
        "month": 0,
        "name": "pytkwrap GTK3 widget",
        "no_month_change": False,
        "opacity": 1.0,
        "parent": None,
        "receives_default": False,
        "scale_factor": 1,
        "sensitive": True,
        "show_day_names": True,
        "show_details": True,
        "show_heading": True,
        "show_week_numbers": False,
        "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
        "tooltip_text": "Missing tooltip, please file an issue to have one added.",
        "valign": Gtk.Align.FILL,
        "vexpand": False,
        "vexpand_set": False,
        "visible": False,
        "width_request": -1,
        "window": None,
        "year": 0,
    }

    def wrong_type_error_handler(self, message):
        """Return a WrongTypeError with the given message."""
        assert "GTK3Calendar.do_set_value(): Wrong type for value" in message

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current date."""
        dut = self.make_dut()
        print(dut.do_get_value())
        assert dut.do_get_value() == date.today()

    @pytest.mark.unit
    def test_do_set_value(self):
        """Should set the current date."""
        dut = self.make_dut()
        dut.do_set_value(date(2020, 1, 1))

        assert dut.do_get_value() == date(2020, 1, 1)

    @pytest.mark.unit
    def test_do_set_value_tuple(self):
        """Should set the current date."""
        dut = self.make_dut()
        dut.do_set_value((2020, 1, 1))

        assert dut.do_get_value() == date(2020, 1, 1)

    @pytest.mark.unit
    def test_do_set_value_bool(self):
        """Should raise a WrongTypeError and send a do_log_error message when passed a
        bool."""
        dut = self.make_dut()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(True)

    @pytest.mark.unit
    def test_do_set_value_float(self):
        """Should raise a WrongTypeError and send a do_log_error message when passed a
        float."""
        dut = self.make_dut()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(14.92)

    @pytest.mark.unit
    def test_do_set_value_int(self):
        """Should raise a WrongTypeError and send a do_log_error message when passed a
        int."""
        dut = self.make_dut()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(1492)

    @pytest.mark.unit
    def test_do_set_value_str(self):
        """Should raise a WrongTypeError and send a do_log_error message when passed a
        string."""
        dut = self.make_dut()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value("1492")

    @pytest.mark.unit
    def test_do_set_value_none(self):
        """Should raise a WrongTypeError and send a do_log_error message when passed
        None."""
        dut = self.make_dut()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(None)
