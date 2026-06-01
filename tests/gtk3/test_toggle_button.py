"""Test module for the GTK3ToggleButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3ToggleButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests
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
class TestGTK3ToggleButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ToggleButton."""

    widget_class = GTK3ToggleButton
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_TOGGLE_BUTTON_ATTRIBUTES
    )
    expected_default_height = 30
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

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3ToggleButton."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)

        # These are inherited from GTK3GObjectMixin.
        assert dut._DEFAULT_HEIGHT == self.expected_default_height
        assert dut._DEFAULT_TOOLTIP == self.expected_default_tooltip
        assert dut._DEFAULT_WIDTH == self.expected_default_width
        assert dut.dic_attributes == self.expected_attributes
        assert dut.dic_handler_id == self.expected_handler_id
        assert dut.dic_properties == self.expected_properties

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties to the values passed in the
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

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3ToggleButton with the data package value."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: True})

        assert dut.do_get_property("active")
        assert not dut.do_get_property("draw_indicator")
        assert not dut.do_get_property("inconsistent")

    @pytest.mark.unit
    def test_do_update_float(self):
        """Should update the GTK3ToggleButton with a float value."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: 6.8})

        assert dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.unit
    def test_do_update_int(self):
        """Should update the GTK3ToggleButton with an int value."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: 6})

        assert dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3ToggleButton is set."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 5
        dut.dic_attributes["send_topic"] = "toggle_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("toggled")
