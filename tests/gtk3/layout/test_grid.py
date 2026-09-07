"""Test module for the GTK3Grid class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io import GTK3Entry
from pytkwrap.gtk3.layout import GTK3Grid
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
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
from tests.gtk3.layout.constants import (
    EXPECTED_GRID_ATTRIBUTES,
    EXPECTED_GRID_METHODS,
    EXPECTED_GRID_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Grid(BaseGTK3GObjectTests):
    """Test class for the GTK3Grid class."""

    widget_class = GTK3Grid
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_GRID_ATTRIBUTES
    )
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_GRID_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_GRID_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("n_columns") == 1
        assert dut.do_get_attribute("n_rows") == 1

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values when passed in a GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes(n_columns=10, n_rows=5))

        assert dut.do_get_attribute("n_columns") == 10
        assert dut.do_get_attribute("n_rows") == 5

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("baseline_row") == 0
        assert not dut.do_get_property("column_homogeneous")
        assert dut.do_get_property("column_spacing") == 0
        assert not dut.do_get_property("row_homogeneous")
        assert dut.do_get_property("row_spacing") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                baseline_row=1,
                column_homogeneous=True,
                column_spacing=10,
                row_homogeneous=True,
                row_spacing=20,
            )
        )

        assert dut.get_property("baseline_row") == 1
        assert dut.get_baseline_row() == 1
        assert dut.get_property("column_homogeneous")
        assert dut.get_column_homogeneous()
        assert dut.get_property("column_spacing") == 10
        assert dut.get_column_spacing() == 10
        assert dut.get_property("row_homogeneous")
        assert dut.get_row_homogeneous()
        assert dut.get_property("row_spacing") == 20
        assert dut.get_row_spacing() == 20

    @pytest.mark.unit
    def test_do_build_grid(self):
        """Should build the GTK3Grid."""
        dut = self.make_dut()
        dut.do_build_grid(columns=[1, 2, 3], rows=[1, 2, 3])

        assert dut.do_get_attribute("n_columns") == 4
        assert dut.do_get_attribute("n_rows") == 4

    @pytest.mark.unit
    def test_do_build_grid_with_tuples(self):
        """Should build the GTK3Grid when passed tuples of integers instead of lists."""
        dut = self.make_dut()
        dut.do_build_grid(columns=(1, 2, 3), rows=(1, 2, 3))

        assert dut.do_get_attribute("n_columns") == 4
        assert dut.do_get_attribute("n_rows") == 4

    @pytest.mark.unit
    def test_do_build_grid_with_children(self):
        """Should build the GTK3Grid with children."""
        _entry_1 = GTK3Entry()

        dut = self.make_dut()
        dut.attach(_entry_1, 0, 0, 1, 1)
        # Add one column and one row to the grid.
        dut.do_build_grid(
            siblings=[_entry_1],
            sides=[[Gtk.PositionType.RIGHT, Gtk.PositionType.BOTTOM]],
        )

        assert dut.do_get_attribute("n_columns") == 2
        assert dut.do_get_attribute("n_rows") == 2

    @pytest.mark.unit
    def test_do_populate_grid(self):
        """Should populate the GTK3Grid."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()
        _entry_3 = GTK3Entry()
        _entry_4 = GTK3Entry()

        dut = self.make_dut()
        dut.do_build_grid([1], [1])
        dut.do_populate_grid(
            [_entry_1, _entry_2, _entry_3, _entry_4],
            [[0, 0], [1, 0], [0, 1], [1, 1]],
            [],
        )

        assert dut.get_child_at(0, 0) == _entry_1
        assert dut.get_child_at(1, 0) == _entry_2
        assert dut.get_child_at(0, 1) == _entry_3
        assert dut.get_child_at(1, 1) == _entry_4

    @pytest.mark.unit
    def test_do_populate_grid_span_columns(self):
        """Should populate the GTK3Grid with widgets that span multiple columns."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()
        _entry_3 = GTK3Entry()
        _entry_4 = GTK3Entry()

        dut = self.make_dut()
        dut.do_build_grid([1, 2, 3], [1])
        dut.do_populate_grid(
            [_entry_1, _entry_2, _entry_3, _entry_4],
            [[0, 0], [2, 0], [0, 1], [2, 1]],
            [[2, 1], [2, 1], [2, 1], [2, 1]],
        )

        assert dut.get_child_at(0, 0) == _entry_1
        assert dut.get_child_at(0, 1) == _entry_3
        assert dut.get_child_at(1, 0) == _entry_1
        assert dut.get_child_at(1, 1) == _entry_3
        assert dut.get_child_at(2, 0) == _entry_2
        assert dut.get_child_at(2, 1) == _entry_4
        assert dut.get_child_at(3, 0) == _entry_2
        assert dut.get_child_at(3, 1) == _entry_4

    @pytest.mark.unit
    def test_do_populate_grid_span_rows(self):
        """Should populate the GTK3Grid with widgets that span multiple rows."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()
        _entry_3 = GTK3Entry()
        _entry_4 = GTK3Entry()

        dut = self.make_dut()
        dut.do_build_grid([1], [1, 2, 3])
        dut.do_populate_grid(
            [_entry_1, _entry_2, _entry_3, _entry_4],
            [[0, 0], [1, 0], [0, 2], [1, 2]],
            [[1, 2], [1, 2], [1, 2], [1, 2]],
        )

        assert dut.get_child_at(0, 0) == _entry_1
        assert dut.get_child_at(0, 1) == _entry_1
        assert dut.get_child_at(0, 2) == _entry_3
        assert dut.get_child_at(0, 3) == _entry_3
        assert dut.get_child_at(1, 0) == _entry_2
        assert dut.get_child_at(1, 1) == _entry_2
        assert dut.get_child_at(1, 2) == _entry_4
        assert dut.get_child_at(1, 3) == _entry_4

    @pytest.mark.unit
    def test_do_populate_grid_with_existing_widgets(self):
        """Should populate the GTK3Grid with widgets that span multiple rows."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()
        _entry_3 = GTK3Entry()
        _entry_4 = GTK3Entry()

        dut = self.make_dut()
        dut.do_build_grid([1], [1])
        dut.do_populate_grid(
            [_entry_1, _entry_2],
            [[0, 0], [1, 0]],
            [],
        )
        dut.do_populate_grid(
            [_entry_3, _entry_4],
            [],
            [],
            [_entry_1, _entry_2],
            [Gtk.PositionType.BOTTOM, Gtk.PositionType.BOTTOM],
        )

        assert dut.get_child_at(0, 0) == _entry_1
        assert dut.get_child_at(0, 1) == _entry_3
        assert dut.get_child_at(1, 0) == _entry_2
        assert dut.get_child_at(1, 1) == _entry_4
