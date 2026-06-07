"""Test module for the GTK3Calendar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import date, datetime

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io import GTK3Calendar
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests
from .test_constants import (
    EXPECTED_CALENDAR_ATTRIBUTES,
    EXPECTED_CALENDAR_HANDLER_IDS,
    EXPECTED_CALENDAR_METHODS,
    EXPECTED_CALENDAR_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.order(3)
class TestGTK3Calendar(BaseGTK3DataWidgetTests):
    """Test class for the GTK3Calendar class."""

    widget_class = GTK3Calendar
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_CALENDAR_ATTRIBUTES
    )
    expected_get_value = [
        [date.today(), date.today()],
    ]
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CALENDAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_CALENDAR_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_CALENDAR_PROPERTIES
    expected_set_value = [
        [date(2020, 1, 1), date(2020, 1, 1)],
        [(2020, 1, 1), date(2020, 1, 1)],
    ]
    expected_set_value_wrong_types = [
        True,
        14.92,
        1492,
        "1492",
        None,
    ]

    def mock_handler(self, package):
        """Mock handler for on_changed() calls."""
        assert isinstance(package, dict)
        assert package == {-1: date.today()}

    def wrong_type_error_handler(self, message):
        """Return a WrongTypeError with the given message."""
        assert "GTK3Calendar.do_set_value(): Wrong type for value" in message

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("default_value") == date.today()
        assert dut.do_get_attribute("edit_signal") == [
            "day-selected",
            "month-changed",
            "next-month",
            "next-year",
            "prev-month",
            "prev-year",
        ]

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=datetime.strptime("2023-10-14", "%Y-%m-%d"),
                edit_signal="calendar_changed",
            )
        )

        assert dut.do_get_attribute("default_value") == datetime.strptime(
            "2023-10-14", "%Y-%m-%d"
        )
        assert dut.do_get_attribute("edit_signal") == "calendar_changed"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("day") == 0
        assert dut.do_get_property("detail_height_rows") == 0
        assert dut.do_get_property("detail_width_chars") == 0
        assert dut.do_get_property("month") == 0
        assert not dut.do_get_property("no_month_change")
        assert dut.do_get_property("show_day_names")
        assert dut.do_get_property("show_details")
        assert dut.do_get_property("show_heading")
        assert not dut.do_get_property("show_week_numbers")
        assert dut.do_get_property("year") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                day=1,
                detail_height_rows=2,
                detail_width_chars=25,
                month=6,
                no_month_change=True,
                show_day_names=False,
                show_details=False,
                show_heading=False,
                show_week_numbers=True,
                year=2026,
            )
        )

        assert dut.do_get_property("day") == 1
        assert dut.do_get_property("detail_height_rows") == 2
        assert dut.do_get_property("detail_width_chars") == 25
        assert dut.do_get_property("month") == 6
        assert dut.do_get_property("no_month_change")
        assert not dut.do_get_property("show_day_names")
        assert not dut.do_get_property("show_details")
        assert not dut.do_get_property("show_heading")
        assert dut.do_get_property("show_week_numbers")
        assert dut.do_get_property("year") == 2026

    @pytest.mark.unit
    def test_do_set_edit_signal_callbacks(self):
        """Should set the callback function for a GTK3Calendar edit signal."""
        dut = self.make_dut()
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], self.mock_callback)

        assert dut.dic_handler_id["day-selected"] != -1
        assert dut.dic_handler_id["month-changed"] != -1
        assert dut.dic_handler_id["next-month"] != -1
        assert dut.dic_handler_id["next-year"] != -1
        assert dut.dic_handler_id["prev-month"] != -1
        assert dut.dic_handler_id["prev-year"] != -1

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the value of the GTK3Calendar."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.dic_attributes["send_topic"] = "calendar_changed"
        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: date.today()})

        assert dut.do_get_value() == date.today()

        pub.unsubscribe(dut.do_update, "rootTopic")

    @pytest.mark.unit
    def test_on_changed(self):
        """Should be called when the GTK3Calendar value changes."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.dic_attributes["send_topic"] = "calendar_changed"
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("day-selected")

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
