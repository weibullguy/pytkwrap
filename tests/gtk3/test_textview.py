# pylint: skip-file
# type: ignore
#
#       pytkwrap.gtk3.test_textview.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3TextView module algorithms and models."""

# Standard Library Imports
import sys
from io import StringIO

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.textview import GTK3TextView
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestTextView(BaseGTK3DataWidgetTests):
    """Test class for the TextView."""

    widget_class = GTK3TextView
    expected_default_height = 100
    expected_default_value = ""
    expected_default_width = 200
    expected_package = {0: {"test_field": "Test Text"}}

    def make_dut(self):
        """Create a device under test for the GTK3TextView."""
        return self.widget_class(Gtk.TextBuffer())

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3TextView with default values for attributes."""
        super().test_init()

        dut = self.make_dut()

        # TextView-specific properties should be registered.
        for _property in GTK3TextView._GTK3_TEXTVIEW_PROPERTIES:
            assert _property in dut.dic_properties
        # TextView-specific signals should be registered.
        for _signal in GTK3TextView._GTK3_TEXTVIEW_SIGNALS:
            assert _signal in dut.dic_handler_id
        assert dut.edit_signal == "changed"
        assert isinstance(dut.tag_bold, Gtk.TextTag)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties of a GTK3TextView when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("accepts-tab")
        assert dut.get_property("border-width") == 0
        assert dut.get_property("bottom-margin") == 0
        assert isinstance(dut.get_property("buffer"), Gtk.TextBuffer)
        assert dut.get_property("cursor-visible")
        assert dut.get_property("editable")
        assert isinstance(dut.get_property("hadjustment"), Gtk.Adjustment)
        assert dut.get_property("hscroll-policy") == Gtk.ScrollablePolicy.MINIMUM
        assert dut.get_property("im-module") is None
        assert dut.get_property("indent") == 0
        assert dut.get_property("input-hints") == Gtk.InputHints.NONE
        assert dut.get_property("input-purpose") == Gtk.InputPurpose.FREE_FORM
        assert dut.get_property("justification") == Gtk.Justification.LEFT
        assert dut.get_property("left-margin") == 0
        assert not dut.get_property("monospace")
        assert not dut.get_property("overwrite")
        assert dut.get_property("pixels-above-lines") == 0
        assert dut.get_property("pixels-below-lines") == 0
        assert dut.get_property("pixels-inside-wrap") == 0
        assert not dut.get_property("populate-all")
        assert dut.get_property("right-margin") == 0
        assert dut.get_property("tabs") is None
        assert dut.get_property("top-margin") == 0
        assert isinstance(dut.get_property("vadjustment"), Gtk.Adjustment)
        assert dut.get_property("vscroll-policy") == Gtk.ScrollablePolicy.MINIMUM
        assert dut.get_property("wrap-mode") == Gtk.WrapMode.NONE

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3TextView."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                accepts_tab=False,
                border_width=10,
                bottom_margin=10,
                buffer=None,
                cursor_visible=False,
                editable=False,
                hadjustment=None,
                height_request=700,
                hscroll_policy=Gtk.ScrollablePolicy.NATURAL,
                im_module=None,
                indent=5,
                input_hints=Gtk.InputHints.SPELLCHECK,
                input_purpose=Gtk.InputPurpose.ALPHA,
                justification=Gtk.Justification.FILL,
                left_margin=10,
                monospace=True,
                overwrite=False,
                pixels_above_lines=1,
                pixels_below_lines=2,
                pixels_inside_wrap=3,
                populate_all=False,
                right_margin=0,
                tabs=None,
                tooltip_markup="<b>Test TextView Tooltip.</b>",
                tooltip_text="Test TextView Tooltip.",
                top_margin=0,
                vadjustment=None,
                vscroll_policy=Gtk.ScrollablePolicy.NATURAL,
                width_request=1500,
                wrap_mode=Gtk.WrapMode.WORD,
            )
        )

        assert not dut.get_property("accepts-tab")
        assert dut.get_property("border-width") == 10
        assert dut.get_property("bottom-margin") == 10
        assert isinstance(dut.get_property("buffer"), Gtk.TextBuffer)
        assert not dut.get_property("cursor-visible")
        assert not dut.get_property("editable")
        assert isinstance(dut.get_property("hadjustment"), Gtk.Adjustment)
        assert dut.get_property("height-request") == 700
        assert dut.get_property("hscroll-policy") == Gtk.ScrollablePolicy.NATURAL
        assert dut.get_property("im-module") is None
        assert dut.get_property("indent") == 5
        assert dut.get_property("input-hints") == Gtk.InputHints.SPELLCHECK
        assert dut.get_property("input-purpose") == Gtk.InputPurpose.ALPHA
        assert dut.get_property("justification") == Gtk.Justification.FILL
        assert dut.get_property("left-margin") == 10
        assert dut.get_property("monospace")
        assert not dut.get_property("overwrite")
        assert dut.get_property("pixels-above-lines") == 1
        assert dut.get_property("pixels-below-lines") == 2
        assert dut.get_property("pixels-inside-wrap") == 3
        assert not dut.get_property("populate-all")
        assert dut.get_property("right-margin") == 0
        assert dut.get_property("tabs") is None
        assert dut.get_property("tooltip-markup") == "Test TextView Tooltip."
        assert dut.get_property("tooltip-text") == "Test TextView Tooltip."
        assert dut.get_property("top-margin") == 0
        assert isinstance(dut.get_property("vadjustment"), Gtk.Adjustment)
        assert dut.get_property("vscroll-policy") == Gtk.ScrollablePolicy.NATURAL
        assert dut.get_property("width-request") == 1500
        assert dut.get_property("wrap-mode") == Gtk.WrapMode.WORD

    @pytest.mark.unit
    def test_do_set_properties_tabs(self):
        """Should set the tabs property of a GTK3TextView."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                accepts_tab=True,
                tabs=Pango.TabArray(5, True),
            )
        )

        assert dut.get_property("accepts-tab")
        assert isinstance(dut.get_property("tabs"), Pango.TabArray)
        assert dut.get_property("tabs").get_size() == 5
        assert dut.get_property("tabs").get_positions_in_pixels()

    @pytest.mark.skip
    def test_do_set_callbacks(self):
        """Should set the callbacks for a GTK3TextView."""
        _signal_1 = "notify"
        _signal_2 = "changed"
        dut = self.make_dut()
        dut.do_set_callbacks(_signal_1, self.mock_callback)
        dut.do_set_callbacks(_signal_2, self.mock_callback)

        assert dut.dic_handler_id[_signal_1] != -1
        assert dut.dic_handler_id[_signal_2] != -1

        for signal, handler_id in dut.dic_handler_id.items():
            if signal not in (_signal_1, _signal_2):
                assert handler_id == -1, (
                    f"Expected {signal} to be -1, got {handler_id}."
                )

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3TextView with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert dut.do_get_value() == "Test Package"

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should update the GTK3TextView with the default value when passed None."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert dut.do_get_value() == ""

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Should raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert dut.do_get_value() == ""

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Should do nothing when the package field doesn't match."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.dic_properties["buffer"].set_text("Test Text")

        pub.sendMessage("rootTopic", package={"wrong_field": "Test Package"})

        assert dut.do_get_value() == "Test Text"

    @pytest.mark.unit
    def test_on_changed(self):
        """Should be called when the GTK3TextView text changes."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "textview_changed"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.dic_properties["buffer"].set_text("Test Text")

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Should raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "textview_changed"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.edit_signal = "edit_signal"
        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.dic_properties["buffer"].set_text("Test Text")
