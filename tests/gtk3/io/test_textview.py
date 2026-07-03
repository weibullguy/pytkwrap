"""Test module for the GTK3TextView class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import date

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.io import GTK3TextView
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3DataWidgetTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.container.constants import (
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.io.constants import (
    EXPECTED_TEXTVIEW_ATTRIBUTES,
    EXPECTED_TEXTVIEW_HANDLER_IDS,
    EXPECTED_TEXTVIEW_METHODS,
    EXPECTED_TEXTVIEW_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3TextView(BaseGTK3DataWidgetTests):
    """Test class for the GTK3TextView class."""

    widget_class = GTK3TextView
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_TEXTVIEW_ATTRIBUTES
    )
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TEXTVIEW_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_TEXTVIEW_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TEXTVIEW_PROPERTIES
    )
    expected_set_value = [
        [14.92, "14.92"],
        [1492, "1492"],
        ["Test TextView Value", "Test TextView Value"],
    ]
    expected_set_value_wrong_types = [
        True,
        date(2020, 1, 1),
        Gtk.Label(),
        ("A", "Tuple"),
        None,
    ]

    def make_dut(self, buffer=Gtk.TextBuffer()):
        return self.widget_class(buffer)

    @pytest.mark.unit
    def test_init_with_buffer(self):
        """Should create a GTK3TextView with default attribute values."""
        _buffer = Gtk.TextBuffer()

        dut = self.make_dut(buffer=_buffer)

        assert dut.get_property("buffer") == _buffer
        assert dut.get_buffer() == _buffer

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
        assert dut.do_get_attribute("default_value") == ""
        assert dut.do_get_attribute("edit_signal") == "changed"
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
        """Should set attributes to the values passed in a GTK3WidgetAttributes dict."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                data_type=str,
                default_value="Default TextView Value",
                edit_signal="apply-tag",
                font_description=None,
                format="",
                index=10,
                listen_topic="tvw_changed",
                send_topic="txtvw_changed",
                x_pos=50,
                y_pos=100,
            )
        )

        assert dut.do_get_attribute("data_type") == str
        assert dut.do_get_attribute("default_value") == "Default TextView Value"
        assert dut.do_get_attribute("edit_signal") == "apply-tag"
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == ""
        assert dut.do_get_attribute("index") == 10
        assert dut.do_get_attribute("listen_topic") == "tvw_changed"
        assert dut.do_get_attribute("send_topic") == "txtvw_changed"
        assert dut.do_get_attribute("x_pos") == 50
        assert dut.do_get_attribute("y_pos") == 100

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("accepts_tab")
        assert dut.do_get_property("bottom_margin") == 0
        assert dut.do_get_property("buffer") is None
        assert dut.do_get_property("cursor_visible")
        assert dut.do_get_property("editable")
        assert dut.do_get_property("im_module") is None
        assert dut.do_get_property("indent") == 0
        assert dut.do_get_property("input_hints") == Gtk.InputHints.NONE
        assert dut.do_get_property("input_purpose") == Gtk.InputPurpose.FREE_FORM
        assert dut.do_get_property("justification") == Gtk.Justification.LEFT
        assert dut.do_get_property("left_margin") == 0
        assert not dut.do_get_property("monospace")
        assert not dut.do_get_property("overwrite")
        assert dut.do_get_property("pixels_above_lines") == 0
        assert dut.do_get_property("pixels_below_lines") == 0
        assert dut.do_get_property("pixels_inside_wrap") == 0
        assert not dut.do_get_property("populate_all")
        assert dut.do_get_property("right_margin") == 0
        assert dut.do_get_property("tabs") is None
        assert dut.do_get_property("top_margin") == 0
        assert dut.do_get_property("wrap_mode") == Gtk.WrapMode.NONE

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _buffer = Gtk.TextBuffer()
        _tab_array = Pango.TabArray(0)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                accepts_tab=False,
                bottom_margin=10,
                buffer=_buffer,
                cursor_visible=False,
                editable=False,
                im_module=None,
                indent=20,
                input_hints=Gtk.InputHints.SPELLCHECK,
                input_purpose=Gtk.InputPurpose.ALPHA,
                justification=Gtk.Justification.CENTER,
                left_margin=30,
                monospace=True,
                overwrite=True,
                pixels_above_lines=40,
                pixels_below_lines=50,
                pixels_inside_wrap=60,
                populate_all=True,
                right_margin=70,
                tabs=_tab_array,
                top_margin=80,
                wrap_mode=Gtk.WrapMode.WORD_CHAR,
            )
        )

        assert not dut.get_property("accepts_tab")
        assert not dut.get_accepts_tab()
        assert dut.get_property("bottom_margin") == 10
        assert dut.get_bottom_margin() == 10
        assert dut.get_property("buffer") == _buffer
        assert dut.get_buffer() == _buffer
        assert not dut.get_property("cursor_visible")
        assert not dut.get_cursor_visible()
        assert not dut.get_property("editable")
        assert not dut.get_editable()
        assert dut.get_property("im_module") is None
        assert dut.get_property("indent") == 20
        assert dut.get_indent() == 20
        assert dut.get_property("input_hints") == Gtk.InputHints.SPELLCHECK
        assert dut.get_input_hints() == Gtk.InputHints.SPELLCHECK
        assert dut.get_property("input_purpose") == Gtk.InputPurpose.ALPHA
        assert dut.get_input_purpose() == Gtk.InputPurpose.ALPHA
        assert dut.get_property("justification") == Gtk.Justification.CENTER
        assert dut.get_justification() == Gtk.Justification.CENTER
        assert dut.get_property("left_margin") == 30
        assert dut.get_left_margin() == 30
        assert dut.get_property("monospace")
        assert dut.get_monospace()
        assert dut.get_property("overwrite")
        assert dut.get_overwrite()
        assert dut.get_property("pixels_above_lines") == 40
        assert dut.get_pixels_above_lines() == 40
        assert dut.get_property("pixels_below_lines") == 50
        assert dut.get_pixels_below_lines() == 50
        assert dut.get_property("pixels_inside_wrap") == 60
        assert dut.get_pixels_inside_wrap() == 60
        assert dut.get_property("populate_all")
        assert dut.get_property("right_margin") == 70
        assert dut.get_right_margin() == 70
        assert isinstance(dut.get_property("tabs"), Pango.TabArray)
        assert isinstance(dut.get_tabs(), Pango.TabArray)
        assert dut.get_property("top_margin") == 80
        assert dut.get_top_margin() == 80
        assert dut.get_property("wrap_mode") == Gtk.WrapMode.WORD_CHAR
        assert dut.get_wrap_mode() == Gtk.WrapMode.WORD_CHAR
