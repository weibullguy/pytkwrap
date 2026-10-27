"""Test module for the GTK3Toolbar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool import GTK3Toolbar, GTK3ToolItem
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
from tests.gtk3.tool.constants import (
    EXPECTED_TOOLBAR_HANDLER_IDS,
    EXPECTED_TOOLBAR_METHODS,
    EXPECTED_TOOLBAR_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Toolbar(BaseGTK3GObjectTests):
    """Test class for the GTK3Toolbar class."""

    widget_class = GTK3Toolbar
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TOOLBAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_TOOLBAR_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TOOLBAR_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("icon_size") == Gtk.IconSize.LARGE_TOOLBAR
        assert not dut.do_get_property("icon_size_set")
        assert dut.do_get_property("show_arrow")
        assert dut.do_get_property("toolbar_style") == Gtk.ToolbarStyle.BOTH_HORIZ

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                icon_size=Gtk.IconSize.BUTTON,
                icon_size_set=True,
                show_arrow=False,
                toolbar_style=Gtk.ToolbarStyle.BOTH,
            )
        )

        assert dut.get_property("icon_size") == Gtk.IconSize.BUTTON
        assert dut.get_icon_size() == Gtk.IconSize.BUTTON
        assert dut.get_property("icon_size_set")
        assert not dut.get_property("show_arrow")
        assert not dut.get_show_arrow()
        assert dut.get_property("toolbar_style") == Gtk.ToolbarStyle.BOTH
        assert dut.get_style() == Gtk.ToolbarStyle.BOTH

    @pytest.mark.unit
    def test_do_build_toolbar_with_list_of_lists(self):
        """Should build a toolbar with the children passed in."""
        _toolitem1 = GTK3ToolItem()
        _toolitem2 = GTK3ToolItem()

        dut = self.make_dut()
        dut.do_build_toolbar([[_toolitem1, 0], [_toolitem2, 1]])

        assert dut.n_items == 2
        assert dut.get_nth_item(0) == _toolitem1
        assert dut.get_nth_item(1) == _toolitem2

    @pytest.mark.unit
    def test_do_build_toolbar_with_list_of_tuples(self):
        """Should build a toolbar with the children passed in."""
        _toolitem1 = GTK3ToolItem()
        _toolitem2 = GTK3ToolItem()

        dut = self.make_dut()
        dut.do_build_toolbar([(_toolitem1, 0), (_toolitem2, 1)])

        assert dut.n_items == 2
        assert dut.get_nth_item(0) == _toolitem1
        assert dut.get_nth_item(1) == _toolitem2

    @pytest.mark.unit
    def test_do_build_toolbar_with_tuple_of_lists(self):
        """Should build a toolbar with the children passed in."""
        _toolitem1 = GTK3ToolItem()
        _toolitem2 = GTK3ToolItem()

        dut = self.make_dut()
        dut.do_build_toolbar(([_toolitem1, 0], [_toolitem2, 1]))

        assert dut.n_items == 2
        assert dut.get_nth_item(0) == _toolitem1
        assert dut.get_nth_item(1) == _toolitem2

    @pytest.mark.unit
    def test_do_build_toolbar_with_tuple_of_tuples(self):
        """Should build a toolbar with the children passed in."""
        _toolitem1 = GTK3ToolItem()
        _toolitem2 = GTK3ToolItem()

        dut = self.make_dut()
        dut.do_build_toolbar(((_toolitem1, 0), (_toolitem2, 1)))

        assert dut.n_items == 2
        assert dut.get_nth_item(0) == _toolitem1
        assert dut.get_nth_item(1) == _toolitem2

    @pytest.mark.unit
    def test_n_items(self):
        """Should return the number of items in the toolbar."""
        _toolitem1 = GTK3ToolItem()
        _toolitem2 = GTK3ToolItem()

        dut = self.make_dut()
        assert dut.n_items == 0

        dut.insert(_toolitem1, 0)
        assert dut.n_items == 1

        dut.insert(_toolitem2, 1)
        assert dut.n_items == 2

    @pytest.mark.unit
    def test_relief_style(self):
        """Should return the relief style of the toolbar."""
        dut = self.make_dut()

        assert dut.relief_style == Gtk.ReliefStyle.NONE
