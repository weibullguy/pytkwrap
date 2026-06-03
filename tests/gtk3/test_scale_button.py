"""Test module for the GTK3ScaleButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.buttons import GTK3ScaleButton
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
    EXPECTED_SCALE_BUTTON_ATTRIBUTES,
    EXPECTED_SCALE_BUTTON_HANDLER_IDS,
    EXPECTED_SCALE_BUTTON_METHODS,
    EXPECTED_SCALE_BUTTON_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ScaleButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ScaleButton."""

    widget_class = GTK3ScaleButton
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_SCALE_BUTTON_ATTRIBUTES
    )
    expected_default_height = 30
    expected_default_width = 60
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_SCALE_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_SCALE_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_SCALE_BUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("adjustment") is None
        assert dut.do_get_property("icons") == []
        assert dut.do_get_property("size") == Gtk.IconSize.SMALL_TOOLBAR
        assert dut.do_get_property("value") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _adjustment = GTK3Adjustment()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=_adjustment,
                size=Gtk.IconSize.BUTTON,
                value=0.68,
            )
        )

        assert dut.do_get_property("adjustment") == _adjustment
        assert dut.do_get_property("size") == Gtk.IconSize.BUTTON
        assert dut.do_get_property("value") == 0.68

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3ScaleButton with the data package value."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={-1: 0.75})

        assert dut.do_get_property("value") == 0.75

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3ScaleButton value is set."""
        dut = self.make_dut()

        dut.dic_attributes["send_topic"] = "scale_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_value(5.8)

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
