# pylint: skip-file
# ruff: noqa: S101
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
from .conftest import CommonWidgetTests


class TestBaseButton(CommonWidgetTests):
    """Test class for the BaseButton."""

    widget_class = GTK3BaseButton
    expected_default_height = 30
    expected_default_value = None
    expected_default_width = 200

    def make_dut(self, label="..."):
        return self.widget_class(label)

    def no_signal_error_handler(self, message):
        assert (
            message
            == "BaseButton.do_set_callbacks(): Unknown signal name 'value-changed'."
        )

    @pytest.mark.unit
    def test_init_with_label(self):
        """__init__() should create a Button."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3BaseButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """do_set_properties() should set the default properties of a GTK3BaseButton
        when no keywords are passed to the method.
        """
        dut = self.make_dut()
        dut.do_set_properties(WidgetProperties())

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
        """do_set_properties() should set the properties of a GTK3BaseButton when passed
        a GTK3WidgetProperties with values.
        """
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
        """do_set_properties() should set the properties of a GTK3BaseButton when passed
        a GTK3WidgetProperties with values.
        """
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
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=["Test tooltip"],
        callbacks=[],
    )

    assert isinstance(_buttonbox, Gtk.VButtonBox)


@pytest.mark.integration
def test_do_make_buttonbox_horizontal(image_file):
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=["Test tooltip"],
        callbacks=[],
        orientation="horizontal",
    )

    assert isinstance(_buttonbox, Gtk.HButtonBox)


@pytest.mark.integration
def test_do_make_buttonbox_no_tooltip(image_file):
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=[],
        callbacks=[],
    )

    assert isinstance(_buttonbox, Gtk.VButtonBox)
