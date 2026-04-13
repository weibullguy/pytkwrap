# pylint: skip-file
# ruff: noqa: S101
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
from .conftest import CommonWidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestCheckButton(CommonWidgetTests):
    """Test class for the CheckButton."""

    widget_class = GTK3CheckButton
    expected_default_height = 40
    expected_default_value = False
    expected_default_width = 200

    def make_dut(self, label="..."):
        return self.widget_class(label)

    def do_update_error_handler(self, message):
        assert message == "CheckButton.do_update(): Unknown signal name 'edit_signal'."

    def example_handler(self, node_id, package) -> None:
        if node_id == 0:
            assert package == {"test_field": True}

    def no_signal_error_handler(self, message):
        assert (
            message == "CheckButton.do_set_callbacks(): Unknown signal name "
            "'value-changed'."
        )

    def on_changed_error_handler(self, message):
        assert message == "CheckButton.on_changed(): Unknown signal name 'edit_signal'."

    @pytest.mark.unit
    def test_init_with_label(self):
        """__init__() should create a CheckButton with a label."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3CheckButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_set_properties_default(self):
        """do_set_properties() should set the default properties of a CheckButton when
        no keywords are passed to the method.
        """
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert not dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.unit
    def test_set_properties(self):
        """do_set_properties() should set the properties of a CheckButton."""
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
        """do_update() should update the GTK3CheckButton with the data in the passed
        package.
        """
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": True})

        assert dut.get_property("active")
        assert dut.get_active()

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """do_update() should update the GTK3CheckButton with the data in the passed
        package.
        """
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert not dut.get_property("active")
        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """do_update() should raise a key error with an unknown edit signal name."""
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
        """do_update() should do nothing when the package field doesn't match."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_active(True)

        pub.sendMessage("rootTopic", package={"wrong_field": False})

        assert dut.get_active()

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the CheckButton is toggled."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(self.example_handler, dut.send_topic)

        dut.set_active(True)

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """on_changed() should raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.edit_signal = "edit_signal"
        pub.subscribe(self.example_handler, dut.send_topic)

        dut.set_active(True)
