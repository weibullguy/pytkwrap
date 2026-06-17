"""Test module for the GTK3CellRendererSpin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererSpin

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CELL_RENDERER_HANDLER_IDS,
    EXPECTED_CELL_RENDERER_METHODS,
    EXPECTED_CELL_RENDERER_PROPERTIES,
    EXPECTED_CELLRENDERERSPIN_PROPERTIES,
    EXPECTED_CELLRENDERERTEXT_HANDLER_IDS,
    EXPECTED_CELLRENDERERTEXT_METHODS,
    EXPECTED_CELLRENDERERTEXT_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CellRendererSpin(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererSpin class."""

    widget_class = GTK3CellRendererSpin
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_CELL_RENDERER_HANDLER_IDS
        | EXPECTED_CELLRENDERERTEXT_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_CELL_RENDERER_METHODS
        + EXPECTED_CELLRENDERERTEXT_METHODS
    )
    expected_properties = (
        EXPECTED_CELL_RENDERER_PROPERTIES
        | EXPECTED_CELLRENDERERTEXT_PROPERTIES
        | EXPECTED_CELLRENDERERSPIN_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("adjustment") is None
        assert dut.do_get_property("climb_rate") == 0.0
        assert dut.do_get_property("digits") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                climb_rate=1.0,
                digits=2,
            )
        )

        assert isinstance(dut.do_get_property("adjustment"), Gtk.Adjustment)
        assert dut.do_get_property("climb_rate") == 1.0
        assert dut.do_get_property("digits") == 2
