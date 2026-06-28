"""Test module for the GTK3Grid class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
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
