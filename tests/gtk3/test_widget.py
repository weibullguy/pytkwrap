"""Test module for the GTK3Widget class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.order(3)
class TestGTK3Widget(BaseGTK3GObjectTests):
    """Test class for the GTK3Widget class."""

    widget_class = GTK3Widget
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS
    expected_properties = EXPECTED_WIDGET_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_zero_height(self):
        """Should use _DEFAULT_HEIGHT when height_request is 0."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(height_request=0))

        assert (
            dut.dic_properties["height_request"] == self.expected_default_height
        )  # falls back to _DEFAULT_HEIGHT

    @pytest.mark.unit
    def test_do_set_properties_zero_width(self):
        """Should use _DEFAULT_WIDTH when width_request is 0."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(width_request=0))

        assert (
            dut.dic_properties["width_request"] == self.expected_default_width
        )  # falls back to _DEFAULT_WIDTH
