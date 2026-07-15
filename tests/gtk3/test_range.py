"""Test module for the GTK3Range class.

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

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.range import GTK3Range
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_RANGE_ATTRIBUTES,
    EXPECTED_RANGE_HANDLER_IDS,
    EXPECTED_RANGE_METHODS,
    EXPECTED_RANGE_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Range(BaseGTK3GObjectTests):
    """Test class for the GTK3Range class."""

    widget_class = GTK3Range
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_RANGE_ATTRIBUTES
    )
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_RANGE_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_RANGE_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_RANGE_PROPERTIES

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
        assert dut.do_get_attribute("default_value") is None
        assert dut.do_get_attribute("edit_signal") == "value-changed"
        assert dut.do_get_attribute("figure") is None
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") is None
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen-topic"
        assert dut.do_get_attribute("n_columns") is None
        assert dut.do_get_attribute("n_rows") is None
        assert dut.do_get_attribute("send_topic") == "send-topic"
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                edit_signal="range-updated",
            )
        )

        assert dut.do_get_attribute("edit_signal") == "range-updated"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("adjustment") is None
        assert dut.do_get_property("fill_level") == 1.7976931348623157e308
        assert not dut.do_get_property("inverted")
        assert dut.do_get_property("restrict_to_fill_level")
        assert dut.do_get_property("round_digits") == -1
        assert not dut.do_get_property("show_fill_level")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _adjustment = Gtk.Adjustment(lower=0, upper=100, value=50, step_increment=1)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=_adjustment,
                fill_level=100.0,
                inverted=True,
                restrict_to_fill_level=False,
                round_digits=2,
                show_fill_level=True,
            )
        )

        assert dut.get_property("adjustment") == _adjustment
        assert dut.get_adjustment() == _adjustment
        assert dut.get_property("fill_level") == 100.0
        assert dut.get_fill_level() == 100.0
        assert dut.get_property("inverted")
        assert dut.get_inverted()
        assert not dut.get_property("restrict_to_fill_level")
        assert not dut.get_restrict_to_fill_level()
        assert dut.get_property("round_digits") == 2
        assert dut.get_round_digits() == 2
        assert dut.get_property("show_fill_level")
        assert dut.get_show_fill_level()

    @pytest.mark.unit
    def test_do_set_value_float(self):
        """Should set the value of the GTK3Range when passed a float."""
        dut = self.make_dut()

        dut.set_range(0.0, 1.0)
        dut.do_set_value(0.86)

        assert dut.get_value() == 0.86

    @pytest.mark.unit
    def test_do_set_value_int(self):
        """Should set the value of the GTK3Range when passed an int."""
        dut = self.make_dut()

        dut.set_range(0.0, 10.0)
        dut.do_set_value(2)

        assert dut.get_value() == 2.0

    @pytest.mark.unit
    def test_do_set_value_str(self):
        """Should set the value of the GTK3Range when passed a str."""
        dut = self.make_dut()

        dut.set_range(0.0, 10.0)
        dut.do_set_value("3.9")

        assert dut.get_value() == 3.9

    @pytest.mark.unit
    def test_do_set_value_wrong_type(self):
        """Should raise the WrongTypeError when passed None, date, or a tuple."""
        dut = self.make_dut()

        dut.set_range(0.0, 1.0)
        with pytest.raises(WrongTypeError):
            dut.do_set_value(None)
        with pytest.raises(WrongTypeError):
            dut.do_set_value(date.today())
        with pytest.raises(WrongTypeError):
            dut.do_set_value((1.0, 3.2))

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current value of the GTK3Range."""
        dut = self.make_dut()

        dut.set_range(0.0, 1.0)
        dut.set_value(0.86)

        assert dut.do_get_value() == 0.86

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the value of the GTK3Range."""
        dut = self.make_dut()

        dut.set_range(0.0, 10.0)
        dut.dic_attributes["send_topic"] = "adjustment_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: 2})

        assert dut.do_get_value() == 2.0

        pub.unsubscribe(dut.do_update, "rootTopic")
