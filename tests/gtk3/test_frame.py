# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_frame.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3 frame module algorithms and models."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.frame import GTK3Frame
from pytkwrap.gtk3.label import GTK3Label
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


@pytest.mark.order(4)
class TestFrame(BaseGTK3WidgetTests):
    """Test class for the Frame."""

    widget_class = GTK3Frame
    expected_default_height = -1
    expected_default_value = None
    expected_default_width = -1

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3Frame with default values for attributes."""
        super().test_init()

        dut = self.make_dut()

        assert isinstance(dut, GTK3Frame)
        assert dut._DEFAULT_HEIGHT == -1
        assert dut._DEFAULT_WIDTH == -1
        # All handler IDs should start at -1.
        assert all(_hid == -1 for _hid in dut.dic_handler_id.values())
        # Frame-specific properties should be registered.
        for _property in GTK3Frame._GTK3_FRAME_PROPERTIES:
            assert _property in dut.dic_properties
        # Frame-specific signals should be registered.
        for _signal in GTK3Frame._GTK3_FRAME_SIGNALS:
            assert _signal in dut.dic_handler_id

    @pytest.mark.unit
    def test_set_properties_default(self):
        """Set the default properties of a GTK3Frame when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("label") == ""
        assert isinstance(dut.get_property("label_widget"), Gtk.Label)
        assert dut.get_property("label_xalign") == 0.0
        assert dut.get_property("label_yalign") == 0.5
        assert dut.get_property("shadow-type") == Gtk.ShadowType.ETCHED_IN

    @pytest.mark.unit
    def test_set_properties(self):
        """Should set the properties of a GTK3Frame."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                label="Test Frame Title",
                shadow_type=Gtk.ShadowType.ETCHED_OUT,
            ),
        )

        assert dut.get_label() == "Test Frame Title"
        assert dut.get_property("shadow-type") == Gtk.ShadowType.ETCHED_OUT

    @pytest.mark.unit
    def test_set_properties_label_widget(self):
        """Should set the label widget property of a GTK3Frame."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(label_widget=GTK3Label("Test Frame Title"))
        )

        assert isinstance(dut.get_label_widget(), Gtk.Label)
