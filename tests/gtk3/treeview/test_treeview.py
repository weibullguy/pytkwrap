"""Test module for the GTK3TreeView class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.treeview import (
    GTK3ListStore,
    GTK3TreeStore,
    GTK3TreeView,
    GTK3TreeViewColumn,
    do_construct_treeview,
)
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

    def make_populated_liststore_dut(self):
        _model = GTK3ListStore(
            column_types=[str, str, int, float],
            n_columns=4,
            n_rows=0,
        )
        _model.do_insert_row(["Column 1A", "Column 2A", 0, 1.0], position=-1)
        _model.do_insert_row(["Column 1B", "Column 2B", 1, 2.0], position=-1)
        _model.do_insert_row(["Column 1C", "Column 2C", 2, 3.0], position=-1)
        _model.do_insert_row(["Column 1D", "Column 2D", 3, 4.0], position=-1)

        dut = self.make_dut(model=_model)
        dut.do_add_column(position=-1)
        dut.do_add_column(position=-1)
        dut.do_add_column(position=-1)
        dut.do_add_column(position=-1)

        return dut

    def make_populated_treestore_dut(self):
        _model = GTK3TreeStore(
            column_types=[str, str, int, float],
            n_columns=4,
            n_rows=0,
        )
        _iter = _model.do_insert_row(
            values=["Column 1A", "Column 2A", 0, 1.0],
            position=-1,
            parent=None,
        )
        _iter = _model.do_insert_row(
            ["Column 1B", "Column 2B", 1, 2.0],
            position=-1,
            parent=_iter,
        )
        _model.do_insert_row(
            ["Column 1C", "Column 2C", 2, 3.0],
            position=-1,
            parent=_iter,
        )
        _model.do_insert_row(
            ["Column 1D", "Column 2D", 3, 4.0],
            position=-1,
            parent=_iter,
        )

        dut = self.make_dut(model=_model)
        dut.do_add_column(position=-1)
        dut.do_add_column(position=-1)
        dut.do_add_column(position=-1)
        dut.do_add_column(position=-1)

        return dut

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

    @pytest.mark.unit
    def test_do_add_column_append(self):
        """Should add a column at the end of the GTK3TreeView."""
        _column = GTK3TreeViewColumn()

        dut = self.make_dut()
        dut.do_add_column()
        dut.do_add_column()
        dut.do_add_column()
        dut.do_add_column(column=_column)

        assert len(dut.columns) == 4
        assert isinstance(dut.columns[0], GTK3TreeViewColumn)
        assert isinstance(dut.columns[1], GTK3TreeViewColumn)
        assert isinstance(dut.columns[2], GTK3TreeViewColumn)
        assert dut.columns[3] == _column

    @pytest.mark.unit
    def test_do_add_column_at_position(self):
        """Should add a column at the position specified."""
        _column1 = GTK3TreeViewColumn()
        _column2 = GTK3TreeViewColumn()
        _column3 = GTK3TreeViewColumn()
        _column4 = GTK3TreeViewColumn()

        dut = self.make_dut()
        dut.do_add_column(column=_column1, position=-1)
        dut.do_add_column(column=_column3, position=-1)
        dut.do_add_column(column=_column4, position=-1)
        dut.do_add_column(column=_column2, position=1)

        assert len(dut.columns) == 4
        assert dut.columns[0] == _column1
        assert dut.columns[1] == _column2
        assert dut.columns[2] == _column3
        assert dut.columns[3] == _column4

    @pytest.mark.unit
    def test_do_add_column_with_attributes(self):
        """Should add a GTK3TreeViewColumn with attributes."""
        _column1 = GTK3TreeViewColumn()
        _column2 = GTK3TreeViewColumn()
        _column3 = GTK3TreeViewColumn()
        _column4 = GTK3TreeViewColumn()

        dut = self.make_dut()
        dut.do_add_column(column=_column1, position=-1, title="Col 1")
        dut.do_add_column(column=_column2, position=-1, title="Col 2")
        dut.do_add_column(column=_column3, position=-1, title="Col 3")
        dut.do_add_column(column=_column4, position=-1, title="Col 4")

        assert dut.columns[0].get_title() == "Col 1"
        assert dut.columns[1].get_title() == "Col 2"
        assert dut.columns[2].get_title() == "Col 3"
        assert dut.columns[3].get_title() == "Col 4"

    @pytest.mark.unit
    def test_do_expand_row_all(self):
        """Should expand the entire GTK3TreeStore is path is None."""
        dut = self.make_populated_treestore_dut()

        assert dut.do_expand_row() is None

    @pytest.mark.unit
    def test_do_expand_row_treestore(self):
        """Should expand only the row pointed to by path in a GTK3TreeStore."""
        dut = self.make_populated_treestore_dut()

        _model = dut.get_model()
        _path = _model.get_path(_model["0:0"].iter)

        assert dut.do_expand_row(_path) is None

    @pytest.mark.unit
    def test_do_expand_row_treestore_open_all(self):
        """Should expand only the row pointed to by path in a GTK3TreeStore."""
        dut = self.make_populated_treestore_dut()

        _model = dut.get_model()
        _path = _model.get_path(_model["0"].iter)

        assert dut.do_expand_row(_path, True)

    @pytest.mark.unit
    def test_do_collapse_row_all(self):
        """Should collapse all rows in the GTK3TreeView."""
        dut = self.make_populated_treestore_dut()
        dut.do_expand_row()

        assert dut.do_collapse_row() is None

    @pytest.mark.unit
    def test_do_collapse_row_liststore(self):
        """Should not be able to collapse only a row in a GTK3ListStore."""
        dut = self.make_populated_liststore_dut()

        _model = dut.get_model()
        _path = _model.get_path(_model[2].iter)

        assert not dut.do_collapse_row(_path)

    @pytest.mark.unit
    def test_do_collapse_row_treestore(self):
        """Should collapse only the row pointed to by path in a GTK3TreeStore."""
        dut = self.make_populated_treestore_dut()

        _model = dut.get_model()
        _path = _model.get_path(_model["0:0"].iter)

        assert dut.do_expand_row(_path) is None
        assert dut.do_collapse_row(_path)

    @pytest.mark.unit
    def test_do_move_column(self):
        """Should move column A after column B."""
        dut = self.make_populated_treestore_dut()

        _base_column = dut.get_column(1)
        _column = dut.get_column(3)

        assert dut.do_move_column(_column, _base_column) is None
        assert dut.get_column(1) == _base_column
        assert dut.get_column(2) == _column

    @pytest.mark.unit
    def test_do_move_column_first(self):
        """Should move column A to the beginning if column B is None."""
        dut = self.make_populated_treestore_dut()

        _column = dut.get_column(3)

        assert dut.do_move_column(_column, None) is None
        assert dut.get_column(0) == _column

    @pytest.mark.unit
    def test_do_remove_column(self):
        """Should remove the column passed."""
        dut = self.make_populated_treestore_dut()

        _column1 = dut.get_column(1)
        _column2 = dut.get_column(2)

        assert dut.do_remove_column(_column1) == 3
        assert dut.get_column(1) == _column2

    @pytest.mark.unit
    def test_do_scroll_to_cell(self):
        """Should scroll to the cell specified by path and column."""
        dut = self.make_populated_treestore_dut()

        _column = dut.get_column(2)
        _model = dut.get_model()
        _path = _model.get_path(_model["0:0:0"].iter)

        assert (
            dut.do_scroll(
                path=_path,
                column=_column,
                use_align=False,
                row_align=0.5,
                col_align=0.5,
            )
            is None
        )

    @pytest.mark.unit
    def test_columns(self):
        """Should return a list of the GTK3TreeViewColumns in the GTK3TreeView."""
        dut = self.make_populated_treestore_dut()

        _column0 = dut.get_column(0)
        _column1 = dut.get_column(1)
        _column2 = dut.get_column(2)
        _column3 = dut.get_column(3)

        assert dut.n_columns == 4
        assert dut.columns[0] == _column0
        assert dut.columns[1] == _column1
        assert dut.columns[2] == _column2
        assert dut.columns[3] == _column3

    @pytest.mark.unit
    def test_selection(self):
        """Should return the Gtk.TreeSelection for the selected row."""
        dut = self.make_populated_treestore_dut()

        assert isinstance(dut.selection, Gtk.TreeSelection)
        assert dut.selection.get_selected() == (dut.get_model(), None)

    @pytest.mark.unit
    def test_visible_range(self):
        """Should return a tuple with the first and last visible paths."""
        dut = self.make_populated_treestore_dut()

        assert dut.visible_range is None

    @pytest.mark.unit
    def test_visible_rect(self):
        """Should return a Gdk.Rectanble representing the visible region.."""
        dut = self.make_populated_treestore_dut()

        assert isinstance(dut.visible_rect, Gdk.Rectangle)
        assert dut.visible_rect.height == 0
        assert dut.visible_rect.width == 1
        assert dut.visible_rect.x == 0
        assert dut.visible_rect.y == 0

    @pytest.mark.unit
    def test_do_construct_treeview(self):
        """Should construct a GTK3TreeView with the column types and titles passed."""
        dut = do_construct_treeview(
            column_types=[str, str, int, float, bool],
            renderer_types=["ComBo", "tEXt", "TEXT", "SpiN", "ToGGle"],
            attributes=[
                {"text": 0, "visible": 4},
                {"markup": 1},
                {"text": 2},
                {"text": 3},
                {"active": 4},
            ],
            headers=[
                "String 1",
                "String 2",
                "Integer",
                "Float",
                "Boolean",
            ],
        )

        assert isinstance(dut, GTK3TreeView)
        assert dut.n_columns == 5
        assert dut.get_column(0).get_title() == "String 1"
        assert dut.get_column(1).get_title() == "String 2"
        assert dut.get_column(2).get_title() == "Integer"
        assert dut.get_column(3).get_title() == "Float"
        assert dut.get_column(4).get_title() == "Boolean"

    @pytest.mark.unit
    def test_do_add_liststore_row(self):
        """Should add a GTK3TreeView with a GTK3ListStore."""
        dut = do_construct_treeview(
            column_types=[str, str, int],
            renderer_types=["ComBo", "tEXt", "TEXT"],
            attributes=[
                {"text": 0},
                {"markup": 1},
                {"text": 2},
            ],
            headers=[
                "String 1",
                "String 2",
                "Integer",
            ],
            tree=False,
        )
        dut.do_add_row(values=["Column 1A", "Column 2A", 0], position=-1)

        _model = dut.get_model()
        _iter = _model.get_iter_first()

        assert _model.get_value(_iter, 0) == "Column 1A"
        assert _model.get_value(_iter, 1) == "Column 2A"
        assert _model.get_value(_iter, 2) == 0

    @pytest.mark.unit
    def test_do_add_treestore_row(self):
        """Should add a GTK3TreeView with a GTK3TreeStore."""
        dut = do_construct_treeview(
            column_types=[str, str, int],
            renderer_types=["ComBo", "tEXt", "TEXT"],
            attributes=[
                {"text": 0},
                {"markup": 1},
                {"text": 2},
            ],
            headers=[
                "String 1",
                "String 2",
                "Integer",
            ],
        )
        _iter = dut.do_add_row(values=["Column 1A", "Column 2A", 0], position=-1)
        _iter = dut.do_add_row(
            values=["Column 1A.1", "Column 2A.1", 2], position=-1, parent=_iter
        )

        _model = dut.get_model()
        _iter = _model.get_iter_first()

        assert _model.get_value(_iter, 0) == "Column 1A"
        assert _model.get_value(_iter, 1) == "Column 2A"
        assert _model.get_value(_iter, 2) == 0

        _iter = _model.iter_children(_iter)

        assert _model.get_value(_iter, 0) == "Column 1A.1"
        assert _model.get_value(_iter, 1) == "Column 2A.1"
        assert _model.get_value(_iter, 2) == 2
