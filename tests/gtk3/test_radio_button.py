"""Test module for the GTK3RadioButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3RadioButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestRadioButton(BaseGTK3WidgetTests):
    """Test class for the GTK3RadioButton."""

    widget_class = GTK3RadioButton
    expected_attributes = [
        "get_group",
        "join_group",
        "set_group",
    ]
    expected_default_height = 40
    expected_default_edit_signal = "toggled"
    expected_default_width = 200
    expected_handler_id = {}
    expected_package = {0: {"test_field": True}}
    expected_properties = {}

    def make_dut(self, label="", group=None):
        return self.widget_class(label, group)

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3RadioButton with default attribute values."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3RadioButton)
        assert self.expected_default_height == dut._DEFAULT_HEIGHT
        assert self.expected_default_width == dut._DEFAULT_WIDTH
        assert self.expected_default_edit_signal == dut._DEFAULT_EDIT_SIGNAL
        # GTK3RadioButton-specific properties should be registered.
        for _property in GTK3RadioButton._GTK3_RADIO_BUTTON_PROPERTIES:
            assert _property in dut.dic_properties
        # GTK3RadioButton-specific signals should be registered.
        for _signal in GTK3RadioButton._GTK3_RADIO_BUTTON_SIGNALS:
            assert _signal in dut.dic_handler_id

        assert dut.get_active()
        assert dut.get_group() == [dut]
        assert not dut.get_inconsistent()
        assert dut.get_label() == ""
        assert dut.get_mode()  # draw-indicator property.

    @pytest.mark.unit
    def test_init_with_group(self):
        """Should create a GTK3RadioButton as part of passed group."""
        btnRadioButton = GTK3RadioButton()

        dut = self.make_dut(group=btnRadioButton)

        assert isinstance(dut, GTK3RadioButton)
        assert not dut.get_active()
        assert dut.get_group() == [dut, btnRadioButton]

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3RadioButton with a label."""
        dut = self.make_dut(label="Test Radio Button Label")

        assert isinstance(dut, GTK3RadioButton)
        assert dut.get_label() == "Test Radio Button Label"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties values of a GTK3RadioButton when passed an
        empty GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_active()
        assert dut.get_group() == [dut]
        assert not dut.get_inconsistent()
        assert dut.get_label() == "..."
        assert not dut.get_mode()  # draw-indicator property.

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the GTKRadioButton properties to the values passed in a
        GTK3WidgetProperties dict."""
        btnRadioButton = GTK3RadioButton()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                active=False,
                draw_indicator=True,
                group=btnRadioButton,
                inconsistent=True,
                label="Test Option Button Label",
            ),
        )

        assert not dut.get_active()
        assert dut.get_group() == [dut, btnRadioButton]
        assert dut.get_inconsistent()
        assert dut.get_label() == "Test Option Button Label"
        assert dut.get_mode()  # draw-indicator property.

    @pytest.mark.unit
    def test_do_update(self):
        """Update the GTK3RadioButton with the data package value."""
        btnRadioButton = GTK3RadioButton()

        dut = self.make_dut()
        dut.join_group(btnRadioButton)

        dut.dic_attributes["index"] = 3
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={3: True})

        assert dut.get_active()

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Do NOT update the GTK3RadioButton with the data package value or None."""
        btnRadioButton = GTK3RadioButton()

        dut = self.make_dut()
        dut.join_group(btnRadioButton)

        dut.dic_attributes["index"] = 3
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={3: None})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Raise an UnkSignalError with an unknown edit signal name."""
        btnRadioButton = GTK3RadioButton()

        dut = self.make_dut()
        dut.join_group(btnRadioButton)

        dut.dic_attributes["index"] = 8
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.dic_attributes["edit_signal"] = "unk_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={8: True})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Do nothing when the package field doesn't match."""
        btnRadioButton = GTK3RadioButton()

        dut = self.make_dut()
        dut.join_group(btnRadioButton)

        dut.dic_attributes["index"] = 3
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={23: True})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_on_changed(self):
        """Called when the GTK3RadioButton active state changes."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 3
        dut.dic_attributes["record_id"] = 0
        dut.dic_attributes["send_topic"] = "button_toggled"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("toggled")

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 3
        dut.dic_attributes["record_id"] = 0
        dut.dic_attributes["send_topic"] = "button_toggled"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.dic_attributes["edit_signal"] = "toggle_signal"
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("toggled")
