"""Test module for the GTK3ToggleButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3ToggleButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ToggleButton(BaseGTK3WidgetTests):
    """Test class for the GTK3ToggleButton."""

    widget_class = GTK3ToggleButton
    expected_attributes = [
        "get_active",
        "get_inconsistent",
        "get_mode",
        "set_active",
        "set_inconsistent",
        "set_mode",
        "toggled",
    ]
    expected_default_edit_signal = "toggled"
    expected_default_height = 30
    expected_default_value = 0.0
    expected_default_width = 60
    expected_handler_id = {
        "add": -1,
        "check-resize": -1,
        "destroy": -1,
        "direction-changed": -1,
        "hide": -1,
        "keynav-failed": -1,
        "map": -1,
        "mnemonic-activate": -1,
        "move-focus": -1,
        "notify": -1,
        "query-tooltip": -1,
        "realize": -1,
        "remove": -1,
        "set-focus-child": -1,
        "show": -1,
        "state-flags-changed": -1,
        "toggled": -1,
        "unmap": -1,
        "unrealize": -1,
    }
    expected_properties = {
        "active": False,
        "border_width": 0,
        "can_default": False,
        "can_focus": False,
        "draw_indicator": False,
        "focus_on_click": True,
        "halign": Gtk.Align.FILL,
        "has_default": False,
        "has_focus": False,
        "has_tooltip": False,
        "height_request": -1,
        "hexpand": False,
        "hexpand_set": False,
        "inconsistent": False,
        "is_focus": False,
        "margin": 0,
        "margin_bottom": 0,
        "margin_end": 0,
        "margin_start": 0,
        "margin_top": 0,
        "name": "pytkwrap GTK3 widget",
        "opacity": 1.0,
        "parent": None,
        "receives_default": False,
        "scale_factor": 1,
        "sensitive": True,
        "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
        "tooltip_text": "Missing tooltip, please file an issue to have one added.",
        "valign": Gtk.Align.FILL,
        "vexpand": False,
        "vexpand_set": False,
        "visible": False,
        "width_request": -1,
        "window": None,
    }

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3ToggleButton."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)

        # These are inherited from GTK3GObjectMixin.
        assert dut._DEFAULT_HEIGHT == self.expected_default_height
        assert dut._DEFAULT_TOOLTIP == self.expected_default_tooltip
        assert dut._DEFAULT_WIDTH == self.expected_default_width
        assert dut.dic_attributes == {
            "default_value": False,
            "edit_signal": "toggled",
            "index": -1,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_handler_id == self.expected_handler_id
        assert dut.dic_properties == self.expected_properties

    @pytest.mark.unit
    def test_set_properties_default(self):
        """Should set the default properties of a GTK3ToggleButton when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert not dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.unit
    def test_set_properties(self):
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

        assert dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

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
    def test_do_update_none_value(self):
        """Should update the GTK3ToggleButton properties with the default values when
        passed a data package with a value of None."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 11
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={11: None})

        assert not dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

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

        assert not dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Should do nothing when the data package key doesn't match the
        GTK3ToggleButton field name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 22
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_active(True)

        pub.sendMessage("rootTopic", package={12: False})

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

    @pytest.mark.skip(
        reason="GTK3ToggleButton.on_changed() does not raise an UnkSignalError for "
        "some reason."
    )
    def test_on_changed_unknown_signal(self):
        """Should raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 15
        dut.dic_attributes["send_topic"] = "toggle_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.dic_attributes["edit_signal"] = "unk_signal"

        with pytest.raises(UnkSignalError):
            dut.emit("toggled")
