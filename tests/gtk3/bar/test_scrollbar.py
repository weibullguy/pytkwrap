"""Test module for the GTK3Scrollbar class.

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
from pytkwrap.gtk3.bar.scrollbar import GTK3ScrollBar
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
class TestGTK3ScrollBar(BaseGTK3GObjectTests):
    """Test class for the GTK3ScrollBar class."""

    widget_class = GTK3ScrollBar
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

    def make_dut(self, orientation=Gtk.Orientation.VERTICAL, adjustment=None):
        return self.widget_class(orientation=orientation, adjustment=adjustment)

    @pytest.mark.unit
    def test_init_with_orientation(self):
        """Should create a GTK3ScrollBar with the passed orientation."""
        dut = self.make_dut(orientation=Gtk.Orientation.HORIZONTAL)

        assert dut.get_orientation() == Gtk.Orientation.HORIZONTAL

    @pytest.mark.unit
    def test_init_with_adjustment(self):
        """Should create a GTK3ScrollBar with the passed adjustment."""
        adjustment = Gtk.Adjustment(value=0.5, lower=0.0, upper=1.0, step_increment=0.1)
        dut = self.make_dut(adjustment=adjustment)

        assert dut.get_adjustment() == adjustment
        assert dut.get_value() == 0.5
