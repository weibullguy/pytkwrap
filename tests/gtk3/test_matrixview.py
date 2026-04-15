# pylint: skip-file
# type: ignore
# -*- coding: utf-8 -*-
#
#       tests.gtk3.test_matrixview.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3MatrixView module algorithms and models."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
#  Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.combo import GTK3ComboBox
from pytkwrap.gtk3.entry import GTK3Entry
from pytkwrap.gtk3.label import GTK3Label
from pytkwrap.gtk3.matrixview import GTK3MatrixView
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.textview import GTK3TextView

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests


COLUMN_HEADINGS = [
    ("Column 1", "Column Tooltip 1"),
    ("Column 2", "Column Tooltip 2"),
    ("Column 3", "Column Tooltip 3"),
]
ROW_HEADINGS = [
    ("Row 1", "Row Tooltip 1"),
    ("Row 2", "Row Tooltip 2"),
    ("Row 3", "Row Tooltip 3"),
]


class TestMatrixView(BaseGTK3DataWidgetTests):
    """Test class for the GTK3MatrixView."""

    widget_class = GTK3MatrixView
    expected_default_height = -1
    expected_default_value = None
    expected_default_width = -1

    def mock_callback(self, matrixview) -> None:
        """Mock callback to attach dut signals to."""
        assert isinstance(matrixview, GTK3MatrixView)

    def no_signal_error_handler(self, message):
        """Error handler for do_set_callbacks() errors."""
        assert (
            message == "GTK3MatrixView.do_set_callbacks(): Unknown signal name "
            "'value-changed'."
        )

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3MatrixView with default values for attributes."""
        super().test_init()

        dut = self.make_dut()

        # All handler IDs should start at -1.
        assert all(_hid == -1 for _hid in dut.dic_handler_id.values())
        # MatrixView-specific attributes should be registered.
        for _attribute in GTK3MatrixView._GTK3_MATRIXVIEW_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        # MatrixView-specific properties should be registered.
        for _property in GTK3MatrixView._GTK3_MATRIXVIEW_PROPERTIES:
            assert _property in dut.dic_properties
        # MatrixView-specific signals should be registered.
        for _signal in GTK3MatrixView._GTK3_MATRIXVIEW_SIGNALS:
            assert _signal in dut.dic_handler_id
        assert dut.n_columns == 0
        assert dut.n_rows == 0

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set the default attributes of a GTK3MatrixView when passed an empty
        GTK3DataWidgetAttributes.
        """
        super().test_do_set_attributes_default()

        dut = self.make_dut()
        dut.do_set_attributes(GTK3DataWidgetAttributes())

        assert dut.n_columns == 0
        assert dut.n_rows == 0

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """do_set_attributes() should set the MatrixView attributes to the values passed
        in a WidgetAttributes dict.
        """
        super().test_do_set_attributes()

        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3DataWidgetAttributes(
                n_columns=3,
                n_rows=2,
            )
        )

        assert dut.n_columns == 3
        assert dut.n_rows == 2

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should retrieve the value of the passed attribute."""
        super().test_do_get_attribute()

        dut = self.make_dut()

        assert dut.do_get_attribute("n_columns") == 0
        assert dut.do_get_attribute("n_rows") == 0

    @pytest.mark.unit
    def test_do_add_column(self):
        """Should add a column to the GTK3MatrixView."""
        dut = self.make_dut()

        assert dut.n_columns == 0
        dut.do_add_column(1)
        assert dut.n_columns == 1

    @pytest.mark.integration
    def test_do_add_column_label(self):
        """Should add a GTK3Label widget with text and a tooltip to each column."""
        dut = self.make_dut()
        dut.do_set_column_headings([
            (
                "Column of the 1",
                "This is the first, and only, column in the MatrixView.",
            ),
        ])

        assert dut.n_columns == 1
        assert dut.n_rows == 0
        assert isinstance(dut.get_child_at(1, 0), GTK3Label)
        assert dut.get_child_at(1, 0).get_label() == "Column of the 1"
        assert (
            dut.get_child_at(1, 0).get_property("tooltip-markup")
            == "This is the first, and only, column in the MatrixView."
        )

    @pytest.mark.integration
    def test_do_add_row_label(self):
        """Should add a GTK3Label widget with text and a tooltip to each row."""
        dut = self.make_dut()
        dut.do_set_row_headings([
            (
                "Row of the 1",
                "This is the first, and only, row in the MatrixView.",
            ),
        ])

        assert dut.n_columns == 0
        assert dut.n_rows == 1
        assert isinstance(dut.get_child_at(0, 1), GTK3Label)
        assert dut.get_child_at(0, 1).get_label() == "Row of the 1"
        assert (
            dut.get_child_at(0, 1).get_property("tooltip-markup")
            == "This is the first, and only, row in the MatrixView."
        )

    @pytest.mark.unit
    def test_do_add_row(self):
        """Should add a row to the GTK3MatrixView."""
        dut = self.make_dut()

        assert dut.n_columns == 0
        dut.do_add_row(1)
        assert dut.n_rows == 1

    @pytest.mark.integration
    def test_do_add_combobox_widget(self):
        """Should add a GTK3ComboBox widget to the cell at X, Y coordinates."""
        _combo = GTK3ComboBox()
        dut = self.make_dut()
        dut.do_add_column(1)
        dut.do_add_row(1)
        dut.do_add_widget(_combo, 1, 1, 1, 1)

        assert dut.n_columns == 1
        assert dut.n_rows == 1
        assert isinstance(dut.do_get_widget(1, 1), GTK3ComboBox)

    @pytest.mark.integration
    def test_do_add_entry_widget(self):
        """Should add a GTK3Entry widget to the cell at X, Y coordinates."""
        _entry = GTK3Entry()
        dut = self.make_dut()
        dut.do_add_column(1)
        dut.do_add_row(1)
        dut.do_add_widget(_entry, 1, 1, 1, 1)

        assert dut.n_columns == 1
        assert dut.n_rows == 1
        assert isinstance(dut.do_get_widget(1, 1), GTK3Entry)

    @pytest.mark.integration
    def test_do_add_label_widget(self):
        """Should add a GTK3Label widget to the cell at X, Y coordinates."""
        _label = GTK3Label("Test Label")
        dut = self.make_dut()
        dut.do_add_column(1)
        dut.do_add_row(1)
        dut.do_add_widget(_label, 1, 1, 1, 1)

        assert dut.n_columns == 1
        assert dut.n_rows == 1
        assert isinstance(dut.do_get_widget(1, 1), GTK3Label)

    @pytest.mark.integration
    def test_do_add_textview_widget(self):
        """Should add a GTK3TextView widget to the cell at X, Y coordinates."""
        _textview = GTK3TextView(Gtk.TextBuffer())
        dut = self.make_dut()
        dut.do_add_column(1)
        dut.do_add_row(1)
        dut.do_add_widget(_textview.scrollwindow, 1, 1, 1, 1)

        assert dut.n_columns == 1
        assert dut.n_rows == 1
        assert isinstance(dut.do_get_widget(1, 1), Gtk.ScrolledWindow)

    @pytest.mark.integration
    def test_do_build_matrix(self):
        """Should build a 3 row by 3 column matrix."""
        dut = self.make_dut()

        assert dut.n_columns == 0
        assert dut.n_rows == 0

        dut.do_build_matrix(
            COLUMN_HEADINGS,
            ROW_HEADINGS,
        )

        assert dut.n_columns == 3
        assert dut.n_rows == 3
        assert isinstance(dut.get_child_at(0, 1), GTK3Label)
        assert dut.get_child_at(0, 1).get_label() == "Row 1"
        assert dut.get_child_at(0, 1).get_property("tooltip-markup") == "Row Tooltip 1"
        assert isinstance(dut.get_child_at(0, 2), GTK3Label)
        assert dut.get_child_at(0, 2).get_label() == "Row 2"
        assert dut.get_child_at(0, 2).get_property("tooltip-markup") == "Row Tooltip 2"
        assert isinstance(dut.get_child_at(0, 3), GTK3Label)
        assert dut.get_child_at(0, 3).get_label() == "Row 3"
        assert dut.get_child_at(0, 3).get_property("tooltip-markup") == "Row Tooltip 3"
        assert isinstance(dut.get_child_at(1, 0), GTK3Label)
        assert dut.get_child_at(1, 0).get_label() == "Column 1"
        assert (
            dut.get_child_at(1, 0).get_property("tooltip-markup") == "Column Tooltip 1"
        )
        assert isinstance(dut.get_child_at(2, 0), GTK3Label)
        assert dut.get_child_at(2, 0).get_label() == "Column 2"
        assert (
            dut.get_child_at(2, 0).get_property("tooltip-markup") == "Column Tooltip 2"
        )
        assert isinstance(dut.get_child_at(3, 0), GTK3Label)
        assert dut.get_child_at(3, 0).get_label() == "Column 3"
        assert (
            dut.get_child_at(3, 0).get_property("tooltip-markup") == "Column Tooltip 3"
        )

    @pytest.mark.xfail
    def test_do_get_widget(self):
        """Should retrieve the widget at the column/row intersection."""
        dut = self.make_dut()
        dut.do_build_matrix(
            COLUMN_HEADINGS,
            ROW_HEADINGS,
        )

        assert isinstance(dut.get_child_at(1, 1), GTK3ComboBox)
        assert isinstance(dut.get_child_at(1, 2), GTK3ComboBox)
        assert isinstance(dut.get_child_at(1, 3), GTK3ComboBox)
        assert isinstance(dut.get_child_at(1, 1), GTK3ComboBox)
        assert isinstance(dut.get_child_at(2, 1), GTK3ComboBox)
        assert isinstance(dut.get_child_at(3, 1), GTK3ComboBox)

    @pytest.mark.unit
    def test_do_remove_column(self):
        """Should remove a column from the GTK3MatrixView."""
        dut = self.make_dut()

        assert dut.n_columns == 0
        dut.do_add_column(1)
        dut.do_add_column(1)
        assert dut.n_columns == 2
        dut.do_remove_column(1)
        assert dut.n_columns == 1

    @pytest.mark.unit
    def test_do_remove_row(self):
        """Should remove a row from the GTK3MatrixView."""
        dut = self.make_dut()

        assert dut.n_rows == 0
        dut.do_add_row(1)
        dut.do_add_row(2)
        assert dut.n_rows == 2
        dut.do_remove_row(1)
        assert dut.n_rows == 1

    @pytest.mark.unit
    def test_do_set_column_headings(self):
        """Should add a row and populate with column heading Labels."""
        dut = self.make_dut()

        assert dut.n_columns == 0
        assert dut.n_rows == 0

        dut.do_set_column_headings(
            COLUMN_HEADINGS,
        )

        _label_lst = [
            dut.get_child_at(1, 0),
            dut.get_child_at(2, 0),
            dut.get_child_at(3, 0),
        ]

        assert dut.n_columns == 3
        assert dut.n_rows == 0
        assert isinstance(_label_lst[0], GTK3Label)
        assert _label_lst[0].get_label() == "Column 1"
        assert _label_lst[0].get_property("tooltip-markup") == COLUMN_HEADINGS[0][1]
        assert isinstance(_label_lst[1], GTK3Label)
        assert _label_lst[1].get_label() == "Column 2"
        assert _label_lst[1].get_property("tooltip-markup") == COLUMN_HEADINGS[1][1]
        assert isinstance(_label_lst[2], GTK3Label)
        assert _label_lst[2].get_label() == "Column 3"
        assert _label_lst[2].get_property("tooltip-markup") == COLUMN_HEADINGS[2][1]

    @pytest.mark.unit
    def test_do_set_row_headings(self):
        """Should add a column and populate with row heading Labels."""
        dut = self.make_dut()

        assert dut.n_columns == 0
        assert dut.n_rows == 0

        dut.do_set_row_headings(
            ROW_HEADINGS,
        )

        _label_lst = [
            dut.get_child_at(0, 1),
            dut.get_child_at(0, 2),
            dut.get_child_at(0, 3),
        ]

        assert dut.n_columns == 0
        assert dut.n_rows == 3
        assert isinstance(_label_lst[0], GTK3Label)
        assert _label_lst[0].get_label() == "Row 1"
        assert _label_lst[0].get_property("tooltip-markup") == ROW_HEADINGS[0][1]
        assert isinstance(_label_lst[1], GTK3Label)
        assert _label_lst[1].get_label() == "Row 2"
        assert _label_lst[1].get_property("tooltip-markup") == ROW_HEADINGS[1][1]
        assert isinstance(_label_lst[2], GTK3Label)
        assert _label_lst[2].get_label() == "Row 3"
        assert _label_lst[2].get_property("tooltip-markup") == ROW_HEADINGS[2][1]
