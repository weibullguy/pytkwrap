"""Test module for the GTK3IconView class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.icon import GTK3IconView
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
from tests.gtk3.icon.constants import (
    EXPECTED_ICONVIEW_HANDLER_IDS,
    EXPECTED_ICONVIEW_METHODS,
    EXPECTED_ICONVIEW_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3IconView(BaseGTK3GObjectTests):
    """Test class for the GTK3IconView class."""

    widget_class = GTK3IconView
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_ICONVIEW_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_ICONVIEW_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_ICONVIEW_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("activate_on_single_click")
        assert dut.do_get_property("cell_area") is None
        assert dut.do_get_property("column_spacing") == 6
        assert dut.do_get_property("columns") == -1
        assert dut.do_get_property("item_orientation") == Gtk.Orientation.VERTICAL
        assert dut.do_get_property("item_padding") == 6
        assert dut.do_get_property("item_width") == -1
        assert dut.do_get_property("markup_column") == -1
        assert dut.do_get_property("model") is None
        assert dut.do_get_property("pixbuf_column") == -1
        assert not dut.do_get_property("reorderable")
        assert dut.do_get_property("row_spacing") == 6
        assert dut.do_get_property("selection_mode") == Gtk.SelectionMode.SINGLE
        assert dut.do_get_property("spacing") == 0
        assert dut.do_get_property("text_column") == -1
        assert dut.do_get_property("tooltip_column") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _model = Gtk.ListStore()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                activate_on_single_click=True,
                column_spacing=36,
                columns=5,
                item_orientation=Gtk.Orientation.HORIZONTAL,
                item_padding=26,
                item_width=5,
                markup_column=4,
                model=_model,
                pixbuf_column=3,
                reorderable=True,
                row_spacing=16,
                selection_mode=Gtk.SelectionMode.MULTIPLE,
                spacing=10,
                text_column=1,
                tooltip_column=2,
            )
        )

        assert dut.get_property("activate_on_single_click")
        assert dut.get_activate_on_single_click()
        assert isinstance(dut.get_property("cell_area"), Gtk.CellArea)
        assert dut.get_property("column_spacing") == 36
        assert dut.get_column_spacing() == 36
        assert dut.get_property("columns") == 5
        assert dut.get_columns() == 5
        assert dut.get_property("item_orientation") == Gtk.Orientation.HORIZONTAL
        assert dut.get_item_orientation() == Gtk.Orientation.HORIZONTAL
        assert dut.get_property("item_padding") == 26
        assert dut.get_item_padding() == 26
        assert dut.get_property("item_width") == 5
        assert dut.get_item_width() == 5
        assert dut.get_property("markup_column") == 4
        assert dut.get_markup_column() == 4
        assert dut.get_property("model") is None
        assert dut.get_model() is None
        assert dut.get_property("pixbuf_column") == 3
        assert dut.get_pixbuf_column() == 3
        assert dut.get_property("reorderable")
        assert dut.get_reorderable()
        assert dut.get_property("row_spacing") == 16
        assert dut.get_row_spacing() == 16
        assert dut.get_property("selection_mode") == Gtk.SelectionMode.MULTIPLE
        assert dut.get_selection_mode() == Gtk.SelectionMode.MULTIPLE
        assert dut.get_property("spacing") == 10
        assert dut.get_spacing() == 10
        assert dut.get_property("text_column") == 1
        assert dut.get_text_column() == 1
        assert dut.get_property("tooltip_column") == 2
        assert dut.get_tooltip_column() == 2
