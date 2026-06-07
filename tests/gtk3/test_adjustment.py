"""Test module for the GTK3Adjustment class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import date

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests
from .test_constants import (
    EXPECTED_ADJUSTMENT_ATTRIBUTES,
    EXPECTED_ADJUSTMENT_HANDLER_IDS,
    EXPECTED_ADJUSTMENT_METHODS,
    EXPECTED_ADJUSTMENT_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.order(3)
class TestGTK3Adjustment(BaseGTK3DataWidgetTests):
    """Test class for the GTK3Adjustment class."""

    widget_class = GTK3Adjustment
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_ADJUSTMENT_ATTRIBUTES
    expected_get_value = [
        [True, 1.0],
        [4.3, 4.3],
        [8, 8.0],
    ]
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_ADJUSTMENT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_ADJUSTMENT_METHODS
    expected_properties = EXPECTED_ADJUSTMENT_PROPERTIES
    expected_set_value = [
        [True, 1.0],
        [4.3, 4.3],
        [8, 8.0],
    ]
    expected_set_value_wrong_types = [
        date.today(),
        None,
        (1, 2),
    ]

    def make_dut(
        self,
        value=0.0,
        lower=0.0,
        upper=0.0,
        step_increment=0.0,
        page_increment=0.0,
        page_size=0.0,
    ):
        """Create a device under test for the GTK3Adjustment."""
        return self.widget_class(
            value, lower, upper, step_increment, page_increment, page_size
        )

    def mock_handler(self, package):
        """Mock handler for on_changed() calls."""
        assert isinstance(package, dict)
        assert package == {-1: 1.8}

    @pytest.mark.unit
    def test_init_with_values(self):
        dut = self.make_dut(6.5, 5, 10, 0.1, 0.2, 1.0)

        assert dut.do_get_property("lower") == 5
        assert dut.do_get_property("upper") == 10
        assert dut.do_get_value() == 6.5
        assert dut.do_get_property("step_increment") == 0.1
        assert dut.do_get_property("page_increment") == 0.2
        assert dut.do_get_property("page_size") == 1.0

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("axis") is None
        assert dut.do_get_attribute("canvas") is None
        assert dut.do_get_attribute("column_types") is None
        assert dut.do_get_attribute("data_type") is None
        assert dut.do_get_attribute("default_value") == 0.0
        assert dut.do_get_attribute("edit_signal") == "value-changed"
        assert dut.do_get_attribute("figure") is None
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") is None
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen-topic"
        assert dut.do_get_attribute("n_columns") is None
        assert dut.do_get_attribute("n_rows") is None
        assert dut.do_get_attribute("send_topic") == "send-topic"
        assert dut.do_get_attribute("x_pos") is None
        assert dut.do_get_attribute("y_pos") is None

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=1.0,
                edit_signal="adjustment_changed",
            )
        )

        assert dut.do_get_attribute("default_value") == 1.0
        assert dut.do_get_attribute("edit_signal") == "adjustment_changed"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("lower") == 0.0
        assert dut.do_get_property("upper") == 0.0
        assert dut.do_get_value() == 0.0
        assert dut.do_get_property("step_increment") == 0.0
        assert dut.do_get_property("page_increment") == 0.0
        assert dut.do_get_property("page_size") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                lower=5,
                upper=10,
                value=6.5,
                step_increment=0.1,
                page_increment=0.2,
                page_size=1.0,
            )
        )

        assert dut.do_get_property("lower") == 5
        assert dut.do_get_property("upper") == 10
        assert dut.do_get_value() == 6.5
        assert dut.do_get_property("step_increment") == 0.1
        assert dut.do_get_property("page_increment") == 0.2
        assert dut.do_get_property("page_size") == 1.0

    @pytest.mark.unit
    def test_do_set_value(self):
        """Should set the value of the GTK3Adjustment."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)

        for _value in self.expected_set_value:
            dut.do_set_value(_value[0])
            assert dut.do_get_value() == _value[1]

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current date."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)

        for _value in self.expected_get_value:
            dut.do_set_value(_value[0])
            assert dut.do_get_value() == _value[1]

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the value of the GTK3Adjustment."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)

        dut.dic_attributes["send_topic"] = "adjustment_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: 2})

        assert dut.do_get_value() == 2.0

        pub.unsubscribe(dut.do_update, "rootTopic")

    @pytest.mark.unit
    def test_on_changed(self):
        """Call on_changed() when a GTK3Adjustment value changes."""
        dut = self.make_dut(0.0, 0, 5, 0.1, 0.2, 0.5)

        dut.dic_attributes["send_topic"] = "adjustment_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_value(1.8)

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
