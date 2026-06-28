"""Test module for the GTK3CellRendererToggle class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererToggle
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import EXPECTED_GOBJECT_HANDLER_IDS, EXPECTED_GOBJECT_METHODS
from tests.gtk3.treeview.constants import (
    EXPECTED_CELLRENDERER_HANDLER_IDS,
    EXPECTED_CELLRENDERER_METHODS,
    EXPECTED_CELLRENDERER_PROPERTIES,
    EXPECTED_CELLRENDERERTOGGLE_HANDLER_IDS,
    EXPECTED_CELLRENDERERTOGGLE_METHODS,
    EXPECTED_CELLRENDERERTOGGLE_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CellRendererToggle(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererToggle class."""

    widget_class = GTK3CellRendererToggle
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_CELLRENDERER_HANDLER_IDS
        | EXPECTED_CELLRENDERERTOGGLE_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_CELLRENDERER_METHODS
        + EXPECTED_CELLRENDERERTOGGLE_METHODS
    )
    expected_properties = (
        EXPECTED_CELLRENDERER_PROPERTIES | EXPECTED_CELLRENDERERTOGGLE_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("activatable")
        assert not dut.do_get_property("active")
        assert not dut.do_get_property("inconsistent")
        assert not dut.do_get_property("radio")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                activatable=False,
                active=True,
                inconsistent=True,
                radio=True,
            )
        )

        assert not dut.get_property("activatable")
        assert dut.get_property("active")
        assert dut.get_property("inconsistent")
        assert dut.get_property("radio")
