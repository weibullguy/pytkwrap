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
from .test_constants import (
    EXPECTED_CALENDAR_HANDLER_IDS,
    EXPECTED_CALENDAR_METHODS,
    EXPECTED_CALENDAR_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.order(3)
class TestGTK3Calendar(BaseGTK3WidgetTests):
    """Test class for the GTK3Calendar class."""

    widget_class = GTK3Calendar
    expected_attributes = EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CALENDAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_CALENDAR_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_CALENDAR_PROPERTIES

    def wrong_type_error_handler(self, message):
        """Return a WrongTypeError with the given message."""
        assert "GTK3Calendar.do_set_value(): Wrong type for value" in message

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current date."""
        dut = self.make_dut()

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
