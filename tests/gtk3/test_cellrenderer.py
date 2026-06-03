"""Test module for the GTK3CellRenderer class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.cellrenderer import GTK3CellRenderer
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_RENDERER_HANDLER_IDS,
    EXPECTED_CELL_RENDERER_METHODS,
    EXPECTED_CELL_RENDERER_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.order(3)
class TestGTK3CellRenderer(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRenderer class."""

    widget_class = GTK3CellRenderer
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_CELL_RENDERER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_CELL_RENDERER_METHODS
    expected_properties = EXPECTED_CELL_RENDERER_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("cell_background") is None
        assert dut.do_get_property("cell_background_rgba") is None
        assert not dut.do_get_property("cell_background_set")
        assert dut.do_get_property("height") == -1
        assert not dut.do_get_property("is_expanded")
        assert not dut.do_get_property("is_expander")
        assert dut.do_get_property("mode") == Gtk.CellRendererMode.INERT
        assert dut.do_get_property("sensitive")
        assert dut.do_get_property("visible")
        assert dut.do_get_property("width") == -1
        assert dut.do_get_property("xalign") == 0.5
        assert dut.do_get_property("xpad") == 0
        assert dut.do_get_property("yalign") == 0.5
        assert dut.do_get_property("ypad") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                cell_background="red",
                height=10,
                mode=Gtk.CellRendererMode.EDITABLE,
                sensitive=False,
                visible=False,
                width=20,
                xalign=0.2,
                xpad=10,
                yalign=0.3,
                ypad=20,
            )
        )

        assert dut.do_get_property("cell_background") == "red"
        assert dut.do_get_property("cell_background_rgba") is None
        assert not dut.do_get_property("cell_background_set")
        assert dut.do_get_property("height") == 10
        assert not dut.do_get_property("is_expanded")
        assert not dut.do_get_property("is_expander")
        assert dut.do_get_property("mode") == Gtk.CellRendererMode.EDITABLE
        assert not dut.do_get_property("sensitive")
        assert not dut.do_get_property("visible")
        assert dut.do_get_property("width") == 20
        assert dut.do_get_property("xalign") == 0.2
        assert dut.do_get_property("xpad") == 10
        assert dut.do_get_property("yalign") == 0.3
        assert dut.do_get_property("ypad") == 20

    @pytest.mark.unit
    def test_do_set_properties_background_rgba(self):
        """Should set the properties of a GTK3CellRenderer."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                cell_background_rgba=Gdk.RGBA(1.0, 0.0, 0.0, 1.0),
                mode=Gtk.CellRendererMode.EDITABLE,
            )
        )

        assert dut.do_get_property("cell_background") is None
        assert dut.do_get_property("cell_background_rgba") == Gdk.RGBA(
            1.0, 0.0, 0.0, 1.0
        )
        assert not dut.do_get_property("cell_background_set")
        assert dut.do_get_property("height") == -1
        assert not dut.do_get_property("is_expanded")
        assert not dut.do_get_property("is_expander")
        assert dut.do_get_property("mode") == Gtk.CellRendererMode.EDITABLE
        assert dut.do_get_property("sensitive")
        assert dut.do_get_property("visible")
        assert dut.do_get_property("width") == -1
        assert dut.do_get_property("xalign") == 0.5
        assert dut.do_get_property("xpad") == 0
        assert dut.do_get_property("yalign") == 0.5
        assert dut.do_get_property("ypad") == 0
