"""Test module for the GTK3FlowBox class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io import GTK3Entry
from pytkwrap.gtk3.layout import GTK3FlowBox
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
)
from tests.gtk3.layout.constants import (
    EXPECTED_FLOWBOX_HANDLER_IDS,
    EXPECTED_FLOWBOX_METHODS,
    EXPECTED_FLOWBOX_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FlowBox(BaseGTK3GObjectTests):
    """Test class for the GTK3FlowBox class."""

    widget_class = GTK3FlowBox
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_FLOWBOX_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_FLOWBOX_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_FLOWBOX_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("activate_on_single_click")
        assert dut.do_get_property("column_spacing") == 0
        assert not dut.do_get_property("homogeneous")
        assert dut.do_get_property("max_children_per_line") == 7
        assert dut.do_get_property("min_children_per_line") == 0
        assert dut.do_get_property("row_spacing") == 0
        assert dut.do_get_property("selection_mode") == Gtk.SelectionMode.SINGLE

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                activate_on_single_click=False,
                column_spacing=10,
                homogeneous=True,
                max_children_per_line=22,
                min_children_per_line=4,
                row_spacing=8,
                selection_mode=Gtk.SelectionMode.BROWSE,
            )
        )

        assert not dut.get_property("activate_on_single_click")
        assert not dut.get_activate_on_single_click()
        assert dut.get_property("column_spacing") == 10
        assert dut.get_column_spacing() == 10
        assert dut.get_property("homogeneous")
        assert dut.get_homogeneous()
        assert dut.get_property("max_children_per_line") == 22
        assert dut.get_max_children_per_line() == 22
        assert dut.get_property("min_children_per_line") == 4
        assert dut.get_min_children_per_line() == 4
        assert dut.get_property("row_spacing") == 8
        assert dut.get_row_spacing() == 8
        assert dut.get_property("selection_mode") == Gtk.SelectionMode.BROWSE
        assert dut.get_selection_mode() == Gtk.SelectionMode.BROWSE

    @pytest.mark.unit
    def test_do_populate_flowbox(self):
        """Should populate the GTK3FlowBox."""
        dut = self.make_dut()
        dut.do_populate_flowbox([(GTK3Entry(), i) for i in range(4)])

        for _index in range(4):
            assert isinstance(dut.get_child_at_index(_index).get_child(), GTK3Entry)

    @pytest.mark.unit
    def test_do_unpopulate_flowbox(self):
        """Should unpopulate the GTK3FlowBox."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()
        _entry_3 = GTK3Entry()
        _entry_4 = GTK3Entry()

        dut = self.make_dut()
        dut.do_populate_flowbox([(_entry_1, 0)])
        dut.do_populate_flowbox([(_entry_2, 1)])
        dut.do_populate_flowbox([(_entry_3, 2)])
        dut.do_populate_flowbox([(_entry_4, 3)])

        assert dut.get_child_at_index(0).get_child() == _entry_1
        assert dut.get_child_at_index(1).get_child() == _entry_2
        assert dut.get_child_at_index(2).get_child() == _entry_3
        assert dut.get_child_at_index(3).get_child() == _entry_4

        dut.do_unpopulate_flowbox([3, 1])
        assert dut.get_child_at_index(0).get_child() == _entry_1
        assert dut.get_child_at_index(1).get_child() == _entry_3
        assert dut.get_child_at_index(2) is None
        assert dut.get_child_at_index(3) is None

    @pytest.mark.unit
    def test_do_unpopulate_flowbox_last_two_widgets(self):
        """Should unpopulate the GTK3FlowBox."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()
        _entry_3 = GTK3Entry()
        _entry_4 = GTK3Entry()

        dut = self.make_dut()
        dut.do_populate_flowbox([(_entry_1, 0)])
        dut.do_populate_flowbox([(_entry_2, 1)])
        dut.do_populate_flowbox([(_entry_3, 2)])
        dut.do_populate_flowbox([(_entry_4, 3)])

        assert dut.get_child_at_index(0).get_child() == _entry_1
        assert dut.get_child_at_index(1).get_child() == _entry_2
        assert dut.get_child_at_index(2).get_child() == _entry_3
        assert dut.get_child_at_index(3).get_child() == _entry_4

        dut.do_unpopulate_flowbox([2, 2])
        assert dut.get_child_at_index(0).get_child() == _entry_1
        assert dut.get_child_at_index(1).get_child() == _entry_2
        assert dut.get_child_at_index(2) is None
        assert dut.get_child_at_index(3) is None

    @pytest.mark.unit
    def test_do_unpopulate_flowbox_no_widget(self):
        """Should unpopulate the GTK3FlowBox."""
        _entry_1 = GTK3Entry()
        _entry_2 = GTK3Entry()

        dut = self.make_dut()
        dut.do_populate_flowbox([(_entry_1, 0)])
        dut.do_populate_flowbox([(_entry_2, 1)])

        assert dut.get_child_at_index(0).get_child() == _entry_1
        assert dut.get_child_at_index(1).get_child() == _entry_2

        with pytest.raises(TypeError):
            dut.do_unpopulate_flowbox([3])
