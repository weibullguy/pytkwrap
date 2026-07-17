"""Test module for the GTK3EntryBuffer class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import (
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
    set_widget_sensitivity,
)
from pytkwrap.gtk3.text import GTK3EntryBuffer
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.text.constants import (
    EXPECTED_ENTRYBUFFER_HANDLER_IDS,
    EXPECTED_ENTRYBUFFER_METHODS,
    EXPECTED_ENTRYBUFFER_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3EntryBuffer(BaseGTK3GObjectTests):
    """Test class for the GTK3EntryBuffer class."""

    widget_class = GTK3EntryBuffer
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_ENTRYBUFFER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_ENTRYBUFFER_METHODS
    expected_properties = EXPECTED_ENTRYBUFFER_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("max_length") == 0
        assert dut.do_get_property("text") == ""

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                max_length=10,
                text="Test Text",
            )
        )

        assert dut.get_property("max_length") == 10
        assert dut.get_max_length() == 10
        assert dut.get_property("text") == "Test Text"
        assert dut.get_text() == "Test Text"
