"""Test module for the GTK3TreeViewColumn class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.cellrenderer import GTK3CellRenderer
from pytkwrap.gtk3.treeviewcolumn import GTK3TreeViewColumn

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests


@pytest.mark.order(3)
class TestGTK3TreeViewColumn(BaseGTK3GObjectTests):
    """Test class for the GTK3TreeViewColumn class."""

    widget_class = GTK3TreeViewColumn
    expected_attributes = [
        "add_attribute",
        "cell_get_position",
        "cell_get_size",
        "cell_is_visible",
        "cell_set_cell_data",
        "clear",
        "clear_attributes",
        "clicked",
        "focus_cell",
        "get_alignment",
        "get_button",
        "get_clickable",
        "get_expand",
        "get_fixed_width",
        "get_max_width",
        "get_min_width",
        "get_reorderable",
        "get_resizable",
        "get_sizing",
        "get_sort_column_id",
        "get_sort_indicator",
        "get_sort_order",
        "get_spacing",
        "get_title",
        "get_tree_view",
        "get_visible",
        "get_widget",
        "get_width",
        "get_x_offset",
        "pack_end",
        "pack_start",
        "queue_resize",
        "set_alignment",
        "set_attributes",
        "set_cell_data_func",
        "set_clickable",
        "set_expand",
        "set_fixed_width",
        "set_max_width",
        "set_min_width",
        "set_reorderable",
        "set_resizable",
        "set_sizing",
        "set_sort_column_id",
        "set_sort_indicator",
        "set_sort_order",
        "set_spacing",
        "set_title",
        "set_visible",
        "set_widget",
    ]
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1
    expected_handler_id = {
        "clicked": -1,
        "notify": -1,
    }
    expected_properties = {
        "alignment": 0.0,
        "cell_area": None,
        "clickable": False,
        "expand": False,
        "fixed_width": -1,
        "max_width": -1,
        "min_width": -1,
        "reorderable": False,
        "resizable": False,
        "sizing": Gtk.TreeViewColumnSizing.GROW_ONLY,
        "sort_column_id": -1,
        "sort_indicator": False,
        "sort_order": Gtk.SortType.ASCENDING,
        "spacing": 0,
        "title": "",
        "visible": True,
        "widget": None,
        "width": 0,
        "x_offset": 0,
    }

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
