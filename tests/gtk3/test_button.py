# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3Button module algorithms and models."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3Button, do_make_buttonbox
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


class TestButton(BaseGTK3WidgetTests):
    """Test class for the GTK3Button."""

    widget_class = GTK3Button
    expected_attributes = [
        "clicked",
        # "enter", # deprecated
        # "get_alignment", # deprecated
        "get_always_show_image",
        "get_event_window",
        # "get_focus_on_click", # deprecated
        "get_image",
        "get_image_position",
        "get_label",
        "get_relief",
        # "get_use_stock", # deprecated
        "get_use_underline",
        # "leave", # deprecated
        # "pressed", # deprecated
        # "released", # deprecated
        # "set_alignment", # deprecated
        "set_always_show_image",
        # "set_focus_on_click", # deprecated
        "set_image",
        "set_image_position",
        "set_label",
        "set_relief",
        # "set_use_stock", # deprecated
        "set_use_underline",
    ]
    expected_default_height = 30
    expected_default_width = 200
    expected_handler_id = {
        "activate": -1,
        "add": -1,
        "check-resize": -1,
        "clicked": -1,
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
        "unmap": -1,
        "unrealize": -1,
    }
    expected_properties = {
        "action_name": None,
        "action_target": None,
        "always_show_image": False,
        "border_width": 0,
        "can_default": False,
        "can_focus": False,
        "focus_on_click": True,
        "halign": Gtk.Align.FILL,
        "has_default": False,
        "has_focus": False,
        "has_tooltip": False,
        "height_request": -1,
        "hexpand": False,
        "hexpand_set": False,
        "image": None,
        "image_position": Gtk.PositionType.LEFT,
        "is_focus": False,
        "label": None,
        "margin": 0,
        "margin_bottom": 0,
        "margin_end": 0,
        "margin_start": 0,
        "margin_top": 0,
        "name": "pytkwrap GTK3 widget",
        "opacity": 1.0,
        "parent": None,
        "receives_default": False,
        "relief": Gtk.ReliefStyle.NORMAL,
        "scale_factor": 1,
        "sensitive": True,
        "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
        "tooltip_text": "Missing tooltip, please file an issue to have one added.",
        "use_underline": False,
        "valign": Gtk.Align.FILL,
        "vexpand": False,
        "vexpand_set": False,
        "visible": False,
        "width_request": -1,
        "window": None,
    }

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3Button."""
        return self.widget_class(label)

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3Button with a non-default label."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3Button)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties of a GTK3Button when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("action_name") is None
        assert dut.get_property("action_target") is None
        assert not dut.get_property("always_show_image")
        assert dut.get_property("image") is None
        assert dut.get_property("image_position") == Gtk.PositionType.LEFT
        assert dut.get_property("label") == "..."
        assert dut.get_property("relief") == Gtk.ReliefStyle.NORMAL
        assert not dut.get_property("use_underline")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3Button to the values passed in a
        GTK3WidgetProperties dict."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                always_show_image=True,
                image=None,
                label="Test Label",
                relief=Gtk.ReliefStyle.NONE,
                use_underline=True,
            )
        )

        assert dut.do_get_property("always_show_image")
        assert dut.do_get_property("image") is None
        assert dut.do_get_property("label") == "Test Label"
        assert dut.do_get_property("relief") == Gtk.ReliefStyle.NONE
        assert dut.do_get_property("use_underline")

    @pytest.mark.unit
    def test_do_set_properties_image(self, image_file):
        """Should set the properties of a GTK3Button to the values passed in a
        GTK3WidgetProperties dict."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                always_show_image=True,
                image=image_file,
                label="Test Label",
                relief=Gtk.ReliefStyle.NONE,
                use_underline=True,
            )
        )

        assert dut.get_property("always_show_image")
        assert isinstance(dut.get_property("image"), Gtk.Image)
        assert dut.get_property("label") == ""
        assert dut.get_property("relief") == Gtk.ReliefStyle.NONE
        assert dut.get_property("use_underline")


@pytest.mark.integration
def test_do_make_buttonbox_vertical(image_file):
    """Should make a vertical buttonbox with a single button."""
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=["Test tooltip"],
        callbacks=[],
    )

    assert isinstance(_buttonbox, Gtk.VButtonBox)


@pytest.mark.integration
def test_do_make_buttonbox_horizontal(image_file):
    """Should make a horizontal buttonbox with a single button."""
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=["Test tooltip"],
        callbacks=[],
        orientation="horizontal",
    )

    assert isinstance(_buttonbox, Gtk.HButtonBox)


@pytest.mark.integration
def test_do_make_buttonbox_no_tooltip(image_file):
    """Should make a vertical buttonbox with a single button with no tooltip."""
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=[],
        callbacks=[],
    )

    assert isinstance(_buttonbox, Gtk.VButtonBox)
