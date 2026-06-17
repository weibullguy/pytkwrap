"""Test module for the GTK3MessageDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, Gtk
from pytkwrap.gtk3.dialog import GTK3MessageDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_DIALOG_HANDLER_IDS,
    EXPECTED_DIALOG_METHODS,
    EXPECTED_DIALOG_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_MESSAGEDIALOG_METHODS,
    EXPECTED_MESSAGEDIALOG_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
    EXPECTED_WINDOW_HANDLER_IDS,
    EXPECTED_WINDOW_METHODS,
    EXPECTED_WINDOW_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3MessageDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3MessageDialog class."""

    widget_class = GTK3MessageDialog
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_WINDOW_HANDLER_IDS
        | EXPECTED_DIALOG_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_WINDOW_METHODS
        + EXPECTED_DIALOG_METHODS
        + EXPECTED_MESSAGEDIALOG_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
        | EXPECTED_DIALOG_PROPERTIES
        | EXPECTED_MESSAGEDIALOG_PROPERTIES
    )

    def make_dut(
        self,
        buttons: Gtk.ButtonsType = Gtk.ButtonsType.NONE,
        message_type: Gtk.MessageType = Gtk.MessageType.INFO,
    ):
        return self.widget_class(
            buttons=buttons,
            message_type=message_type,
        )

    @pytest.mark.unit
    def test_init_with_buttons(self):
        """Should create a GTK3MessageDialog with the passed buttons."""
        dut = self.make_dut(buttons=Gtk.ButtonsType.OK_CANCEL)

        assert dut.do_get_property("buttons") == Gtk.ButtonsType.OK_CANCEL

    @pytest.mark.unit
    def test_init_with_message_type(self):
        """Should create a GTK3MessageDialog with the passed message type."""
        dut = self.make_dut(message_type=Gtk.MessageType.ERROR)

        assert dut.do_get_property("message_type") == Gtk.MessageType.ERROR

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("buttons") == Gtk.ButtonsType.NONE
        assert dut.do_get_property("message_area") is None
        assert dut.do_get_property("message_type") == Gtk.MessageType.INFO
        assert dut.do_get_property("secondary_text") is None
        assert not dut.do_get_property("secondary_use_markup")
        assert dut.do_get_property("text") == ""
        assert not dut.do_get_property("use_markup")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                buttons=Gtk.ButtonsType.OK_CANCEL,
                message_type=Gtk.MessageType.ERROR,
                secondary_text="Secondary Text",
                secondary_use_markup=True,
                text="Test Text",
                use_markup=True,
            )
        )

        assert isinstance(dut.get_property("message_area"), Gtk.Widget)
        assert isinstance(dut.get_message_area(), Gtk.Widget)
        assert dut.get_property("message_type") == Gtk.MessageType.ERROR
        assert dut.get_property("secondary_text") == "Secondary Text"
        assert dut.get_property("secondary_use_markup")
        assert dut.get_property("text") == "Test Text"
        assert dut.get_property("use_markup")
