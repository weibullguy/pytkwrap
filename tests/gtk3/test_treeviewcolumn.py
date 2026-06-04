"""Test module for the GTK3TreeViewColumn class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.cellrenderer import GTK3CellRenderer
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.treeviewcolumn import GTK3TreeViewColumn

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_TREEVIEW_COLUMN_HANDLER_IDS,
    EXPECTED_TREEVIEW_COLUMN_METHODS,
    EXPECTED_TREEVIEW_COLUMN_PROPERTIES,
)


@pytest.mark.order(3)
class TestGTK3TreeViewColumn(BaseGTK3GObjectTests):
    """Test class for the GTK3TreeViewColumn class."""

    widget_class = GTK3TreeViewColumn
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_TREEVIEW_COLUMN_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_TREEVIEW_COLUMN_METHODS
    expected_properties = EXPECTED_TREEVIEW_COLUMN_PROPERTIES

    def make_dut(self, title="", cell_renderer=None, cell_area=None):
        """Create a device under test for the GTK3TreeViewColumn."""
        return self.widget_class(title, cell_renderer, cell_area)

    @pytest.mark.unit
    def test_init_with_title(self):
        """Should create a GTK3TreeViewColumn with a title and default values for
        attributes."""
        dut = self.make_dut("Test Title")

        assert isinstance(dut, GTK3TreeViewColumn)
        assert dut.get_title() == "Test Title"
        assert dut.do_get_property("title") == "Test Title"

    @pytest.mark.unit
    def test_init_with_cell_renderer(self):
        """Should create a GTK3TreeViewColumn with a cell renderer and default values
        for attributes."""
        _cell_renderer = GTK3CellRenderer()
        dut = self.make_dut(cell_renderer=_cell_renderer)

        assert isinstance(dut, GTK3TreeViewColumn)
        assert dut.cell_get_position(_cell_renderer)[0] != 0
        assert dut.cell_get_position(_cell_renderer)[1] != 0

    @pytest.mark.unit
    def test_init_with_cell_area(self):
        """Should create a GTK3TreeViewColumn with a cell area and default values for
        attributes."""
        _cell_area = Gtk.CellAreaBox()
        dut = self.make_dut(cell_area=_cell_area)

        assert isinstance(dut, GTK3TreeViewColumn)
        assert dut.do_get_property("cell_area") == _cell_area

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
        assert dut.do_get_property("alignment") == 0.0
        assert dut.do_get_property("cell_area") is None
        assert not dut.do_get_property("clickable")
        assert not dut.do_get_property("expand")
        assert dut.do_get_property("fixed_width") == -1
        assert dut.do_get_property("max_width") == -1
        assert dut.do_get_property("min_width") == -1
        assert not dut.do_get_property("reorderable")
        assert not dut.do_get_property("resizable")
        assert dut.do_get_property("sizing") == Gtk.TreeViewColumnSizing.GROW_ONLY
        assert dut.do_get_property("sort_column_id") == -1
        assert not dut.do_get_property("sort_indicator")
        assert dut.do_get_property("sort_order") == Gtk.SortType.ASCENDING
        assert dut.do_get_property("spacing") == 0
        assert dut.do_get_property("title") == ""
        assert dut.do_get_property("visible")
        assert dut.do_get_property("widget") is None
        assert dut.do_get_property("width") == 0
        assert dut.do_get_property("x_offset") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                alignment=0.33,
                clickable=True,
                expand=True,
                fixed_width=50,
                max_width=100,
                min_width=25,
                reorderable=True,
                resizable=True,
                sizing=Gtk.TreeViewColumnSizing.AUTOSIZE,
                sort_column_id=2,
                sort_indicator=True,
                sort_order=Gtk.SortType.DESCENDING,
                spacing=5,
                title="Test Title",
                visible=False,
                width=20,
                x_offset=4,
            )
        )

        assert dut.do_get_property("alignment") == 0.33
        assert dut.do_get_property("cell_area") is None
        assert dut.do_get_property("clickable")
        assert dut.do_get_property("expand")
        assert dut.do_get_property("fixed_width") == 50
        assert dut.do_get_property("max_width") == 100
        assert dut.do_get_property("min_width") == 25
        assert dut.do_get_property("reorderable")
        assert dut.do_get_property("resizable")
        assert dut.do_get_property("sizing") == Gtk.TreeViewColumnSizing.AUTOSIZE
        assert dut.do_get_property("sort_column_id") == 2
        assert dut.do_get_property("sort_indicator")
        assert dut.do_get_property("sort_order") == Gtk.SortType.DESCENDING
        assert dut.do_get_property("spacing") == 5
        assert dut.do_get_property("title") == "Test Title"
        assert not dut.do_get_property("visible")
        assert dut.do_get_property("widget") is None
        assert dut.do_get_property("width") == 20
        assert dut.do_get_property("x_offset") == 4
