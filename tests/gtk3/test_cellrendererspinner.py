"""Test module for the GTK3CellRendererSpinner class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererSpinner

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_RENDERER_HANDLER_IDS,
    EXPECTED_CELL_RENDERER_METHODS,
    EXPECTED_CELL_RENDERER_PROPERTIES,
    EXPECTED_CELLRENDERESPINNER_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CellRenderer(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererSpinner class."""

    widget_class = GTK3CellRendererSpinner
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_CELL_RENDERER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_CELL_RENDERER_METHODS
    expected_properties = (
        EXPECTED_CELL_RENDERER_PROPERTIES | EXPECTED_CELLRENDERESPINNER_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("active")
        assert dut.do_get_property("pulse") == 0
        assert dut.do_get_property("size") == Gtk.IconSize.MENU

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                active=True,
                pulse=10,
                size=Gtk.IconSize.BUTTON,
            )
        )

        assert dut.do_get_property("active")
        assert dut.do_get_property("pulse") == 10
        assert dut.do_get_property("size") == Gtk.IconSize.BUTTON
