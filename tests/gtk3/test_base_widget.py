# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_base_widget.py is part of the pytkwrap project.
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3BaseWidget module algorithms and models."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.common.mixins import set_widget_sensitivity
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.widget import (
    GTK3BaseWidget,
    GTK3WidgetProperties,
)

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


def example_callback():
    pass


@pytest.mark.order(3)
class TestBaseWidget(BaseGTK3WidgetTests):
    """Test class for the BaseWidget."""

    widget_class = GTK3BaseWidget
    expected_default_height = -1
    expected_default_value = None
    expected_default_width = -1

    def no_signal_error_handler(self, message):
        """Mock error handling method."""
        assert (
            message
            == "GTK3BaseWidget.do_set_callbacks(): Unknown signal name 'value-changed'."
        )

    @pytest.mark.unit
    def test_widget_do_set_properties_default(self):
        """Should set the default values when passed an empty GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("app_paintable")
        assert dut.get_property("can_default")
        assert dut.get_property("can_focus")
        assert (
            dut.get_property("events")
            == Gdk.EventMask.POINTER_MOTION_MASK | Gdk.EventMask.LEAVE_NOTIFY_MASK
        )
        assert dut.get_property("expand")
        assert dut.get_property("focus_on_click")
        assert dut.get_property("halign") == Gtk.Align.FILL
        assert not dut.get_property("has_default")
        assert not dut.get_property("has_focus")
        assert dut.get_property("has_tooltip")
        assert dut.get_property("height_request") == -1
        assert dut.get_property("hexpand")
        assert dut.get_property("hexpand_set")
        assert not dut.get_property("is_focus")
        assert dut.get_property("margin") == 0
        assert dut.get_property("margin_bottom") == 0
        assert dut.get_property("margin_end") == 0
        assert dut.get_property("margin_start") == 0
        assert dut.get_property("margin_top") == 0
        assert dut.get_property("name") == "pytkwrap widget"
        assert not dut.get_property("no_show_all")
        assert dut.get_property("opacity") == 1.0
        assert dut.get_property("parent") is None
        assert not dut.get_property("receives_default")
        assert (
            dut.get_property("tooltip_markup")
            == "Missing tooltip, please file an issue to have one added."
        )
        assert (
            dut.get_property("tooltip_text")
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut.get_property("valign")
        assert dut.get_property("vexpand")
        assert dut.get_property("vexpand_set")
        assert dut.get_property("visible")
        assert dut.get_property("width_request") == -1

    @pytest.mark.unit
    def test_widget_do_set_properties(self):
        """Should set the attributes of a GTK3BaseWidget."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                app_paintable=False,
                can_default=True,
                can_focus=True,
                events=Gdk.EventMask.TOUCH_MASK,
                expand=False,
                focus_on_click=False,
                halign=Gtk.Align.FILL,
                has_default=True,
                has_focus=True,
                has_tooltip=True,
                height_request=35,
                hexpand=False,
                hexpand_set=False,
                is_focus=False,
                margin=10,
                margin_bottom=5,
                margin_end=22,
                margin_start=3,
                margin_top=22,
                name="Test Widget Name",
                no_show_all=True,
                opacity=0.5,
                receives_default=True,
                sensitive=True,
                tooltip_markup="<b>Test Widget Tooltip</b>",
                tooltip_text="Test Widget Tooltip",
                valign=Gtk.Align.END,
                vexpand=False,
                vexpand_set=False,
                visible=True,
                width_request=120,
            )
        )

        assert not dut.get_property("app_paintable")
        assert dut.get_property("can_default")
        assert dut.get_property("can_focus")
        assert (
            dut.get_property("events")
            == Gdk.EventMask.POINTER_MOTION_MASK | Gdk.EventMask.LEAVE_NOTIFY_MASK
        )
        assert not dut.get_property("expand")
        assert not dut.get_property("focus_on_click")
        assert dut.get_property("halign") == Gtk.Align.FILL
        assert not dut.get_property("has_default")  # Must be within a GtkWindow to set.
        assert not dut.get_property("has_focus")  # Must be within a GtkWindow to set.
        assert dut.get_property("has_tooltip")
        assert dut.get_property("height_request") == 35
        assert not dut.get_property("hexpand")
        assert not dut.get_property("hexpand_set")
        assert not dut.get_property("is_focus")
        assert dut.get_property("margin") == 22
        assert dut.get_property("margin_bottom") == 5
        assert dut.get_property("margin_end") == 22
        assert dut.get_property("margin_start") == 3
        assert dut.get_property("margin_top") == 22
        assert dut.get_property("name") == "Test Widget Name"
        assert dut.get_property("no_show_all")
        assert dut.get_property("opacity") == pytest.approx(0.5, abs=0.01)
        assert dut.get_property("parent") is None
        assert dut.get_property("receives_default")
        assert dut.get_property("tooltip_markup") == "Test Widget Tooltip"
        assert dut.get_property("tooltip_text") == "Test Widget Tooltip"
        assert dut.get_property("valign")
        assert not dut.get_property("vexpand")
        assert not dut.get_property("vexpand_set")
        assert dut.get_property("visible")
        assert dut.get_property("width_request") == 120

    @pytest.mark.unit
    def test_widget_do_set_callbacks_with_buffer(self):
        """Should connect to the buffer when one is set in dic_properties."""
        if self.widget_class is not GTK3BaseWidget:
            pytest.skip("Buffer callback only applies to TextViews.")

        dut = self.make_dut()
        _buffer = Gtk.TextBuffer()
        dut.dic_properties["buffer"] = _buffer
        dut.do_set_callbacks("changed", example_callback)

        assert dut.dic_handler_id["changed"] != -1


@pytest.mark.unit
def test_set_widget_sensitivity_true():
    """Should make all widgets in the list sensitive."""
    widgets = [GTK3BaseWidget(), GTK3BaseWidget(), GTK3BaseWidget()]
    for w in widgets:
        w.set_sensitive(False)

    set_widget_sensitivity(widgets, sensitive=True)

    assert all(w.get_sensitive() for w in widgets)


@pytest.mark.unit
def test_set_widget_sensitivity_false():
    """Should make all widgets in the list insensitive."""
    widgets = [GTK3BaseWidget(), GTK3BaseWidget()]
    set_widget_sensitivity(widgets, sensitive=False)

    assert all(not w.get_sensitive() for w in widgets)


@pytest.mark.unit
def test_set_widget_sensitivity_empty_list():
    """Should handle an empty list without raising an exception."""
    assert set_widget_sensitivity([]) is None
