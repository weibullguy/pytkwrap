# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_option_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3OptionButton module algorithms and models."""

# Third Party Imports
import pytest

from pubsub import pub

# Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3OptionButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties
from .conftest import BaseGTK3DataWidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestOptionButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3OptionButton."""

    widget_class = GTK3OptionButton
    expected_default_height = 40
    expected_default_edit_signal = "toggled"
    expected_package = {0:{"test_field": True}}
    expected_default_width = 200

    def make_dut(self, group=None, label=""):
        return self.widget_class(group, label)

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3OptionButton with default attribute values."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3OptionButton)
        assert self.expected_default_height == dut._DEFAULT_HEIGHT
        assert self.expected_default_width == dut._DEFAULT_WIDTH
        assert self.expected_default_edit_signal == dut._DEFAULT_EDIT_SIGNAL
        # GTK3OptionButton-specific properties should be registered.
        for _property in GTK3OptionButton._GTK3_OPTION_BUTTON_PROPERTIES:
            assert _property in dut.dic_properties
        # GTK3OptionButton-specific signals should be registered.
        for _signal in GTK3OptionButton._GTK3_OPTION_BUTTON_SIGNALS:
            assert _signal in dut.dic_handler_id

        assert dut.get_active()
        assert dut.get_group() == [dut]
        assert not dut.get_inconsistent()
        assert dut.get_label() == ""
        assert not dut.get_mode() # draw-indicator property.

    @pytest.mark.unit
    def test_init_with_group(self):
        """Should create a GTK3OptionButton as part of passed group."""
        btnOptionButton = GTK3OptionButton()

        dut = self.make_dut(btnOptionButton)

        assert isinstance(dut, GTK3OptionButton)
        assert not dut.get_active()
        assert dut.get_group() == [dut, btnOptionButton]

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3OptionButton with a label."""
        dut = self.make_dut(None,"Test Option Button Label")

        assert isinstance(dut, GTK3OptionButton)
        assert dut.get_label() == "Test Option Button Label"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties values of a GTK3OptionButton when passed an
        empty GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_active()
        assert dut.get_group() == [dut]
        assert not dut.get_inconsistent()
        assert dut.get_label() == ""
        assert not dut.get_mode() # draw-indicator property.

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the GTKOptionButton properties to the values passed in a
        GTK3WidgetProperties dict."""
        btnOptionButton = GTK3OptionButton()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                active=False,
                draw_indicator=True,
                group=btnOptionButton,
                inconsistent=True,
                label="Test Option Button Label",
                ),
            )

        assert not dut.get_active()
        assert dut.get_group() == [dut, btnOptionButton]
        assert dut.get_inconsistent()
        assert dut.get_label() == "Test Option Button Label"
        assert dut.get_mode() # draw-indicator property.

    @pytest.mark.unit
    def test_do_update(self):
        """Update the GTK3OptionButton with the data package value."""
        btnOptionButton = GTK3OptionButton()

        dut = self.make_dut()
        dut.join_group(btnOptionButton)

        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": True})

        assert dut.get_active()

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Do NOT update the GTK3OptionButton with the data package value or None."""
        btnOptionButton = GTK3OptionButton()

        dut = self.make_dut()
        dut.join_group(btnOptionButton)

        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Raise an UnkSignalError with an unknown edit signal name."""
        btnOptionButton = GTK3OptionButton()

        dut = self.make_dut()
        dut.join_group(btnOptionButton)

        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": True})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Do nothing when the package field doesn't match."""
        btnOptionButton = GTK3OptionButton()

        dut = self.make_dut()
        dut.join_group(btnOptionButton)

        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"wrong_field": True})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_on_changed(self):
        """Called when the GTK3OptionButton active state changes."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.emit("toggled")

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.edit_signal = "toggle_signal"
        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.emit("toggled")
