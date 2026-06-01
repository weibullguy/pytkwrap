"""Test module for the GTK3VolumeButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3VolumeButton
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
    EXPECTED_SCALE_BUTTON_ATTRIBUTES,
    EXPECTED_SCALE_BUTTON_HANDLER_IDS,
    EXPECTED_SCALE_BUTTON_METHODS,
    EXPECTED_SCALE_BUTTON_PROPERTIES,
    EXPECTED_VOLUME_BUTTON_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.skip(
    reason=(
        "Gtk.VolumeButton routinely crashes at the C level in test environments. "
        "Requires manual testing in a running GTK3 application."
        "See examples/Volume_button.py for manual test program."
    )
)
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3VolumeButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3VolumeButton."""

    widget_class = GTK3VolumeButton
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
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
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
        | EXPECTED_VOLUME_BUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties to the values passed in the
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                rgba=Gdk.RGBA(1.0, 1.0, 1.0, 1.0),
                show_editor=True,
                title="Choose a Volume",
                use_alpha=False,
            )
        )

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 1.0
        assert dut.get_property("rgba").blue == 1.0
        assert dut.get_property("rgba").green == 1.0
        assert dut.get_property("rgba").red == 1.0
        assert dut.get_property("show-editor")
        assert dut.get_property("title") == "Choose a Volume"
        assert not dut.get_property("use-alpha")

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3VolumeButton with the data package value."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: Gdk.RGBA(0.3, 0.1, 0.9, 0.75)})

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert isinstance(dut.get_rgba(), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 0.75
        assert dut.get_property("rgba").blue == 0.9
        assert dut.get_property("rgba").green == 0.1
        assert dut.get_property("rgba").red == 0.3

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3VolumeButton Volume is set."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 5
        dut.dic_attributes["send_topic"] = "Volume_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("Volume-set")
