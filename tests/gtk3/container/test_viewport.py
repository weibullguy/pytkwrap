"""Test module for the GTK3Viewport class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Adjustment

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Viewport
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.container.constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_VIEWPORT_METHODS,
    EXPECTED_VIEWPORT_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Viewport(BaseGTK3GObjectTests):
    """Test class for the GTK3Viewport class."""

    widget_class = GTK3Viewport
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_VIEWPORT_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_VIEWPORT_PROPERTIES
    )

    def make_dut(self, hadjustment=None, vadjustment=None):
        return self.widget_class(hadjustment, vadjustment)

    @pytest.mark.unit
    def test_init_with_adjustments(self):
        """Should create a GTK3Viewport with passed GTK3Adjustments."""
        _hadjustment = GTK3Adjustment()
        _vadjustment = GTK3Adjustment()

        dut = self.make_dut(_hadjustment, _vadjustment)

        assert dut.do_get_property("hadjustment") == _hadjustment
        assert dut.do_get_property("vadjustment") == _vadjustment

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("hadjustment") is None
        assert dut.do_get_property("shadow_type") == Gtk.ShadowType.IN
        assert dut.do_get_property("vadjustment") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _hadjustment = GTK3Adjustment()
        _vadjustment = GTK3Adjustment()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                hadjustment=_hadjustment,
                shadow_type=Gtk.ShadowType.OUT,
                vadjustment=_vadjustment,
            )
        )

        assert Gtk.Scrollable.get_hadjustment(dut) == _hadjustment
        assert dut.get_property("hadjustment") == _hadjustment
        assert dut.get_shadow_type() == Gtk.ShadowType.OUT
        assert dut.get_property("shadow_type") == Gtk.ShadowType.OUT
        assert Gtk.Scrollable.get_vadjustment(dut) == _vadjustment
        assert dut.get_property("vadjustment") == _vadjustment

    @pytest.mark.unit
    def test_bin_window(self):
        """Should return the bin window."""
        dut = self.make_dut()

        assert dut.bin_window is None

    @pytest.mark.unit
    def test_view_window(self):
        """Should return the view window."""
        dut = self.make_dut()

        assert dut.view_window is None
