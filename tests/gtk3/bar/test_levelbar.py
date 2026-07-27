"""Test module for the GTK3LevelBar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.exceptions import WrongTypeError
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.bar import GTK3LevelBar
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.bar.constants import (
    EXPECTED_LEVELBAR_ATTRIBUTES,
    EXPECTED_LEVELBAR_HANDLER_IDS,
    EXPECTED_LEVELBAR_METHODS,
    EXPECTED_LEVELBAR_PROPERTIES,
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
class TestGTK3LevelBar(BaseGTK3DataWidgetTests):
    """Test class for the GTK3LevelBar class."""

    widget_class = GTK3LevelBar
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_LEVELBAR_ATTRIBUTES
    )
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_LEVELBAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_LEVELBAR_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_LEVELBAR_PROPERTIES

    @pytest.mark.unit
    def test_do_set_default_attributes(self):
        """Should set the default attributes of the GTK3LevelBar."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("axis") is None
        assert dut.do_get_attribute("canvas") is None
        assert dut.do_get_attribute("data_type") is None
        assert dut.do_get_attribute("default_value") == 0.0
        assert dut.do_get_attribute("edit_signal") == "changed"
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
        """Should set the attributes of the GTK3LevelBar to the values passed in a
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=5.0,
            )
        )

        assert dut.do_get_attribute("default_value") == 5.0

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("inverted")
        assert dut.do_get_property("max_value") == 1.0
        assert dut.do_get_property("min_value") == 0.0
        assert dut.do_get_property("mode") == Gtk.LevelBarMode.CONTINUOUS
        assert dut.do_get_property("value") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                inverted=True,
                max_value=5.0,
                min_value=1.0,
                mode=Gtk.LevelBarMode.DISCRETE,
                value=2.6,
            )
        )

        assert dut.get_property("inverted")
        assert dut.get_inverted()
        assert dut.get_property("max_value") == 5.0
        assert dut.get_max_value() == 5.0
        assert dut.get_property("min_value") == 1.0
        assert dut.get_min_value() == 1.0
        assert dut.get_property("mode") == Gtk.LevelBarMode.DISCRETE
        assert dut.get_mode() == Gtk.LevelBarMode.DISCRETE
        assert dut.get_property("value") == 2.6
        assert dut.get_value() == 2.6

    @pytest.mark.unit
    def test_do_set_value_float(self):
        """Should set the value of the GTK3LevelBar when passed a float."""
        dut = self.make_dut()
        dut.do_set_value(0.5)

        assert dut.get_value() == 0.5
        assert dut.get_property("value") == 0.5
        assert dut.do_get_property("value") == 0.5

    @pytest.mark.unit
    def test_do_set_value_int(self):
        """Should set the value of the GTK3LevelBar when passed an int."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(min_value=5.0, max_value=15.0))
        dut.do_set_value(10)

        assert dut.get_value() == 10.0
        assert dut.get_property("value") == 10.0
        assert dut.do_get_property("value") == 10.0

    @pytest.mark.unit
    def test_do_set_value_str(self):
        """Should set the value of the GTK3LevelBar when passed a string."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(min_value=5.0, max_value=15.0))
        dut.do_set_value("8.5")

        assert dut.get_value() == 8.5
        assert dut.get_property("value") == 8.5
        assert dut.do_get_property("value") == 8.5

    @pytest.mark.unit
    def test_do_set_value_by_property(self):
        """Should set the value of the GTK3LevelBar when passed a property."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                min_value=5.0,
                max_value=15.0,
                value=8.6,
            )
        )

        assert dut.get_value() == 8.6
        assert dut.get_property("value") == 8.6
        assert dut.do_get_property("value") == 8.6

    @pytest.mark.unit
    def test_do_set_value_out_of_range(self):
        """Should not set the value of the GTK3LevelBar when passed a value out of
        range."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(min_value=5.0, max_value=15.0))
        dut.do_set_value(20)

        assert dut.get_value() == 15.0
        assert dut.get_property("value") == 15.0
        assert dut.do_get_property("value") == 15.0

    @pytest.mark.unit
    def test_do_set_value_invalid_type(self):
        """Should raise a WrongTypeError when passed an invalid type."""
        dut = self.make_dut()

        with pytest.raises(WrongTypeError):
            dut.do_set_value(Gdk.RGBA())

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current value of the GTK3LevelBar."""
        dut = self.make_dut()
        dut.do_set_value(0.5)

        assert dut.do_get_value() == 0.5
        assert dut.get_property("value") == 0.5
        assert dut.do_get_property("value") == 0.5

    @pytest.mark.unit
    def test_do_set_value_discrete(self):
        """Should set the value of the GTK3LevelBar when passed a discrete value."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                max_value=15.0,
                min_value=5.0,
                mode=Gtk.LevelBarMode.DISCRETE,
            )
        )
        dut.do_set_value(7)

        assert dut.get_value() == 7.0
        assert dut.do_get_value() == 7.0
        assert dut.get_property("value") == 7.0
        assert dut.do_get_property("value") == 7.0
