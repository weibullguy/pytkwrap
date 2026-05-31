"""Test module for the GTK3CheckButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3CheckButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_METHODS,
    EXPECTED_BUTTON_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_TOGGLE_BUTTON_ATTRIBUTES,
    EXPECTED_TOGGLE_BUTTON_HANDLER_IDS,
    EXPECTED_TOGGLE_BUTTON_METHODS,
    EXPECTED_TOGGLE_BUTTON_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CheckButton(BaseGTK3GObjectTests):
    """Test class for the GTK3CheckButton."""

    widget_class = GTK3CheckButton
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_TOGGLE_BUTTON_ATTRIBUTES
    )
    expected_default_height = 40
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_TOGGLE_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_TOGGLE_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_TOGGLE_BUTTON_PROPERTIES
    )

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3CheckButton."""
        return self.widget_class(label)

    def mock_handler(self, package):
        """Mock handler for on_changed() calls."""
        assert isinstance(package, dict)
        assert package == {-1: True}

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3CheckButton with a default label and default values for
        attributes."""
        super().test_init()

        dut = self.make_dut()

        assert dut.get_label() == "..."
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3CheckButton with a label and default values for
        attributes."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3CheckButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

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

        assert dut.do_get_property("active")
        assert dut.do_get_property("draw_indicator")
        assert dut.do_get_property("inconsistent")
        assert dut.get_active()
        assert dut.get_inconsistent()

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3CheckButton with the data package value."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.dic_attributes["send_topic"] = "check_button_changed"
        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: True})

        assert dut.do_get_property("active")
        assert dut.get_active()

        pub.unsubscribe(dut.do_update, "rootTopic")

    @pytest.mark.unit
    def test_on_changed(self):
        """Call on_changed() when the GTK3CheckButton is toggled."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.dic_attributes["send_topic"] = "check_button_changed"
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_active(True)

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
