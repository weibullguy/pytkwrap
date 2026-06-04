"""Test module for the GTK3Widget class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.order(3)
class TestGTK3Widget(BaseGTK3GObjectTests):
    """Test class for the GTK3Widget class."""

    widget_class = GTK3Widget
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS
    expected_properties = EXPECTED_WIDGET_PROPERTIES

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("axis") is None
        assert dut.do_get_attribute("canvas") is None
        assert dut.do_get_attribute("column_types") is None
        assert dut.do_get_attribute("data_type") is None
        assert dut.do_get_attribute("default_value") is None
        assert dut.do_get_attribute("edit_signal") is None
        assert dut.do_get_attribute("figure") is None
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") is None
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen-topic"
        assert dut.do_get_attribute("n_columns") is None
        assert dut.do_get_attribute("n_rows") is None
        assert dut.do_get_attribute("send_topic") == "send-topic"
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                x_pos=25,
                y_pos=100,
            )
        )

        assert dut.do_get_attribute("x_pos") == 25
        assert dut.do_get_attribute("y_pos") == 100

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("app_paintable")
        assert not dut.do_get_property("can_default")
        assert not dut.do_get_property("can_focus")
        assert not dut.do_get_property("composite_child")
        assert (
            dut.do_get_property("events")
            == Gdk.EventMask.ALL_EVENTS_MASK  # pylint: disable=no-member
        )
        assert not dut.do_get_property("expand")
        assert dut.do_get_property("focus_on_click")
        assert dut.do_get_property("halign") == Gtk.Align.FILL
        assert not dut.do_get_property("has_default")
        assert not dut.do_get_property("has_focus")
        assert not dut.do_get_property("has_tooltip")
        assert dut.do_get_property("height_request") == -1
        assert not dut.do_get_property("hexpand")
        assert not dut.do_get_property("hexpand_set")
        assert not dut.do_get_property("is_focus")
        assert dut.do_get_property("margin") == 0
        assert dut.do_get_property("margin_bottom") == 0
        assert dut.do_get_property("margin_end") == 0
        assert dut.do_get_property("margin_start") == 0
        assert dut.do_get_property("margin_top") == 0
        assert dut.do_get_property("name") == "pytkwrap GTK3 widget"
        assert not dut.do_get_property("no_show_all")
        assert dut.do_get_property("opacity") == 1.0
        assert dut.do_get_property("parent") is None
        assert not dut.do_get_property("receives_default")
        assert dut.do_get_property("scale_factor") == 1
        assert dut.do_get_property("sensitive")
        assert dut.do_get_property("style") is None
        assert (
            dut.do_get_property("tooltip_markup")
            == "Missing tooltip, please file an issue to have one added."
        )
        assert (
            dut.do_get_property("tooltip_text")
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut.do_get_property("valign") == Gtk.Align.FILL
        assert not dut.do_get_property("vexpand")
        assert not dut.do_get_property("vexpand_set")
        assert not dut.do_get_property("visible")
        assert dut.do_get_property("width_request") == -1
        assert dut.do_get_property("window") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                app_paintable=True,
                can_default=True,
                can_focus=True,
                composite_child=True,
                events=Gdk.EventMask.KEY_PRESS_MASK,  # pylint: disable=no-member
                expand=True,
                focus_on_click=False,
                halign=Gtk.Align.CENTER,
                has_default=True,
                has_focus=True,
                has_tooltip=True,
                height_request=50,
                hexpand=True,
                hexpand_set=True,
                is_focus=True,
                margin=10,
                margin_bottom=1,
                margin_end=2,
                margin_start=3,
                margin_top=4,
                name="Test GTK3 widget",
                no_show_all=True,
                opacity=0.87,
                receives_default=True,
                scale_factor=5,
                sensitive=False,
                tooltip_markup="New tooltip.",
                tooltip_text="New tooltip.",
                valign=Gtk.Align.BASELINE,
                vexpand=True,
                vexpand_set=True,
                visible=True,
                width_request=100,
            )
        )

        assert dut.do_get_property("app_paintable")
        assert dut.do_get_property("can_default")
        assert dut.do_get_property("can_focus")
        assert dut.do_get_property("composite_child")
        assert (
            dut.do_get_property("events")
            == Gdk.EventMask.KEY_PRESS_MASK  # pylint: disable=no-member
        )
        assert dut.do_get_property("expand")
        assert not dut.do_get_property("focus_on_click")
        assert dut.do_get_property("halign") == Gtk.Align.CENTER
        assert dut.do_get_property("has_default")
        assert dut.do_get_property("has_focus")
        assert dut.do_get_property("has_tooltip")
        assert dut.do_get_property("height_request") == 50
        assert dut.do_get_property("hexpand")
        assert dut.do_get_property("hexpand_set")
        assert dut.do_get_property("is_focus")
        assert dut.do_get_property("margin") == 10
        assert dut.do_get_property("margin_bottom") == 1
        assert dut.do_get_property("margin_end") == 2
        assert dut.do_get_property("margin_start") == 3
        assert dut.do_get_property("margin_top") == 4
        assert dut.do_get_property("name") == "Test GTK3 widget"
        assert dut.do_get_property("no_show_all")
        assert dut.do_get_property("opacity") == 0.87
        assert dut.do_get_property("parent") is None
        assert dut.do_get_property("receives_default")
        assert dut.do_get_property("scale_factor") == 5
        assert not dut.do_get_property("sensitive")
        assert dut.do_get_property("style") is None
        assert dut.do_get_property("tooltip_markup") == "New tooltip."
        assert dut.do_get_property("tooltip_text") == "New tooltip."
        assert dut.do_get_property("valign") == Gtk.Align.BASELINE
        assert dut.do_get_property("vexpand")
        assert dut.do_get_property("vexpand_set")
        assert dut.do_get_property("visible")
        assert dut.do_get_property("width_request") == 100
        assert dut.do_get_property("window") is None

    @pytest.mark.unit
    def test_do_set_properties_zero_height(self):
        """Should use _DEFAULT_HEIGHT when height_request is 0."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(height_request=0))

        assert (
            dut.dic_properties["height_request"] == self.expected_default_height
        )  # falls back to _DEFAULT_HEIGHT

    @pytest.mark.unit
    def test_do_set_properties_zero_width(self):
        """Should use _DEFAULT_WIDTH when width_request is 0."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(width_request=0))

        assert (
            dut.dic_properties["width_request"] == self.expected_default_width
        )  # falls back to _DEFAULT_WIDTH
