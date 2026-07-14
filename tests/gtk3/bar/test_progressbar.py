"""Test module for the GTK3ProgressBar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk, Pango
from pytkwrap.gtk3.bar import GTK3ProgressBar
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.bar.constants import (
    EXPECTED_PROGRESSBAR_ATTRIBUTES,
    EXPECTED_PROGRESSBAR_METHODS,
    EXPECTED_PROGRESSBAR_PROPERTIES,
)
from tests.gtk3.conftest import BaseGTK3DataWidgetTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ProgressBar(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ProgressBar class."""

    widget_class = GTK3ProgressBar
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_PROGRESSBAR_ATTRIBUTES
    )
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_PROGRESSBAR_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_PROGRESSBAR_PROPERTIES

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
        assert dut.do_get_attribute("data_type") == float
        assert dut.do_get_attribute("default_value") == 0.0
        assert dut.do_get_attribute("edit_signal") is None
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
                data_type=int,
                default_value=0.5,
            )
        )

        assert dut.do_get_attribute("data_type") == int
        assert dut.do_get_attribute("default_value") == 0.5

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("ellipsize") == Pango.EllipsizeMode.NONE
        assert dut.do_get_property("fraction") == 0.0
        assert not dut.do_get_property("inverted")
        assert dut.do_get_property("pulse_step") == 0.1
        assert not dut.do_get_property("show_text")
        assert dut.do_get_property("text") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                ellipsize=Pango.EllipsizeMode.MIDDLE,
                fraction=0.5,
                inverted=True,
                pulse_step=0.25,
                show_text=True,
                text="Test Text",
            )
        )

        assert dut.do_get_property("ellipsize") == Pango.EllipsizeMode.MIDDLE
        assert dut.do_get_property("fraction") == 0.5
        assert dut.do_get_property("inverted")
        assert dut.do_get_property("pulse_step") == 0.25
        assert dut.do_get_property("show_text")
        assert dut.do_get_property("text") == "Test Text"

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the value of the GTK3ProgressBar."""
        dut = self.make_dut()
        dut.set_fraction(0.68)

        assert dut.do_get_value() == 0.68

    @pytest.mark.unit
    def test_do_set_value(self):
        """Should set the value of the GTK3ProgressBar when passed a float."""
        dut = self.make_dut()
        dut.do_set_value(0.42)

        assert dut.get_fraction() == 0.42

    @pytest.mark.unit
    def test_do_set_value_int(self):
        """Should set the value of the GTK3ProgressBar when passed an int."""
        dut = self.make_dut()
        dut.do_set_value(2)

        assert dut.get_fraction() == 0.02

    @pytest.mark.unit
    def test_do_set_value_str(self):
        """Should set the value of the GTK3ProgressBar when passed a str."""
        dut = self.make_dut()
        dut.do_set_value("0.42")

        assert dut.get_fraction() == 0.42

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should not update the GTK3ProgressBar when the value is None."""
        dut = self.make_dut()

        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: None})

        assert dut.dic_attributes == self.expected_attributes
