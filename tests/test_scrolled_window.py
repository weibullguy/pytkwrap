# pylint: skip-file
# type: ignore
# -*- coding: utf-8 -*-
#
#       tests.gtk3.test_scrolledwindow.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3 ScrolledWindow module algorithms and models."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import ScrolledWindow, WidgetProperties
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, GObject, Gtk, Pango, _

# pytkwrap Local Imports
from .conftest import CommonWidgetTests


class TestScrolledWindow(CommonWidgetTests):
    """Test class for the ScrolledWindow."""

    widget_class = ScrolledWindow
    expected_default_height = -1
    expected_default_value = None
    expected_default_width = -1

    def make_dut(self, child=None):
        return self.widget_class(child)

    def no_signal_error_handler(self, message):
        assert (
            message == "ScrolledWindow.do_set_callbacks(): Unknown signal name "
            "'value-changed'."
        )

    @pytest.mark.unit
    def test_init(self):
        super().test_init()

        dut = self.make_dut()

        # ScrolledWindow-specific properties should be registered.
        for _property in ScrolledWindow._SCROLLEDWINDOW_PROPERTIES:
            assert _property in dut.dic_properties
        # ScrolledWindow-specific signals should be registered.
        for _signal in ScrolledWindow._SCROLLEDWINDOW_SIGNALS:
            assert _signal in dut.dic_handler_id

    @pytest.mark.unit
    def test_init_with_child(self):
        """__init__() should create a ScrolledWindow with a Gtk.Fixed child widget."""
        dut = self.make_dut(child=Gtk.Fixed())

        assert isinstance(dut, ScrolledWindow)
        assert isinstance(dut.get_children()[0], Gtk.Viewport)
        assert isinstance(dut.get_children()[0].get_children()[0], Gtk.Fixed)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """do_set_properties() should set the default properties of a ScrolledWindow
        when an empty WidgetProperties is passed to the method."""
        dut = self.make_dut()
        dut.do_set_properties(WidgetProperties())

        assert dut.get_property("border_width") == 0
        assert isinstance(dut.get_property("hadjustment"), Gtk.Adjustment)
        assert dut.get_property("hscrollbar_policy") == Gtk.PolicyType.AUTOMATIC
        assert dut.get_property("kinetic_scrolling")
        assert dut.get_property("max_content_height") == -1
        assert dut.get_property("max_content_width") == -1
        assert dut.get_property("min_content_height") == -1
        assert dut.get_property("min_content_width") == -1
        assert dut.get_property("overlay_scrolling")
        assert not dut.get_property("propagate_natural_height")
        assert not dut.get_property("propagate_natural_width")
        assert dut.get_property("shadow_type") == Gtk.ShadowType.NONE
        assert isinstance(dut.get_property("vadjustment"), Gtk.Adjustment)
        assert dut.get_property("vscrollbar_policy") == Gtk.PolicyType.AUTOMATIC
        assert dut.get_property("window_placement") == Gtk.CornerType.TOP_LEFT
        assert dut.get_property("tooltip-markup") == (
            "Missing tooltip, please file an issue to have one added."
        )
        assert dut.get_property("visible")
        assert dut.get_property("width-request") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """do_set_properties() should set the properties of a ScrolledWindow to the
        values found in the passed WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            WidgetProperties(
                kinetic_scrolling=False,
                propagate_natural_height=True,
                propagate_natural_width=True,
                shadow_type=Gtk.ShadowType.ETCHED_OUT,
            )
        )

        assert not dut.get_property("kinetic_scrolling")
        assert dut.get_property("propagate_natural_height")
        assert dut.get_property("propagate_natural_width")
        assert dut.get_property("shadow_type") == Gtk.ShadowType.ETCHED_OUT
