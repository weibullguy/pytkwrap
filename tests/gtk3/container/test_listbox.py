"""Test module for the GTK3ListBox class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.container import GTK3ListBox
from pytkwrap.gtk3.io import GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
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
    EXPECTED_LISTBOX_HANDLER_IDS,
    EXPECTED_LISTBOX_METHODS,
    EXPECTED_LISTBOX_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ListBox(BaseGTK3GObjectTests):
    """Test class for the GTK3ListBox class."""

    widget_class = GTK3ListBox
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_LISTBOX_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_LISTBOX_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_LISTBOX_PROPERTIES
    )

    def make_dut(self, adjustment=None):
        return self.widget_class(adjustment)

    @pytest.mark.unit
    def test_init_with_adjustment(self):
        """Should initialize a GTK3ListBox with the GTK3Adjustment passed."""
        _adjustment = GTK3Adjustment()
        dut = self.make_dut(_adjustment)

        assert dut.do_get_property("adjustment") == _adjustment
        assert dut.get_adjustment() == _adjustment

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("activate_on_single_click")
        assert dut.do_get_property("adjustment") is None
        assert dut.do_get_property("selection_mode") == Gtk.SelectionMode.SINGLE

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _adjustment = GTK3Adjustment()
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                activate_on_single_click=False,
                adjustment=_adjustment,
                selection_mode=Gtk.SelectionMode.MULTIPLE,
            )
        )

        assert not dut.get_property("activate_on_single_click")
        assert not dut.get_activate_on_single_click()
        assert dut.get_adjustment() == _adjustment
        assert dut.get_property("selection_mode") == Gtk.SelectionMode.MULTIPLE
        assert dut.get_selection_mode() == Gtk.SelectionMode.MULTIPLE

    @pytest.mark.unit
    def test_do_add_child(self):
        """Should add child widgets to the GTK3ListBox."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_add_child(_child1)
        dut.do_add_child(_child2)
        dut.do_add_child(_child3, 1)

        # The GTK3ListBox get_children() returns a list of Gtk.ListBoxRow.  Each
        # Gtk.ListBoxRow get_children() returns a list of Gtk.Widgets in that row.
        assert dut.get_children()[0].get_children()[0] == _child2
        assert dut.get_children()[1].get_children()[0] == _child3
        assert dut.get_children()[2].get_children()[0] == _child1

    @pytest.mark.unit
    def test_do_get_row_at_index(self):
        """Should return the row requested."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_add_child(_child3)
        dut.do_add_child(_child2)
        dut.do_add_child(_child1)

        assert isinstance(dut.do_get_row(index=2), Gtk.ListBoxRow)
        assert dut.do_get_row(index=2).get_children()[0] == _child3
        assert dut.do_get_row(index=-1) is None

    @pytest.mark.skip
    def test_do_get_row_at_y(self):
        """Should return the row requested."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_add_child(_child3)
        dut.do_add_child(_child2)
        dut.do_add_child(_child1)

        assert isinstance(dut.do_get_row(y=2), Gtk.ListBoxRow)
        assert dut.do_get_row(y=2).get_children()[0] == _child3

    @pytest.mark.unit
    def test_do_select_row_all(self):
        """Should select all the rows in the GTK3ListBox."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                selection_mode=Gtk.SelectionMode.MULTIPLE,
            )
        )
        dut.do_add_child(_child3)
        dut.do_add_child(_child2)
        dut.do_add_child(_child1)

        dut.do_select_row(None)

        assert isinstance(dut.do_get_selected()[0], Gtk.ListBoxRow)
        assert isinstance(dut.do_get_selected()[1], Gtk.ListBoxRow)
        assert isinstance(dut.do_get_selected()[2], Gtk.ListBoxRow)
        assert dut.do_get_selected()[0].get_children()[0] == _child1
        assert dut.do_get_selected()[1].get_children()[0] == _child2
        assert dut.do_get_selected()[2].get_children()[0] == _child3

    @pytest.mark.unit
    def test_do_select_row(self):
        """Should select the requested row in the GTK3ListBox."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_add_child(_child3)
        dut.do_add_child(_child2)
        dut.do_add_child(_child1)

        dut.do_select_row(dut.get_children()[1])

        assert isinstance(dut.do_get_selected()[0], Gtk.ListBoxRow)
        assert dut.do_get_selected()[0].get_children()[0] == _child2

    @pytest.mark.unit
    def test_do_unselect_row_all(self):
        """Should unselect all the rows in the GTK3ListBox."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                selection_mode=Gtk.SelectionMode.MULTIPLE,
            )
        )
        dut.do_add_child(_child3)
        dut.do_add_child(_child2)
        dut.do_add_child(_child1)

        dut.do_select_row(None)

        assert isinstance(dut.do_get_selected()[0], Gtk.ListBoxRow)
        assert isinstance(dut.do_get_selected()[1], Gtk.ListBoxRow)
        assert isinstance(dut.do_get_selected()[2], Gtk.ListBoxRow)
        assert dut.do_get_selected()[0].get_children()[0] == _child1
        assert dut.do_get_selected()[1].get_children()[0] == _child2
        assert dut.do_get_selected()[2].get_children()[0] == _child3

        dut.do_unselect_row(None)

        assert dut.do_get_selected() == []

    @pytest.mark.unit
    def test_do_unselect_row(self):
        """Should unselect the requested row in the GTK3ListBox."""
        _child1 = GTK3Label()
        _child2 = GTK3Label()
        _child3 = GTK3Label()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                selection_mode=Gtk.SelectionMode.MULTIPLE,
            )
        )
        dut.do_add_child(_child3)
        dut.do_add_child(_child2)
        dut.do_add_child(_child1)

        dut.do_select_row(None)

        assert isinstance(dut.do_get_selected()[0], Gtk.ListBoxRow)
        assert dut.do_get_selected()[0].get_children()[0] == _child1
