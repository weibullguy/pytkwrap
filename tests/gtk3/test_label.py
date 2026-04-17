# pylint: skip-file
# type: ignore
# -*- coding: utf-8 -*-
#
#       tests.gtk3.test_label.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3Label module algorithms and models."""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.label import GTK3Label, do_make_label_group
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests


@pytest.mark.integration
def test_do_make_label_group():
    """Should return the maximum x-position and the list of GTK3Labels created."""
    _test_labels = ["This", "is", "a", "list", "of", "labels"]
    _max_x, _lst_labels = do_make_label_group(_test_labels)

    assert isinstance(_lst_labels[0], GTK3Label)
    assert isinstance(_lst_labels[1], GTK3Label)
    assert isinstance(_lst_labels[2], GTK3Label)
    assert isinstance(_lst_labels[3], GTK3Label)
    assert isinstance(_lst_labels[4], GTK3Label)
    assert isinstance(_lst_labels[5], GTK3Label)
    assert _max_x == 48


@pytest.mark.order(4)
class TestGTK3Label(BaseGTK3DataWidgetTests):
    """Test class for the GTK3Label."""

    widget_class = GTK3Label
    expected_default_height = 25
    expected_default_value = "..."
    expected_default_width = 200

    def make_dut(self, text="Test Label Text"):
        """Create a device under test for the GTK3Label."""
        return self.widget_class(text)

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3Label with default values for attributes."""
        super().test_init()

        dut = self.make_dut()

        assert isinstance(dut, GTK3Label)
        assert dut._DEFAULT_HEIGHT == 25
        assert dut._DEFAULT_WIDTH == 200
        # All handler IDs should start at -1.
        assert all(_hid == -1 for _hid in dut.dic_handler_id.values())
        # GTK3Label-specific attributes should be registered.
        for _attribute in GTK3Label._GTK3_LABEL_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        # GTK3Label-specific properties should be registered.
        for _property in GTK3Label._GTK3_LABEL_PROPERTIES:
            assert _property in dut.dic_properties
        # GTK3Label-specific signals should be registered.
        for _signal in GTK3Label._GTK3_LABEL_SIGNALS:
            assert _signal in dut.dic_handler_id
        assert dut.font_allow_breaks == "false"
        assert dut.font_bgalpha == "100%"
        assert dut.font_bgcolor == "white"
        assert dut.font_description == ""
        assert dut.font_family == "Sans, Serif, Monospace"
        assert dut.font_features == ""
        assert dut.font_fgalpha == "100%"
        assert dut.font_fgcolor == "black"
        assert dut.font_gravity == "auto"
        assert dut.font_gravity_hint == "natural"
        assert dut.font_insert_hyphens == "true"
        assert dut.font_lang == "en_US"
        assert dut.font_letter_spacing == ""
        assert dut.font_overline == "false"
        assert dut.font_overline_color == "black"
        assert dut.font_rise == "0pt"
        assert dut.font_scale == ""
        assert dut.font_size == "12pt"
        assert dut.font_stretch == "normal"
        assert dut.font_strikethrough == "false"
        assert dut.font_strikethrough_color == "black"
        assert dut.font_style == "normal"
        assert dut.font_underline == "false"
        assert dut.font_underline_color == "black"
        assert dut.font_variant == "normal"
        assert dut.font_weight == "normal"

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set the default attributes of a GTK3Label when passed an empty
        WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3DataWidgetAttributes())

        assert dut.font_allow_breaks == "false"
        assert dut.font_bgalpha == "100%"
        assert dut.font_bgcolor == "white"
        assert dut.font_description == ""
        assert dut.font_family == "Sans, Serif, Monospace"
        assert dut.font_features == ""
        assert dut.font_fgalpha == "100%"
        assert dut.font_fgcolor == "black"
        assert dut.font_gravity == "auto"
        assert dut.font_gravity_hint == "natural"
        assert dut.font_insert_hyphens == "true"
        assert dut.font_lang == "en_US"
        assert dut.font_letter_spacing == ""
        assert dut.font_overline == "false"
        assert dut.font_overline_color == "black"
        assert dut.font_rise == "0pt"
        assert dut.font_scale == ""
        assert dut.font_size == "12pt"
        assert dut.font_stretch == "normal"
        assert dut.font_strikethrough == "false"
        assert dut.font_strikethrough_color == "black"
        assert dut.font_style == "normal"
        assert dut.font_underline == "false"
        assert dut.font_underline_color == "black"
        assert dut.font_variant == "normal"
        assert dut.font_weight == "normal"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """do_set_attributes() should set the attributes of a Label."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3DataWidgetAttributes(
                font_allow_breaks="true",
                font_bgalpha="50%",
                font_bgcolor="blue",
                font_fgalpha="50%",
                font_fgcolor="red",
                font_family="Arial",
                font_lang="en_GB",
                font_letter_spacing="0",
                font_gravity="west",
                font_gravity_hint="strong",
                font_insert_hyphens="false",
                font_overline="true",
                font_overline_color="purple",
                font_rise="2pt",
                font_scale="small-caps",
                font_size="16pt",
                font_stretch="condensed",
                font_style="italic",
                font_strikethrough="true",
                font_strikethrough_color="green",
                font_underline="true",
                font_underline_color="yellow",
                font_variant="title-caps",
                font_weight="bold",
            )
        )
        assert dut.font_allow_breaks == "true"
        assert dut.font_bgalpha == "50%"
        assert dut.font_bgcolor == "blue"
        assert dut.font_description == ""
        assert dut.font_family == "Arial"
        assert dut.font_features == ""
        assert dut.font_fgalpha == "50%"
        assert dut.font_fgcolor == "red"
        assert dut.font_gravity == "west"
        assert dut.font_gravity_hint == "strong"
        assert dut.font_insert_hyphens == "false"
        assert dut.font_lang == "en_GB"
        assert dut.font_letter_spacing == "0"
        assert dut.font_overline == "true"
        assert dut.font_overline_color == "purple"
        assert dut.font_rise == "2pt"
        assert dut.font_scale == "small-caps"
        assert dut.font_size == "16pt"
        assert dut.font_stretch == "condensed"
        assert dut.font_strikethrough == "true"
        assert dut.font_strikethrough_color == "green"
        assert dut.font_style == "italic"
        assert dut.font_underline == "true"
        assert dut.font_underline_color == "yellow"
        assert dut.font_variant == "title-caps"
        assert dut.font_weight == "bold"

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should retrieve the value of the passed attribute."""
        super().test_do_get_attribute()

        dut = self.make_dut()

        assert dut.do_get_attribute("font_allow_breaks") == "false"
        assert dut.do_get_attribute("font_bgalpha") == "100%"
        assert dut.do_get_attribute("font_bgcolor") == "white"
        assert dut.do_get_attribute("font_description") == ""
        assert dut.do_get_attribute("font_family") == "Sans, Serif, Monospace"
        assert dut.do_get_attribute("font_features") == ""
        assert dut.do_get_attribute("font_fgalpha") == "100%"
        assert dut.do_get_attribute("font_fgcolor") == "black"
        assert dut.do_get_attribute("font_gravity") == "auto"
        assert dut.do_get_attribute("font_gravity_hint") == "natural"
        assert dut.do_get_attribute("font_insert_hyphens") == "true"
        assert dut.do_get_attribute("font_overline") == "false"
        assert dut.do_get_attribute("font_overline_color") == "black"
        assert dut.do_get_attribute("font_rise") == "0pt"
        assert dut.do_get_attribute("font_scale") == ""
        assert dut.do_get_attribute("font_size") == "12pt"
        assert dut.do_get_attribute("font_stretch") == "normal"
        assert dut.do_get_attribute("font_strikethrough") == "false"
        assert dut.do_get_attribute("font_strikethrough_color") == "black"
        assert dut.do_get_attribute("font_underline") == "false"
        assert dut.do_get_attribute("font_underline_color") == "black"
        assert dut.do_get_attribute("font_variant") == "normal"
        assert dut.do_get_attribute("font_weight") == "normal"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties of a GTK3Label when no keywords are passed
        to the method."""
        dut = self.make_dut("Test Label Text")
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("angle") == 0.0
        assert dut.get_property("attributes") is None
        assert dut.get_property("ellipsize") == Pango.EllipsizeMode.NONE
        assert dut.get_property("justify") == Gtk.Justification.LEFT
        assert dut.get_property("label") == ""
        assert not dut.get_property("wrap")
        assert dut.get_property("wrap_mode") == Pango.WrapMode.WORD
        assert dut.get_property("lines") == -1
        assert dut.get_property("max_width_chars") == -1
        assert dut.get_property("mnemonic_widget") is None
        assert not dut.get_property("selectable")
        assert not dut.get_property("single_line_mode")
        assert dut.get_property("track_visited_links")
        assert not dut.get_property("use_markup")
        assert not dut.get_property("use_underline")
        assert dut.get_property("width_chars") == -1
        assert dut.get_property("xalign") == pytest.approx(0.05)
        assert dut.get_property("yalign") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3Label."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                angle=90,
                ellipsize=Pango.EllipsizeMode.END,
                justify=Gtk.Justification.CENTER,
                label="<b><span>Test _Label Text</span></b>",
                lines=3,
                max_width_chars=25,
                selectable=True,
                single_line_mode=True,
                track_visited_links=False,
                use_markup=True,
                use_underline=True,
                width_chars=50,
                wrap=True,
                wrap_mode=Pango.WrapMode.CHAR,
                xalign=0.5,
                yalign=0.25,
            )
        )

        assert dut.get_property("angle") == 90.0
        assert dut.get_property("attributes") is None
        assert dut.get_property("ellipsize") == Pango.EllipsizeMode.END
        assert dut.get_property("justify") == Gtk.Justification.CENTER
        assert dut.get_property("label") == "<b><span>Test _Label Text</span></b>"
        assert dut.get_property("wrap")
        assert dut.get_property("wrap_mode") == Pango.WrapMode.CHAR
        assert dut.get_property("lines") == 3
        assert dut.get_property("max_width_chars") == 25
        assert dut.get_property("mnemonic_widget") is None
        assert dut.get_property("selectable")
        assert dut.get_property("single_line_mode")
        assert not dut.get_property("track_visited_links")
        assert dut.get_property("use_markup")
        assert dut.get_property("use_underline")
        assert dut.get_property("width_chars") == 50
        assert dut.get_property("xalign") == 0.5
        assert dut.get_property("yalign") == 0.25

    @pytest.mark.unit
    def test_do_set_properties_justify_right(self):
        """Should set the properties of a GTK3Label."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                justify=Gtk.Justification.RIGHT,
            )
        )

        assert dut.get_property("justify") == Gtk.Justification.RIGHT
        assert dut.get_property("xalign") == pytest.approx(0.95)

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3Label with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("focus-in-event", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert dut.get_label() == "Test Package"
        assert dut.get_text() == "Test Package"

    @pytest.mark.unit
    def test_do_update_use_underline(self):
        """Should update the GTK3Label with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_properties(GTK3WidgetProperties(use_underline=True))
        dut.do_set_callbacks("focus-in-event", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": "_Test Package"})

        assert dut.get_label() == "_Test Package"
        assert dut.get_text() == "Test Package"

    @pytest.mark.unit
    def test_do_update_use_markup(self):
        """Should update the GTK3Label with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_properties(GTK3WidgetProperties(use_markup=True))
        dut.do_set_callbacks("focus-in-event", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage(
            "rootTopic",
            package={"test_field": "<span foreground='red'>Test Package</span>"},
        )

        assert dut.get_label() == "<span foreground='red'>Test Package</span>"
        assert dut.get_text() == "Test Package"

    @pytest.mark.unit
    def test_do_update_use_underline_and_markup(self):
        """Should update the GTK3Label with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_properties(
            GTK3WidgetProperties(
                use_underline=True,
                use_markup=True,
            )
        )
        dut.do_set_callbacks("focus-in-event", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage(
            "rootTopic",
            package={"test_field": "<span foreground='red'>Test _Package</span>"},
        )

        assert dut.get_label() == "<span foreground='red'>Test _Package</span>"
        assert dut.get_text() == "Test Package"

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should not update the GTK3Label with the data package value is None."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("focus-in-event", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage(
            "rootTopic",
            package={"test_field": None},
        )

        assert dut.get_label() == "Test Label Text"
        assert dut.get_text() == "Test Label Text"

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Should not update the GTK3Label when the data package key doesn't mathc the
        field."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks("focus-in-event", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage(
            "rootTopic",
            package={"fld_name": "New Label Text"},
        )

        assert dut.get_label() == "Test Label Text"
        assert dut.get_text() == "Test Label Text"

    @pytest.mark.unit
    def test_do_set_font_description_default(self):
        """Should set the default font description when passed no arguments."""
        dut = self.make_dut()
        dut.do_set_font_description()

        assert (
            dut.font_description == "<span allow_breaks=false "
            "bgalpha=100% "
            "bgcolor=white "
            "face=Sans, Serif, Monospace "
            "font_features= "
            "fgalpha=100% "
            "fgcolor=black "
            "gravity=auto "
            "gravity_hint=natural "
            "insert_hyphen=true "
            "lang=en_US "
            "letter_spacing= "
            "overline=false "
            "overline_color=black "
            "rise=0pt "
            "font_scale= "
            "size=12pt "
            "stretch=normal "
            "strikethrough=false "
            "strikethrough_color=black "
            "style=normal "
            "underline=false "
            "underline_color=black "
            "variant=normal "
            "weight=normal"
        )

    @pytest.mark.unit
    def test_do_set_font_description(self):
        """Should set the default font description values to those in the arguments."""
        dut = self.make_dut()
        dut.font_bgalpha = "50%"
        dut.font_bgcolor = "yellow"
        dut.font_family = "Helvetica"
        dut.font_overline = "true"
        dut.do_set_font_description()

        assert (
            dut.font_description == "<span allow_breaks=false "
            "bgalpha=50% "
            "bgcolor=yellow "
            "face=Helvetica "
            "font_features= "
            "fgalpha=100% "
            "fgcolor=black "
            "gravity=auto "
            "gravity_hint=natural "
            "insert_hyphen=true "
            "lang=en_US "
            "letter_spacing= "
            "overline=true "
            "overline_color=black "
            "rise=0pt "
            "font_scale= "
            "size=12pt "
            "stretch=normal "
            "strikethrough=false "
            "strikethrough_color=black "
            "style=normal "
            "underline=false "
            "underline_color=black "
            "variant=normal "
            "weight=normal"
        )

    @pytest.mark.unit
    def test_do_set_font_description_preserves_existing(self):
        """Should make no changes to the font description when already set and passed no
        arguments."""
        dut = self.make_dut()
        dut.font_description = "<span face=Arial size=12pt"
        dut.do_set_font_description()

        assert dut.font_description == "<span face=Arial size=12pt"
