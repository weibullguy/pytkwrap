"""Test module for the GTK3Layout class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.layout import GTK3Layout
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
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.layout.constants import (
    EXPECTED_LAYOUT_METHODS,
    EXPECTED_LAYOUT_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Layout(BaseGTK3GObjectTests):
    """Test class for the GTK3Layout class."""

    widget_class = GTK3Layout
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_LAYOUT_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_LAYOUT_PROPERTIES
    )

    def make_dut(self, hadjustment=None, vadjustment=None):
        return self.widget_class(hadjustment, vadjustment)

    @pytest.mark.unit
    def test_init_with_adjustments(self):
        """Should create a GTK3Layout with the passed adjustments."""
        _hadjustment = GTK3Adjustment(0, 0, 10, 1, 10, 0)
        _vadjustment = GTK3Adjustment(0, 0, 10, 1, 10, 0)

        dut = self.make_dut(
            hadjustment=_hadjustment,
            vadjustment=_vadjustment,
        )

        assert dut.get_property("hadjustment") == _hadjustment
        assert dut.get_property("vadjustment") == _vadjustment

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("hadjustment") is None
        assert dut.do_get_property("height") == 100
        assert dut.do_get_property("hscroll_policy") == Gtk.ScrollablePolicy.MINIMUM
        assert dut.do_get_property("vadjustment") is None
        assert dut.do_get_property("vscroll_policy") == Gtk.ScrollablePolicy.MINIMUM
        assert dut.do_get_property("width") == 100

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _hadjustment = GTK3Adjustment(0, 0, 10, 1, 10, 0)
        _vadjustment = GTK3Adjustment(0, 0, 10, 1, 10, 0)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                hadjustment=_hadjustment,
                height=215,
                hscroll_policy=Gtk.ScrollablePolicy.NATURAL,
                vadjustment=_vadjustment,
                vscroll_policy=Gtk.ScrollablePolicy.NATURAL,
                width=250,
            )
        )

        assert dut.get_property("hadjustment") == _hadjustment
        assert dut.get_property("height") == 215
        assert dut.get_property("hscroll_policy") == Gtk.ScrollablePolicy.NATURAL
        assert dut.get_property("vadjustment") == _vadjustment
        assert dut.get_property("vscroll_policy") == Gtk.ScrollablePolicy.NATURAL
        assert dut.get_property("width") == 250
        assert dut.get_size() == (250, 215)
