"""Test module for the GTK3CellRendererPixbuf class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererPixbuf

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_RENDERER_HANDLER_IDS,
    EXPECTED_CELL_RENDERER_METHODS,
    EXPECTED_CELL_RENDERER_PROPERTIES,
    EXPECTED_CELLRENDERERPIXBUF_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CellRendererPixbuf(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererPixbuf class."""

    widget_class = GTK3CellRendererPixbuf
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_CELL_RENDERER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_CELL_RENDERER_METHODS
    expected_properties = (
        EXPECTED_CELL_RENDERER_PROPERTIES | EXPECTED_CELLRENDERERPIXBUF_PROPERTIES
    )

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
        assert dut.do_get_attribute("x_pos") is None
        assert dut.do_get_attribute("y_pos") is None

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("gicon") is None
        assert dut.do_get_property("icon_name") is None
        assert dut.do_get_property("pixbuf") is None
        assert dut.do_get_property("pixbuf_expander_closed") is None
        assert dut.do_get_property("pixbuf_expander_open") is None
        assert dut.do_get_property("stock_detail") is None
        assert dut.do_get_property("stock_size") == 1
        assert dut.do_get_property("surface") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _pixbuf = GdkPixbuf.Pixbuf()
        _pixbuf_closed = GdkPixbuf.Pixbuf()
        _pixbuf_open = GdkPixbuf.Pixbuf()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                icon_name="gicon the great",
                pixbuf=_pixbuf,
                pixbuf_expander_closed=_pixbuf_closed,
                pixbuf_expander_open=_pixbuf_open,
                stock_size=22,
            )
        )

        assert dut.do_get_property("gicon") is None
        assert dut.do_get_property("icon_name") == "gicon the great"
        assert dut.do_get_property("pixbuf") == _pixbuf
        assert dut.do_get_property("pixbuf_expander_closed") == _pixbuf_closed
        assert dut.do_get_property("pixbuf_expander_open") == _pixbuf_open
        assert dut.do_get_property("stock_detail") is None
        assert dut.do_get_property("stock_size") == 22
        assert dut.do_get_property("surface") is None
