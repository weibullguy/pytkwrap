"""Test module for the GTK3FontButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3FontButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests
from .test_constants import (
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_FONT_BUTTON_HANDLER_IDS,
    EXPECTED_FONT_BUTTON_PROPERTIES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_PROPERTIES,
)


# @pytest.mark.skip(
#    reason=(
#        "Gtk.FontButton routinely crashes at the C level in test environments. "
#        "Requires manual testing in a running GTK3 application."
#        "See examples/color_button.py for manual test program."
#    )
# )
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FontButton(BaseGTK3WidgetTests):
    """Test class for the GTK3FontButton."""

    widget_class = GTK3FontButton
    expected_attributes = [
        "get_font_name",
        "get_show_size",
        "get_show_style",
        "get_title",
        "get_use_font",
        "get_use_size",
        "set_font_name",
        "set_show_size",
        "set_show_style",
        "set_title",
        "set_use_font",
        "set_use_size",
    ]
    expected_default_edit_signal = "font-set"
    expected_default_height = 30
    expected_default_value = None
    expected_default_width = 60
    expected_handler_id = (
        EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_FONT_BUTTON_HANDLER_IDS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_FONT_BUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3FontButton."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)

        # These are inherited from GTK3GObjectMixin.
        assert dut._DEFAULT_HEIGHT == self.expected_default_height
        assert dut._DEFAULT_TOOLTIP == self.expected_default_tooltip
        assert dut._DEFAULT_WIDTH == self.expected_default_width
        assert dut.dic_attributes == {
            "default_value": "Sans 12",
            "edit_signal": "font-set",
            "index": -1,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_handler_id == self.expected_handler_id
        assert dut.dic_properties == self.expected_properties

    @pytest.mark.unit
    def test_set_properties_default(self):
        """Should set the default properties of a GTK3FontButton when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("font_name") == "Sans 12"
        assert dut.get_property("show_size")
        assert dut.get_property("show_style")
        assert dut.get_property("title") == "Pick a Font"
        assert not dut.get_property("use_font")
        assert not dut.get_property("use_size")

    @pytest.mark.unit
    def test_set_properties(self):
        """Should set the properties to the values passed in the
        GTK3WidgetProperties."""
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
    def test_do_update_none_value(self):
        """Should update the GTK3FontButton properties with the default values when
        passed a data package with a value of None."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 11
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={11: None})

        assert dut.do_get_property("font_name") == "Sans 12"

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Should raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 21
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.dic_attributes["edit_signal"] = "unk_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={21: "Test Package"})

        assert dut.do_get_property("font_name") == "Sans 12"

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Should do nothing when the data package key doesn't match the GTK3FontButton
        field name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 22
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_font("Helvetica 12")

        pub.sendMessage("rootTopic", package={12: False})

        assert dut.do_get_property("font_name") == "Sans 12"

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3FontButton color is set."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 5
        dut.dic_attributes["send_topic"] = "font_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("font-set")

    @pytest.mark.skip(
        reason="GTK3Widget.on_changed() does not raise an UnkSignalError for some "
        "reason."
    )
    def test_on_changed_unknown_signal(self):
        """Should raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 15
        dut.dic_attributes["send_topic"] = "font_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.dic_attributes["edit_signal"] = "unk_signal"

        with pytest.raises(UnkSignalError):
            dut.emit("font-set")
