"""Test module for the GTK3ListStore class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
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
        assert dut.do_get_attribute("n_rows") == 10
