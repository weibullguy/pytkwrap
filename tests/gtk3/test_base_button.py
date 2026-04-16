# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3BaseButton module algorithms and models."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import (
    GTK3BaseButton,
    do_make_buttonbox,
)
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


class TestBaseButton(BaseGTK3WidgetTests):
    """Test class for the GTK3BaseButton."""

    widget_class = GTK3BaseButton
    expected_default_height = 30
    expected_default_value = None
    expected_default_width = 200

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3BaseButton."""
        return self.widget_class(label)

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3BaseButton with default values for attributes."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3BaseButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties of a GTK3BaseButton when passed an empty
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
        """Should set the properties of a GTK3BaseButton to the values passed in a
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

        assert dut.get_property("always_show_image")
        assert dut.get_property("image") is None
        assert dut.get_property("label") == "Test Label"
        assert dut.get_property("relief") == Gtk.ReliefStyle.NONE
        assert dut.get_property("use_underline")

    @pytest.mark.unit
    def test_do_set_properties_image(self, image_file):
        """Should set the properties of a GTK3BaseButton to the values passed in a
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
