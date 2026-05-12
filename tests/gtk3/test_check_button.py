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
from .conftest import BaseGTK3WidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CheckButton(BaseGTK3WidgetTests):
    """Test class for the GTK3CheckButton."""

    widget_class = GTK3CheckButton
    expected_default_height = 40
    expected_default_value = False
    expected_default_width = 200
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
    expected_package = {0: {"test_field": True}}
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
        "label": "...",
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

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3CheckButton."""
        return self.widget_class(label)

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3CheckButton with a default label and default values for
        attributes."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3CheckButton)
        assert dut.dic_handler_id == self.expected_handler_id
        assert dut.dic_properties == self.expected_properties

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
    def test_set_properties_default(self):
        """Should set the default properties of a GTK3CheckButton when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert not dut.do_get_property("active")
        assert not dut.do_get_property("draw_indicator")
        assert not dut.do_get_property("inconsistent")

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
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: True})

        assert dut.do_get_property("active")
        assert dut.get_active()

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should NOT update the GTK3CheckButton when the data package is None."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={1: None})

        assert not dut.do_get_property("active")
        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Should raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.dic_attributes["edit_signal"] = "unk_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={1: True})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Should NOT update the GTK3CheckButton when the package key doesn't match the
        GTK3CheckButton field name."""
        dut = self.make_dut()
        dut.dic_attributes["field"] = "test_field"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_active(True)

        pub.sendMessage("rootTopic", package={"wrong_field": False})

        assert dut.get_active()

    @pytest.mark.unit
    def test_on_changed(self):
        """Call on_changed() when the GTK3CheckButton is Checkd."""
        dut = self.make_dut()
        dut.dic_attributes["field"] = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_Checkd"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.set_active(True)

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Should raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.dic_attributes["field"] = "test_field"
        dut.dic_attributes["record_id"] = 0
        dut.dic_attributes["send_topic"] = "button_Checkd"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.dic_attributes["edit_signal"] = "edit_signal"
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_active(True)
