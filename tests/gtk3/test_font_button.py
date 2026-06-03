"""Test module for the GTK3FontButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3FontButton
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
    EXPECTED_FONT_BUTTON_ATTRIBUTES,
    EXPECTED_FONT_BUTTON_HANDLER_IDS,
    EXPECTED_FONT_BUTTON_METHODS,
    EXPECTED_FONT_BUTTON_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FontButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3FontButton."""

    widget_class = GTK3FontButton
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_FONT_BUTTON_ATTRIBUTES
    )
    expected_default_height = 30
    expected_default_width = 60
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_FONT_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_FONT_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_FONT_BUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("font_name") == "Sans 12"
        assert dut.do_get_property("show_size")
        assert dut.do_get_property("show_style")
        assert dut.do_get_property("title") == "Pick a Font"
        assert not dut.do_get_property("use_font")
        assert not dut.do_get_property("use_size")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                font_name="Sans 10",
                show_size=False,
                show_style=False,
                title="Choose a Font",
                use_font=True,
                use_size=True,
            )
        )

        assert dut.do_get_property("font_name") == "Sans 10"
        assert not dut.do_get_property("show_size")
        assert not dut.do_get_property("show_style")
        assert dut.do_get_property("title") == "Choose a Font"
        assert dut.do_get_property("use_font")
        assert dut.do_get_property("use_size")

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3FontButton with the data package value."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: "Serif 15"})

        assert dut.do_get_property("font_name") == "Serif 15"

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3FontButton color is set."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 5
        dut.dic_attributes["send_topic"] = "font_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("font-set")
