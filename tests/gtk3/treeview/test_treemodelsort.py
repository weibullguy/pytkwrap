"""Test module for the GTK3TreeModelSort class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3ListStore, GTK3TreeModelSort
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.treeview.constants import (
    EXPECTED_TREEMODELSORT_METHODS,
    EXPECTED_TREEMODELSORT_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3TreeModelSort(BaseGTK3GObjectTests):
    """Test class for the GTK3TreeModelSort class."""

    widget_class = GTK3TreeModelSort
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_TREEMODELSORT_METHODS
    expected_properties = EXPECTED_TREEMODELSORT_PROPERTIES

    def make_dut(self, model=None):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class(model)

    @pytest.mark.unit
    def test_init_with_child_model(self):
        dut = self.make_dut(model=Gtk.ListStore())

        assert isinstance(dut.get_property("model"), Gtk.TreeModel)
        assert isinstance(dut.get_model(), Gtk.TreeModel)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("model") is None

    @pytest.mark.unit
    def test_do_convert_rows_child_to_sorted(self):
        """Should convert a child iter to a sorted iter."""
        _child_model = GTK3ListStore(
            column_types=[str, str, float],
            n_columns=3,
            n_rows=0,
        )
        _child_model.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])
        _child_iter = _child_model[1].iter

        dut = self.make_dut(model=_child_model)
        _was_set, _sort_iter = dut.do_convert_iter(child_iter=_child_iter)

        assert _was_set
        assert isinstance(_sort_iter, Gtk.TreeIter)
        assert dut.get_value(_sort_iter, 0) == _child_model.get_value(_child_iter, 0)
        assert dut.get_value(_sort_iter, 1) == _child_model.get_value(_child_iter, 1)
        assert dut.get_value(_sort_iter, 2) == _child_model.get_value(_child_iter, 2)

    @pytest.mark.unit
    def test_do_convert_rows_sorted_to_child(self):
        """Should convert a sorted iter to a child iter."""
        _child_model = GTK3ListStore(
            column_types=[str, str, float],
            n_columns=3,
            n_rows=0,
        )
        _child_model.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])

        dut = self.make_dut(model=_child_model)
        _sorted_iter = dut.do_convert_iter(
            sorted_iter=dut[1].iter,
            child_to_sorted=False,
        )

        assert isinstance(_sorted_iter, Gtk.TreeIter)
        assert _child_model.get_value(_sorted_iter, 0) == dut.get_value(dut[1].iter, 0)
        assert _child_model.get_value(_sorted_iter, 1) == dut.get_value(dut[1].iter, 1)
        assert _child_model.get_value(_sorted_iter, 2) == dut.get_value(dut[1].iter, 2)

    @pytest.mark.unit
    def test_do_convert_path_child_to_sorted(self):
        """Should convert a child path to a sorted path."""
        _child_model = GTK3ListStore(
            column_types=[str, str, float],
            n_columns=3,
            n_rows=0,
        )
        _child_model.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])
        _child_path = _child_model.get_path(_child_model[1].iter)

        dut = self.make_dut(model=_child_model)
        _sort_path = dut.do_convert_path(child_path=_child_path)

        assert isinstance(_sort_path, Gtk.TreePath)
        assert _sort_path == dut.get_path(dut[1].iter)

    @pytest.mark.unit
    def test_do_convert_path_sorted_to_child(self):
        """Should convert a sorted path to a child path."""
        _child_model = GTK3ListStore(
            column_types=[str, str, float],
            n_columns=3,
            n_rows=0,
        )
        _child_model.do_insert_row(["Test", "Text0", 3.2], 0, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text1", 5.0], 1, [0, 1, 2])
        _child_model.do_insert_row(["Test", "Text2", 8.71], 2, [0, 1, 2])
        _child_path = _child_model.get_path(_child_model[1].iter)

        dut = self.make_dut(model=_child_model)
        _sort_path = dut.get_path(dut[1].iter)
        _child_path = dut.do_convert_path(sorted_path=_sort_path, child_to_sorted=False)

        assert isinstance(_child_path, Gtk.TreePath)
        assert _child_path == _child_model.get_path(_child_model[1].iter)
