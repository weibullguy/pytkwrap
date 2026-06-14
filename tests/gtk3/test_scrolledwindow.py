"""Test module for the GTK3ScrolledWindow class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3 import GTK3Adjustment
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window import GTK3ScrolledWindow

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_SCROLLEDWINDOW_HANDLER_IDS,
    EXPECTED_SCROLLEDWINDOW_METHODS,
    EXPECTED_SCROLLEDWINDOW_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ScrolledWindow(BaseGTK3GObjectTests):
    """Test class for the GTK3ScrolledWindow."""

    widget_class = GTK3ScrolledWindow
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_SCROLLEDWINDOW_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_SCROLLEDWINDOW_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_SCROLLEDWINDOW_PROPERTIES
    )

    def make_dut(self, hadjustment=None, vadjustment=None):
        """Create a device under test for the GTK3ScrolledWindow."""
        return self.widget_class(hadjustment, vadjustment)

    @pytest.mark.unit
    def test_init_with_adjustment(self):
        """Should create a GTK3ScrolledWindow with adjustments."""
        _hadjustment = GTK3Adjustment()
        _vadjustment = GTK3Adjustment()

        dut = self.make_dut(_hadjustment, _vadjustment)

        assert dut.get_hadjustment() == _hadjustment
        assert dut.get_vadjustment() == _vadjustment

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("hadjustment") is None
        assert dut.do_get_property("hscrollbar_policy") == Gtk.PolicyType.AUTOMATIC
        assert dut.do_get_property("kinetic_scrolling")
        assert dut.do_get_property("max_content_height") == -1
        assert dut.do_get_property("max_content_width") == -1
        assert dut.do_get_property("min_content_height") == -1
        assert dut.do_get_property("min_content_width") == -1
        assert dut.do_get_property("overlay_scrolling")
        assert not dut.do_get_property("propagate_natural_height")
        assert not dut.do_get_property("propagate_natural_width")
        assert dut.do_get_property("shadow_type") == Gtk.ShadowType.NONE
        assert dut.do_get_property("vadjustment") is None
        assert dut.do_get_property("vscrollbar_policy") == Gtk.PolicyType.AUTOMATIC
        assert dut.do_get_property("window_placement") == Gtk.CornerType.TOP_LEFT

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _hadjustment = GTK3Adjustment()
        _vadjustment = GTK3Adjustment()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                hadjustment=_hadjustment,
                hscrollbar_policy=Gtk.PolicyType.ALWAYS,
                kinetic_scrolling=False,
                max_content_height=100,
                max_content_width=100,
                min_content_height=10,
                min_content_width=10,
                overlay_scrolling=False,
                propagate_natural_height=True,
                propagate_natural_width=True,
                shadow_type=Gtk.ShadowType.OUT,
                vadjustment=_vadjustment,
                vscrollbar_policy=Gtk.PolicyType.ALWAYS,
                window_placement=Gtk.CornerType.TOP_RIGHT,
            )
        )

        assert dut.do_get_property("hadjustment") == _hadjustment
        assert dut.do_get_property("hscrollbar_policy") == Gtk.PolicyType.ALWAYS
        assert not dut.do_get_property("kinetic_scrolling")
        assert dut.do_get_property("max_content_height") == 100
        assert dut.do_get_property("max_content_width") == 100
        assert dut.do_get_property("min_content_height") == 10
        assert dut.do_get_property("min_content_width") == 10
        assert not dut.do_get_property("overlay_scrolling")
        assert dut.do_get_property("propagate_natural_height")
        assert dut.do_get_property("propagate_natural_width")
        assert dut.do_get_property("shadow_type") == Gtk.ShadowType.OUT
        assert dut.do_get_property("vadjustment") == _vadjustment
        assert dut.do_get_property("vscrollbar_policy") == Gtk.PolicyType.ALWAYS
        assert dut.do_get_property("window_placement") == Gtk.CornerType.TOP_RIGHT
