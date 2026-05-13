"""Test module for the GTK3MenuButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3MenuButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3MenuButton(BaseGTK3WidgetTests):
    """Test class for the GTK3MenuButton."""

    widget_class = GTK3MenuButton
    expected_attributes = [
        "get_align_widget",
        "get_direction",
        "get_menu_model",
        "get_popover",
        "get_popup",
        "get_use_popover",
        "set_align_widget",
        "set_direction",
        "set_menu_model",
        "set_popover",
        "set_popup",
        "set_use_popover",
    ]
    expected_default_edit_signal = "toggled"
    expected_default_height = 30
    expected_default_value = 0.0
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
    expected_properties = {
        "active": False,
        "align_widget": None,
        "border_width": 0,
        "can_default": False,
        "can_focus": False,
        "direction": Gtk.ArrowType.DOWN,
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
        "menu_model": None,
        "name": "pytkwrap GTK3 widget",
        "opacity": 1.0,
        "parent": None,
        "popover": None,
        "popup": None,
        "receives_default": False,
        "scale_factor": 1,
        "sensitive": True,
        "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
        "tooltip_text": "Missing tooltip, please file an issue to have one added.",
        "use_popover": True,
        "valign": Gtk.Align.FILL,
        "vexpand": False,
        "vexpand_set": False,
        "visible": False,
        "width_request": -1,
        "window": None,
    }

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3MenuButton."""
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
        """Should set the default properties of a GTK3MenuButton when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("align_widget") is None
        assert dut.do_get_property("direction") == Gtk.ArrowType.DOWN
        assert dut.do_get_property("menu_model") is None
        assert dut.do_get_property("popover") is None
        assert dut.do_get_property("popup") is None
        assert dut.do_get_property("use_popover")

    @pytest.mark.unit
    def test_set_properties(self):
        """Should set the properties to the values passed in the
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                direction=Gtk.ArrowType.UP,
                use_popover=False,
            )
        )

        assert dut.do_get_property("direction") == Gtk.ArrowType.UP
        assert not dut.do_get_property("use_popover")
