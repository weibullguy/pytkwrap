"""Test module for the GTK3CellRendererCombo class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererCombo

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_RENDERER_HANDLER_IDS,
    EXPECTED_CELL_RENDERER_METHODS,
    EXPECTED_CELL_RENDERER_PROPERTIES,
    EXPECTED_CELLRENDERERCOMBO_HANDLER_IDS,
    EXPECTED_CELLRENDERERCOMBO_PROPERTIES,
    EXPECTED_CELLRENDERERTEXT_HANDLER_IDS,
    EXPECTED_CELLRENDERERTEXT_METHODS,
    EXPECTED_CELLRENDERERTEXT_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.order(3)
class TestGTK3CellRenderer(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererCombo class."""

    widget_class = GTK3CellRendererCombo
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_CELL_RENDERER_HANDLER_IDS
        | EXPECTED_CELLRENDERERTEXT_HANDLER_IDS
        | EXPECTED_CELLRENDERERCOMBO_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_CELL_RENDERER_METHODS
        + EXPECTED_CELLRENDERERTEXT_METHODS
    )
    expected_properties = (
        EXPECTED_CELL_RENDERER_PROPERTIES
        | EXPECTED_CELLRENDERERCOMBO_PROPERTIES
        | EXPECTED_CELLRENDERERTEXT_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("has_entry")
        assert dut.do_get_property("model") is None
        assert dut.do_get_property("text_column") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                has_entry=False,
                model=Gtk.TreeStore(),
                text_column=1,
            )
        )

        assert not dut.get_property("has_entry")
        assert isinstance(dut.get_property("model"), Gtk.TreeStore)
        assert dut.get_property("text_column") == 1
