# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_check_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3CheckButton module algorithms and models."""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3.buttons import (
    GTK3CheckButton,
)
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests

def mock_handler(node_id, package) -> None:
    """Mock message handler."""
    if node_id == 0:
        assert package == {"test_field": True}

@pytest.mark.usefixtures("suppress_stderr")
class TestCheckButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3CheckButton."""

    widget_class = GTK3CheckButton
    expected_default_height = 40
    expected_default_value = False
    expected_default_width = 200

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3CheckButton."""
        return self.widget_class(label)

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3CheckButton with a label and default values for
        attributes."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3CheckButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_set_properties_default(self):
        """Should set the default properties of a GTK3CheckButton when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert not dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.unit
    def test_set_properties(self):
        """Should set the properties of a GTK3CheckButton to the values in the passed
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                active=True,
                draw_indicator=True,
                inconsistent=True,
            )
        )

        assert dut.get_property("active")
        assert dut.get_property("draw_indicator")
        assert dut.get_property("inconsistent")
        assert dut.get_active()
        assert dut.get_inconsistent()

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3CheckButton with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": True})

        assert dut.get_property("active")
        assert dut.get_active()

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should NOT update the GTK3CheckButton when the data package is None."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert not dut.get_property("active")
        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Should raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Should NOT update the GTK3CheckButton when the package key doesn't match the
        GTK3CheckButton field name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_active(True)

        pub.sendMessage("rootTopic", package={"wrong_field": False})

        assert dut.get_active()

    @pytest.mark.unit
    def test_on_changed(self):
        """Call on_changed() when the GTK3CheckButton is toggled."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(mock_handler, dut.send_topic)

        dut.set_active(True)

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Should raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.edit_signal = "edit_signal"
        pub.subscribe(mock_handler, dut.send_topic)

        dut.set_active(True)
