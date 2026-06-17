"""Test module for the GTK3CellRendererText class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererText

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_RENDERER_HANDLER_IDS,
    EXPECTED_CELL_RENDERER_METHODS,
    EXPECTED_CELL_RENDERER_PROPERTIES,
    EXPECTED_CELLRENDERERTEXT_HANDLER_IDS,
    EXPECTED_CELLRENDERERTEXT_METHODS,
    EXPECTED_CELLRENDERERTEXT_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CellRenderer(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererText class."""

    widget_class = GTK3CellRendererText
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_CELL_RENDERER_HANDLER_IDS
        | EXPECTED_CELLRENDERERTEXT_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_CELL_RENDERER_METHODS
        + EXPECTED_CELLRENDERERTEXT_METHODS
    )
    expected_properties = (
        EXPECTED_CELL_RENDERER_PROPERTIES | EXPECTED_CELLRENDERERTEXT_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("align_set")
        assert dut.do_get_property("alignment") == Pango.Alignment.LEFT
        assert dut.do_get_property("attributes") is None
        assert dut.do_get_property("background") is None
        assert dut.do_get_property("background_rgba") is None
        assert not dut.do_get_property("background_set")
        assert not dut.do_get_property("editable")
        assert not dut.do_get_property("editable_set")
        assert dut.do_get_property("ellipsize") == Pango.EllipsizeMode.NONE
        assert not dut.do_get_property("ellipsize_set")
        assert dut.do_get_property("family") is None
        assert not dut.do_get_property("family_set")
        assert dut.do_get_property("font") is None
        assert dut.do_get_property("font_desc") is None
        assert dut.do_get_property("foreground") is None
        assert dut.do_get_property("foreground_rgba") is None
        assert not dut.do_get_property("foreground_set")
        assert dut.do_get_property("language") is None
        assert not dut.do_get_property("language_set")
        assert dut.do_get_property("markup") is None
        assert dut.do_get_property("max_width_chars") == -1
        assert dut.do_get_property("placeholder_text") is None
        assert dut.do_get_property("rise") == 0
        assert not dut.do_get_property("rise_set")
        assert dut.do_get_property("scale") == 1.0
        assert not dut.do_get_property("scale_set")
        assert not dut.do_get_property("single_paragraph_mode")
        assert dut.do_get_property("size") == 0
        assert dut.do_get_property("size_points") == 0.0
        assert not dut.do_get_property("size_set")
        assert dut.do_get_property("stretch") == Pango.Stretch.NORMAL
        assert not dut.do_get_property("stretch_set")
        assert not dut.do_get_property("strikethrough")
        assert not dut.do_get_property("strikethrough_set")
        assert dut.do_get_property("style") == Pango.Style.NORMAL
        assert not dut.do_get_property("style_set")
        assert dut.do_get_property("text") is None
        assert dut.do_get_property("underline") == Pango.Underline.NONE
        assert not dut.do_get_property("underline_set")
        assert dut.do_get_property("variant") == Pango.Variant.NORMAL
        assert not dut.do_get_property("variant_set")
        assert dut.do_get_property("weight") == 400
        assert not dut.do_get_property("weight_set")
        assert dut.do_get_property("width_chars") == -1
        assert dut.do_get_property("wrap_mode") == Pango.WrapMode.CHAR
        assert dut.do_get_property("wrap_width") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                align_set=True,
                alignment=Pango.Alignment.RIGHT,
                attributes=None,
                background="pink",
                background_rgba=None,
                background_set=True,
                editable=True,
                editable_set=True,
                ellipsize=Pango.EllipsizeMode.MIDDLE,
                ellipsize_set=True,
                family="Arial",
                family_set=True,
                font="Arial 12pt",
                font_desc=None,
                foreground="red",
                foreground_rgba=None,
                foreground_set=True,
                language=None,
                language_set=True,
                markup="<b>Test Markup</b>",
                max_width_chars=100,
                placeholder_text="Test Placeholder Text",
                rise=5,
                rise_set=True,
                scale=1.2,
                scale_set=True,
                single_paragraph_mode=True,
                size=10,
                size_points=10.0,
                size_set=True,
                stretch=Pango.Stretch.EXPANDED,
                stretch_set=True,
                strikethrough=True,
                strikethrough_set=True,
                style=Pango.Style.ITALIC,
                style_set=True,
                text="Test Text",
                underline=Pango.Underline.DOUBLE,
                underline_set=True,
                variant=Pango.Variant.SMALL_CAPS,
                variant_set=True,
                weight=600,
                weight_set=True,
                width_chars=50,
                wrap_mode=Pango.WrapMode.WORD_CHAR,
                wrap_width=25,
            )
        )

        assert dut.do_get_property("align_set")
        assert dut.do_get_property("alignment") == Pango.Alignment.RIGHT
        assert dut.do_get_property("attributes") is None
        assert dut.do_get_property("background") == "pink"
        assert dut.do_get_property("background_rgba") is None
        assert dut.do_get_property("background_set")
        assert dut.do_get_property("editable")
        assert dut.do_get_property("editable_set")
        assert dut.do_get_property("ellipsize") == Pango.EllipsizeMode.MIDDLE
        assert dut.do_get_property("ellipsize_set")
        assert dut.do_get_property("family") == "Arial"
        assert dut.do_get_property("family_set")
        assert dut.do_get_property("font") == "Arial 12pt"
        assert dut.do_get_property("font_desc") is None
        assert dut.do_get_property("foreground") == "red"
        assert dut.do_get_property("foreground_rgba") is None
        assert dut.do_get_property("foreground_set")
        assert dut.do_get_property("language") is None
        assert dut.do_get_property("language_set")
        assert dut.do_get_property("markup") == "<b>Test Markup</b>"
        assert dut.do_get_property("max_width_chars") == 100
        assert dut.do_get_property("placeholder_text") == "Test Placeholder Text"
        assert dut.do_get_property("rise") == 5
        assert dut.do_get_property("rise_set")
        assert dut.do_get_property("scale") == 1.2
        assert dut.do_get_property("scale_set")
        assert dut.do_get_property("single_paragraph_mode")
        assert dut.do_get_property("size") == 10
        assert dut.do_get_property("size_points") == 10.0
        assert dut.do_get_property("size_set")
        assert dut.do_get_property("stretch") == Pango.Stretch.EXPANDED
        assert dut.do_get_property("stretch_set")
        assert dut.do_get_property("strikethrough")
        assert dut.do_get_property("strikethrough_set")
        assert dut.do_get_property("style") == Pango.Style.ITALIC
        assert dut.do_get_property("style_set")
        assert dut.do_get_property("text") == "Test Text"
        assert dut.do_get_property("underline") == Pango.Underline.DOUBLE
        assert dut.do_get_property("underline_set")
        assert dut.do_get_property("variant") == Pango.Variant.SMALL_CAPS
        assert dut.do_get_property("variant_set")
        assert dut.do_get_property("weight") == 600
        assert dut.do_get_property("weight_set")
        assert dut.do_get_property("width_chars") == 50
        assert dut.do_get_property("wrap_mode") == Pango.WrapMode.WORD_CHAR
        assert dut.do_get_property("wrap_width") == 25
