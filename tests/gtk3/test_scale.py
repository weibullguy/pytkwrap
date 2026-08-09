"""Test module for the GTK3Scale class.

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
from pytkwrap.gtk3.scale import GTK3Scale
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_RANGE_ATTRIBUTES,
    EXPECTED_RANGE_HANDLER_IDS,
    EXPECTED_RANGE_METHODS,
    EXPECTED_RANGE_PROPERTIES,
    EXPECTED_SCALE_HANDLER_IDS,
    EXPECTED_SCALE_METHODS,
    EXPECTED_SCALE_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Scale(BaseGTK3GObjectTests):
    """Test class for the GTK3Scale class."""

    widget_class = GTK3Scale
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
        | EXPECTED_SCALE_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_RANGE_METHODS
        + EXPECTED_SCALE_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_RANGE_PROPERTIES
        | EXPECTED_SCALE_PROPERTIES
    )

    def make_dut(self, orientation=Gtk.Orientation.HORIZONTAL, adjustment=None):
        return self.widget_class(orientation=orientation, adjustment=adjustment)

    @pytest.mark.unit
    def test_init_with_orientation(self):
        """Should create a GTK3Scale with the passed orientation."""
        dut = self.make_dut(orientation=Gtk.Orientation.VERTICAL)

        assert dut.get_orientation() == Gtk.Orientation.VERTICAL

    @pytest.mark.unit
    def test_init_with_adjustment(self):
        """Should create a GTK3Scale with the passed adjustment."""
        adjustment = Gtk.Adjustment(value=0.5, lower=0.0, upper=1.0, step_increment=0.1)
        dut = self.make_dut(adjustment=adjustment)

        assert dut.get_adjustment() == adjustment
        assert dut.get_value() == 0.5

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("digits") == 1
        assert dut.do_get_property("draw_value")
        assert dut.do_get_property("has_origin")
        assert dut.do_get_property("value_pos") == Gtk.PositionType.TOP

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                digits=3,
                draw_value=False,
                has_origin=False,
                value_pos=Gtk.PositionType.BOTTOM,
            )
        )

        assert dut.get_property("digits") == 3
        assert dut.get_digits() == 3
        assert not dut.get_property("draw_value")
        assert not dut.get_draw_value()
        assert not dut.get_property("has_origin")
        assert not dut.get_has_origin()
        assert dut.get_property("value_pos") == Gtk.PositionType.BOTTOM
        assert dut.get_value_pos() == Gtk.PositionType.BOTTOM
