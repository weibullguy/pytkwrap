"""Test module for the GTK3Paned class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Paned
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
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
    EXPECTED_PANED_HANDLER_IDS,
    EXPECTED_PANED_METHODS,
    EXPECTED_PANED_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Paned(BaseGTK3GObjectTests):
    """Test class for the GTK3Paned class."""

    widget_class = GTK3Paned
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_PANED_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_PANED_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_PANED_PROPERTIES
    )

    def make_dut(self, orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL):
        return self.widget_class(orientation=orientation)

    @pytest.mark.unit
    def test_init_horizontal_paned(self):
        dut = self.make_dut()

        assert dut.orientation == Gtk.Orientation.HORIZONTAL

    @pytest.mark.unit
    def test_init_vertical_paned(self):
        dut = self.make_dut(orientation=Gtk.Orientation.VERTICAL)

        assert dut.orientation == Gtk.Orientation.VERTICAL

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("position") == 0
        assert not dut.do_get_property("position_set")
        assert not dut.do_get_property("wide_handle")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                position=25,
                position_set=True,
                wide_handle=True,
            )
        )

        assert dut.get_property("position") == 25
        assert dut.get_position() == 25
        assert dut.get_property("position_set")
        assert dut.get_property("wide_handle")
        assert dut.get_wide_handle()
