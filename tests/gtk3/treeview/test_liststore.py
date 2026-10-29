"""Test module for the GTK3ListStore class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes
from pytkwrap.gtk3.treeview import GTK3ListStore
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.treeview.constants import (
    EXPECTED_LISTSTORE_ATTRIBUTES,
    EXPECTED_LISTSTORE_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ListStore(BaseGTK3GObjectTests):
    """Test class for the GTK3ListStore class."""

    widget_class = GTK3ListStore
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_LISTSTORE_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_LISTSTORE_METHODS

    def make_dut(self, column_types=None, n_columns=0, n_rows=0):
        """Create a device under test for the GTK3ListStore."""
        return self.widget_class(column_types, n_columns, n_rows)

    @pytest.mark.unit
    def test_init_with_column_types(self):
        """Should create a GTK3ListStore with column types."""
        dut = self.make_dut(column_types=[str, str, int])

        assert dut.do_get_attribute("column_types") == [str, str, int]

    @pytest.mark.unit
    def test_init_with_n_columns(self):
        """Should create a GTK3ListStore with n_columns."""
        dut = self.make_dut(column_types=[str, str, float], n_columns=3)

        assert dut.do_get_attribute("column_types") == [str, str, float]
        assert dut.do_get_attribute("n_columns") == 3

    @pytest.mark.unit
    def test_init_with_n_rows(self):
        """Should create a GTK3ListStore with n_rows."""
        dut = self.make_dut(column_types=[str, str, float], n_columns=3, n_rows=10)

        assert dut.do_get_attribute("column_types") == [str, str, float]
        assert dut.do_get_attribute("n_columns") == 3
        assert dut.do_get_attribute("n_rows") == 10

    @pytest.mark.unit
    def test_init_with_column_types_and_zero_n_columns(self):
        """Should create a GTK3ListStore with column types and n_columns."""
        dut = self.make_dut(column_types=[str, str, float], n_columns=0)

        assert dut.do_get_attribute("column_types") == [str, str, float]
        assert dut.do_get_attribute("n_columns") == 3

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("column_types") is None
        assert dut.do_get_attribute("n_columns") == 0
        assert dut.do_get_attribute("n_rows") == 0

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                column_types=[str, int, float],
                n_columns=3,
                n_rows=10,
            )
        )

        assert dut.do_get_attribute("column_types") == [str, int, float]
        assert dut.do_get_attribute("n_columns") == 3
        assert dut.get_n_columns() == 3
        assert dut.do_get_attribute("n_rows") == 10

    @pytest.mark.unit
    def test_do_insert_row_with_values(self):
        """Should insert a row with values placed in the passed columns."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text1", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text3", 8.71], 2, [0, 1, 2])

        dut.do_insert_row(["Test Text", 3.2], position=0, columns=[1, 2])
        _iter = dut.get_iter_first()

        assert dut.get_value(_iter, 0) is None
        assert dut.get_value(_iter, 1) == "Test Text"
        assert dut.get_value(_iter, 2) == 3.2

    @pytest.mark.unit
    def test_do_insert_row_prepend(self):
        """Should insert a row at the beginning of the GTK3ListStore."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text1", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text3", 8.71], 2, [0, 1, 2])

        dut.do_insert_row(["Test", "Text0", 9.78], position=0)

        _iter = dut.get_iter_first()

        assert dut.get_value(_iter, 0) == "Test"
        assert dut.get_value(_iter, 1) == "Text0"
        assert dut.get_value(_iter, 2) == 9.78

    @pytest.mark.unit
    def test_do_insert_row_append(self):
        """Should insert a row at the end of the GTK3ListStore."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_insert_row(["Test", "Text3", 4.88], position=-1)

        assert dut.get_value(dut[-1].iter, 0) == "Test"
        assert dut.get_value(dut[-1].iter, 1) == "Text3"
        assert dut.get_value(dut[-1].iter, 2) == 4.88

    @pytest.mark.unit
    def test_do_insert_row(self):
        """Should insert a row at the position passed."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_insert_row(["Test", "Text3", 4.88], position=1)

        assert dut.get_value(dut[1].iter, 0) == "Test"
        assert dut.get_value(dut[1].iter, 1) == "Text3"
        assert dut.get_value(dut[1].iter, 2) == 4.88

    @pytest.mark.unit
    def test_do_insert_row_after(self):
        """Should insert a row after the sibling row passed."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_insert_row(["Test", "Text3", 66.2], sibling=dut[1].iter, after=True)

        assert dut.get_value(dut[2].iter, 0) == "Test"
        assert dut.get_value(dut[2].iter, 1) == "Text3"
        assert dut.get_value(dut[2].iter, 2) == 66.2

    @pytest.mark.unit
    def test_do_insert_row_before(self):
        """Should insert a row before the sibling row passed."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_insert_row(["Test", "Text3", 66.2], sibling=dut[2].iter, after=False)

        assert dut.get_value(dut[2].iter, 0) == "Test"
        assert dut.get_value(dut[2].iter, 1) == "Text3"
        assert dut.get_value(dut[2].iter, 2) == 66.2

    @pytest.mark.unit
    def test_do_move_row_after(self):
        """Should move the row after the position row passed."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_move_row(dut[0].iter, dut[1].iter, after=True)

        assert dut.get_value(dut[0].iter, 0) == "Test"
        assert dut.get_value(dut[0].iter, 1) == "Text1"
        assert dut.get_value(dut[0].iter, 2) == 5.0
        assert dut.get_value(dut[1].iter, 0) == "Test"
        assert dut.get_value(dut[1].iter, 1) == "Text0"
        assert dut.get_value(dut[1].iter, 2) == 3.2

    @pytest.mark.unit
    def test_do_move_row_after_none(self):
        """Should move the row to the start of the GTK3ListStore."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_move_row(dut[2].iter, None, after=True)

        assert dut.get_value(dut[0].iter, 0) == "Test"
        assert dut.get_value(dut[0].iter, 1) == "Text2"
        assert dut.get_value(dut[0].iter, 2) == 8.71

    @pytest.mark.unit
    def test_do_move_row_before(self):
        """Should move the row before the position row passed."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_move_row(dut[2].iter, dut[1].iter, after=False)

        assert dut.get_value(dut[1].iter, 0) == "Test"
        assert dut.get_value(dut[1].iter, 1) == "Text2"
        assert dut.get_value(dut[1].iter, 2) == 8.71
        assert dut.get_value(dut[2].iter, 0) == "Test"
        assert dut.get_value(dut[2].iter, 1) == "Text1"
        assert dut.get_value(dut[2].iter, 2) == 5.0

    @pytest.mark.unit
    def test_do_move_row_before_none(self):
        """Should move the row to the end of the GTK3ListStore."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_move_row(dut[0].iter, None, after=False)

        assert dut.get_value(dut[-1].iter, 0) == "Test"
        assert dut.get_value(dut[-1].iter, 1) == "Text0"
        assert dut.get_value(dut[-1].iter, 2) == 3.2

    @pytest.mark.unit
    def test_do_move_row_swap(self):
        """Should swap positions of the two iters in the GTK3ListStore."""
        dut = self.make_dut(column_types=[str, str, float])
        dut.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        dut.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        dut.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut.do_move_row(dut[0].iter, dut[2].iter, swap=True)

        assert dut.get_value(dut[0].iter, 0) == "Test"
        assert dut.get_value(dut[0].iter, 1) == "Text2"
        assert dut.get_value(dut[0].iter, 2) == 8.71
        assert dut.get_value(dut[2].iter, 0) == "Test"
        assert dut.get_value(dut[2].iter, 1) == "Text0"
        assert dut.get_value(dut[2].iter, 2) == 3.2
