"""Test module for the GTK3CellView class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import (
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
    set_widget_sensitivity,
)
from pytkwrap.gtk3.treeview import GTK3CellView

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_VIEW_METHODS,
    EXPECTED_CELL_VIEW_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


class TestGTK3CellView(BaseGTK3GObjectTests):
    """Test class for the GTK3CellView class."""

    widget_class = GTK3CellView
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_CELL_VIEW_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_CELL_VIEW_PROPERTIES

    def make_dut(self, cell_area_context=None):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class(cell_area_context)

    @pytest.mark.unit
    def test_init_with_cell_area_context(self):
        cell_area_context = Gtk.CellAreaContext()
        dut = self.make_dut(cell_area_context=cell_area_context)

        assert isinstance(dut.get_property("cell_area"), Gtk.CellArea)
        assert dut.get_property("cell_area_context") == cell_area_context

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("background") is None
        assert dut.do_get_property("background_rgba") is None
        assert not dut.do_get_property("background_set")
        assert dut.do_get_property("cell_area") is None
        assert dut.do_get_property("cell_area_context") is None
        assert not dut.do_get_property("draw_sensitive")
        assert not dut.do_get_property("fit_model")
        assert dut.do_get_property("model") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                background="blue",
                background_rgba=None,
                background_set=True,
                cell_area_context=Gtk.CellAreaContext(),
                draw_sensitive=True,
                fit_model=True,
                model=Gtk.ListStore(),
            )
        )

        assert dut.do_get_property("background") == "blue"
        assert isinstance(dut.get_property("background_rgba"), Gdk.RGBA)
        assert dut.get_property("background_rgba").alpha == 1.0
        assert dut.get_property("background_rgba").blue == 1.0
        assert dut.get_property("background_rgba").green == 0.0
        assert dut.get_property("background_rgba").red == 0.0
        assert dut.get_property("background_set")
        assert isinstance(dut.get_property("cell_area"), Gtk.CellArea)
        assert isinstance(dut.get_property("cell_area_context"), Gtk.CellAreaContext)
        assert dut.get_property("draw_sensitive")
        assert dut.get_property("fit_model")
        assert isinstance(dut.get_property("model"), Gtk.ListStore)

    @pytest.mark.unit
    def test_do_set_properties_background_rgba(self):
        """Should set the background using a Gdk.RGBA object."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                background=None,
                background_rgba=Gdk.RGBA(
                    0.5,
                    0.2,
                    1.0,
                    0.75,
                ),
            )
        )

        assert isinstance(dut.get_property("background_rgba"), Gdk.RGBA)
        assert dut.get_property("background_rgba").alpha == 0.75
        assert dut.get_property("background_rgba").blue == 1.0
        assert dut.get_property("background_rgba").green == 0.2
        assert dut.get_property("background_rgba").red == 0.5
