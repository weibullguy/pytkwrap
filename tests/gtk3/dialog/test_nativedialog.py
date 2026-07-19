"""Test module for the GTK3NativeDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.dialog import GTK3NativeDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.dialog.constants import (
    EXPECTED_NATIVEDIALOG_HANDLER_IDS,
    EXPECTED_NATIVEDIALOG_METHODS,
    EXPECTED_NATIVEDIALOG_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3NativeDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3NativeDialog class."""

    widget_class = GTK3NativeDialog
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_NATIVEDIALOG_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_NATIVEDIALOG_METHODS
    expected_properties = EXPECTED_NATIVEDIALOG_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("modal")
        assert dut.do_get_property("title") is None
        assert dut.do_get_property("transient_for") is None
        assert not dut.do_get_property("visible")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _window = Gtk.Window()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                modal=True,
                title="Test Title",
                transient_for=_window,
                visible=True,
            )
        )

        assert dut.get_property("modal")
        assert dut.get_modal()
        assert dut.get_property("title") == "Test Title"
        assert dut.get_title() == "Test Title"
        assert dut.get_property("transient_for") == _window
        assert dut.get_transient_for() == _window
        assert not dut.get_property("visible")
        assert not dut.get_visible()
