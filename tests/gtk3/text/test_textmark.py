"""Test module for the GTK3TextMark class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.text import GTK3TextMark
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.text.constants import (
    EXPECTED_TEXTMARK_METHODS,
    EXPECTED_TEXTMARK_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3TextMark(BaseGTK3GObjectTests):
    """Test class for the GTK3TextMark class."""

    widget_class = GTK3TextMark
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_TEXTMARK_METHODS
    expected_properties = EXPECTED_TEXTMARK_PROPERTIES

    def make_dut(self, name: str | None = None, left_gravity: bool = False):
        """Make a new instance of the GTK3TextMark class."""
        return self.widget_class(name=name, left_gravity=left_gravity)

    @pytest.mark.unit
    def test_init_with_name(self):
        """Should create a GTK3TextMark with a name."""
        dut = self.make_dut(name="Test Name")

        assert dut.get_name() == "Test Name"

    @pytest.mark.unit
    def test_init_with_left_gravity(self):
        """Should create a GTK3TextMark with left gravity."""
        dut = self.make_dut(left_gravity=True)

        assert dut.get_left_gravity()
