"""Test module for the GTK3CellRendererProgress class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3CellRendererProgress
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import EXPECTED_GOBJECT_HANDLER_IDS, EXPECTED_GOBJECT_METHODS
from tests.gtk3.treeview.constants import (
    EXPECTED_CELLRENDERER_HANDLER_IDS,
    EXPECTED_CELLRENDERER_METHODS,
    EXPECTED_CELLRENDERER_PROPERTIES,
    EXPECTED_CELLRENDERERPROGRESS_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CellRendererProgress(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRendererProgress class."""

    widget_class = GTK3CellRendererProgress
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_CELLRENDERER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_CELLRENDERER_METHODS
    expected_properties = (
        EXPECTED_CELLRENDERER_PROPERTIES | EXPECTED_CELLRENDERERPROGRESS_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("inverted")
        assert dut.do_get_property("pulse") == -1
        assert dut.do_get_property("text") is None
        assert dut.do_get_property("text_xalign") == 0.5
        assert dut.do_get_property("text_yalign") == 0.5
        assert dut.do_get_property("value") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                inverted=True,
                pulse=5,
                text="Test Text",
                text_xalign=0.75,
                text_yalign=0.25,
                value=4,
            )
        )

        assert dut.do_get_property("inverted")
        assert dut.do_get_property("pulse") == 5
        assert dut.do_get_property("text") == "Test Text"
        assert dut.do_get_property("text_xalign") == 0.75
        assert dut.do_get_property("text_yalign") == 0.25
        assert dut.do_get_property("value") == 4
