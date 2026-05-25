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
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_METHODS,
    EXPECTED_BUTTON_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_RADIO_BUTTON_HANDLER_IDS,
    EXPECTED_RADIO_BUTTON_METHODS,
    EXPECTED_RADIO_BUTTON_PROPERTIES,
    EXPECTED_TOGGLE_BUTTON_HANDLER_IDS,
    EXPECTED_TOGGLE_BUTTON_METHODS,
    EXPECTED_TOGGLE_BUTTON_PROPERTIES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestRadioButton(BaseGTK3WidgetTests):
    """Test class for the GTK3RadioButton."""

    widget_class = GTK3RadioButton
    expected_default_height = 40
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_TOGGLE_BUTTON_HANDLER_IDS
        | EXPECTED_RADIO_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_TOGGLE_BUTTON_METHODS
        + EXPECTED_RADIO_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_TOGGLE_BUTTON_PROPERTIES
        | EXPECTED_TOGGLE_BUTTON_PROPERTIES
        | EXPECTED_RADIO_BUTTON_PROPERTIES
    )

    def make_dut(self, label="", group=None):
        return self.widget_class(label, group)

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3RadioButton with default attribute values."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3RadioButton)
        assert self.expected_default_height == dut._DEFAULT_HEIGHT
        assert self.expected_default_width == dut._DEFAULT_WIDTH
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
    def test_on_changed(self):
        """Called when the GTK3RadioButton active state changes."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 3
        dut.dic_attributes["record_id"] = 0
        dut.dic_attributes["send_topic"] = "button_toggled"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("toggled")
