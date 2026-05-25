"""Test module for the GTK3Adjustment class.

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
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_ADJUSTMENT_HANDLER_IDS,
    EXPECTED_ADJUSTMENT_METHODS,
    EXPECTED_ADJUSTMENT_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.order(3)
class TestGTK3Adjustment(BaseGTK3GObjectTests):
    """Test class for the GTK3Adjustment class."""

    widget_class = GTK3Adjustment
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_ADJUSTMENT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_ADJUSTMENT_METHODS
    expected_properties = EXPECTED_ADJUSTMENT_PROPERTIES

    def make_dut(
        self,
        value=0.0,
        lower=0.0,
        upper=0.0,
        step_increment=0.0,
        page_increment=0.0,
        page_size=0.0,
    ):
        """Create a device under test for the GTK3Adjustment."""
        return self.widget_class(
            value, lower, upper, step_increment, page_increment, page_size
        )

    @pytest.mark.unit
    def test_init_with_values(self):
        dut = self.make_dut(6.5, 5, 10, 0.1, 0.2, 1.0)

        assert dut.do_get_property("lower") == 5
        assert dut.do_get_property("upper") == 10
        assert dut.do_get_value() == 6.5
        assert dut.do_get_property("step_increment") == 0.1
        assert dut.do_get_property("page_increment") == 0.2
        assert dut.do_get_property("page_size") == 1.0

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the value of the GTK3Adjustment."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)
        dut.do_set_value(4.3)

        assert dut.do_get_value() == 4.3

    @pytest.mark.unit
    def test_do_set_value_bool(self):
        """Should set the value of the GTK3Adjustment when passed a boolean."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)
        dut.do_set_value(True)

        assert dut.do_get_value() == 1.0

    @pytest.mark.unit
    def test_do_set_value_float(self):
        """Should set the value of the GTK3Adjustment when passed a float."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)
        dut.do_set_value(8.732)

        assert dut.do_get_value() == 8.732

    @pytest.mark.unit
    def test_do_set_value_int(self):
        """Should set the value of the GTK3Adjustment when passed an int."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)
        dut.do_set_value(8)

        assert dut.do_get_value() == 8.0

    @pytest.mark.unit
    def test_do_set_value_date(self):
        """Should a WrongTypeError and pass a do_log_error message when passed a
        date."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(date.today())

    @pytest.mark.unit
    def test_do_set_value_none(self):
        """Should a WrongTypeError and pass a do_log_error message when passed None."""
        dut = self.make_dut(0.0, 0, 10, 0.1, 0.2, 1.0)

        with pytest.raises(WrongTypeError):
            dut.do_set_value(None)
