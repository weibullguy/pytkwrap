"""Test module for the GTK3TreeView class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3TreeView
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
from tests.gtk3.treeview.constants import (
    EXPECTED_TREEVIEW_HANDLER_IDS,
    EXPECTED_TREEVIEW_METHODS,
    EXPECTED_TREEVIEW_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3TreeView(BaseGTK3GObjectTests):
    """Test class for the GTK3TreeView class."""

    widget_class = GTK3TreeView
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TREEVIEW_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_TREEVIEW_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TREEVIEW_PROPERTIES
    )

    def make_dut(self, model: Gtk.TreeModel = None):
        """Create a device under test for the GTK3TreeView."""
        return self.widget_class(model)

    @pytest.mark.unit
    def test_init_with_model(self):
        """Should create a GTK3TreeView with a model."""
        _model = Gtk.TreeStore()
        _model.set_column_types([GObject.TYPE_INT, GObject.TYPE_STRING])
        _model.append(None, [0, "Test"])

        dut = self.make_dut(_model)

        assert isinstance(dut, GTK3TreeView)
        assert dut.do_get_property("model") == _model
        assert dut.get_property("model") == _model
        assert dut.get_model() == _model

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.dic_attributes == self.expected_attributes
        assert dut.do_get_attribute("axis") is None
        assert dut.do_get_attribute("canvas") is None
        assert dut.do_get_attribute("column_types") is None
        assert dut.do_get_attribute("data_type") is None
        assert dut.do_get_attribute("default_value") is None
        assert dut.do_get_attribute("edit_signal") is None
        assert dut.do_get_attribute("figure") is None
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") is None
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen-topic"
        assert dut.do_get_attribute("n_columns") is None
        assert dut.do_get_attribute("n_rows") is None
        assert dut.do_get_attribute("send_topic") == "send-topic"
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("activate_on_single_click")
        assert dut.do_get_property("enable_grid_lines") == Gtk.TreeViewGridLines.NONE
        assert dut.do_get_property("enable_search")
        assert not dut.do_get_property("enable_tree_lines")
        assert dut.do_get_property("expander_column") is None
        assert not dut.do_get_property("fixed_height_mode")
        assert dut.do_get_property("headers_clickable")
        assert dut.do_get_property("headers_visible")
        assert not dut.do_get_property("hover_expand")
        assert not dut.do_get_property("hover_selection")
        assert dut.do_get_property("level_indentation") == 0
        assert dut.do_get_property("model") is None
        assert not dut.do_get_property("reorderable")
        assert not dut.do_get_property("rubber_banding")
        assert dut.do_get_property("search_column") == -1
        assert dut.do_get_property("show_expanders")
        assert dut.do_get_property("tooltip_column") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _model = Gtk.TreeStore()
        _model.set_column_types([GObject.TYPE_INT, GObject.TYPE_STRING])
        _model.append(None, [0, "Test"])

        dut = self.make_dut()

        _column = dut.get_column(1)

        dut.do_set_properties(
            GTK3WidgetProperties(
                activate_on_single_click=True,
                enable_grid_lines=Gtk.TreeViewGridLines.HORIZONTAL,
                enable_search=False,
                enable_tree_lines=True,
                expander_column=_column,
                fixed_height_mode=True,
                headers_clickable=False,
                headers_visible=False,
                hover_expand=True,
                hover_selection=True,
                level_indentation=10,
                model=_model,
                reorderable=True,
                rubber_banding=True,
                search_column=1,
                show_expanders=False,
                tooltip_column=1,
            )
        )

        assert dut.get_property("activate_on_single_click")
        assert dut.get_activate_on_single_click()
        assert dut.get_property("enable_grid_lines") == Gtk.TreeViewGridLines.HORIZONTAL
        assert dut.get_grid_lines() == Gtk.TreeViewGridLines.HORIZONTAL
        assert not dut.get_property("enable_search")
        assert not dut.get_enable_search()
        assert dut.get_property("enable_tree_lines")
        assert dut.get_enable_tree_lines()
        assert dut.get_property("expander_column") == _column
        assert dut.get_expander_column() == _column
        assert dut.get_property("fixed_height_mode")
        assert dut.get_fixed_height_mode()
        assert dut.get_property("headers_clickable")
        assert dut.get_headers_clickable()
        assert not dut.get_property("headers_visible")
        assert not dut.get_headers_visible()
        assert dut.get_property("hover_expand")
        assert dut.get_hover_expand()
        assert dut.get_property("hover_selection")
        assert dut.get_hover_selection()
        assert dut.get_property("level_indentation") == 10
        assert dut.get_level_indentation() == 10
        assert dut.get_property("model") == _model
        assert dut.get_model() == _model
        assert dut.get_property("reorderable")
        assert dut.get_reorderable()
        assert dut.get_property("rubber_banding")
        assert dut.get_rubber_banding()
        assert dut.get_property("search_column") == 1
        assert dut.get_search_column() == 1
        assert not dut.get_property("show_expanders")
        assert not dut.get_show_expanders()
        assert dut.get_property("tooltip_column") == 1
        assert dut.get_tooltip_column() == 1
