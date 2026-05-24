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
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1
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
