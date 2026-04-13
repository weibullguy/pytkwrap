# pylint: skip-file
# type: ignore
# -*- coding: utf-8 -*-
#
#       tests.gtk3.test_button.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3 button module algorithms and models."""

# Third Party Imports
import pytest

from pubsub import pub

# Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import (
    BaseButton,
    CheckButton,
    do_make_buttonbox,
)
from pytkwrap.gtk3 import WidgetProperties
from .conftest import CommonWidgetTests


class TestBaseButton(CommonWidgetTests):
    """Test class for the BaseButton."""

    widget_class = BaseButton
    expected_default_height = 30
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

        assert isinstance(dut, BaseButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """do_set_properties() should set the default properties of a BaseButton when
        no keywords are passed to the method."""
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
        """do_set_properties() should set the properties of a BaseButton when passed
        a WidgetProperties with values."""
        dut = self.make_dut()
        dut.do_set_properties(
            WidgetProperties(
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
        """do_set_properties() should set the properties of a BaseButton when passed
        a WidgetProperties with values."""
        dut = self.make_dut()
        dut.do_set_properties(
            WidgetProperties(
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


class TestCheckButton(CommonWidgetTests):
    """Test class for the CheckButton."""

    widget_class = CheckButton
    expected_default_height = 40
    expected_default_width = 200

    def make_dut(self, label="..."):
        return self.widget_class(label)

    def do_update_error_handler(self, message):
        assert message == "CheckButton.do_update(): Unknown signal name 'edit_signal'."

    def no_signal_error_handler(self, message):
        assert (
            message == "CheckButton.do_set_callbacks(): Unknown signal name "
            "'value-changed'."
        )

    @pytest.mark.unit
    def test_init_with_label(self):
        """__init__() should create a CheckButton with a label."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, CheckButton)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_set_properties_default(self):
        """do_set_properties() should set the default properties of a CheckButton when no keywords are passed to the method."""
        dut = self.make_dut()
        dut.do_set_properties(WidgetProperties())

        assert not dut.get_property("active")
        assert not dut.get_property("draw_indicator")
        assert not dut.get_property("inconsistent")

    @pytest.mark.gui
    def test_set_properties(self):
        """do_set_properties() should set the properties of a CheckButton."""
        dut = self.make_dut()
        dut.do_set_properties(
            WidgetProperties(
                active=True,
                draw_indicator=True,
                inconsistent=True,
            )
        )

        assert dut.get_property("active")
        assert dut.get_property("draw_indicator")
        assert dut.get_property("inconsistent")
        assert dut.get_active()
        assert dut.get_inconsistent()

    @pytest.mark.unit
    def test_do_update(self):
        """do_update() should update the CheckButton with the data in the passed
        package."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("toggled", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": True})

        assert dut.get_property("active")
        assert dut.get_active()

    @pytest.mark.unit
    def test_do_update_non_value(self):
        """do_update() should update the CheckButton with the data in the passed
        package."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("toggled", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert not dut.get_property("active")
        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """do_update() should raise a key error with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("toggled", dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut._EDIT_SIGNAL = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert not dut.get_active()

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """do_update() should do nothing when the package field doesn't match."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("toggled", dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_active(True)

        pub.sendMessage("rootTopic", package={"wrong_field": False})

        assert dut.get_active()


class TestOptionButton:
    """Test class for the OptionButton."""

    @pytest.mark.gui
    def test_create_button(self):
        """__init__() should create a OptionButton."""
        dut = OptionButton(label="Test Option Button")

        assert isinstance(dut, OptionButton)
        assert dut.get_label() == "Test Option Button"
        assert dut.get_property("height-request") == -1
        assert dut.get_property("width-request") == -1
