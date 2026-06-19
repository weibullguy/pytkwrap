"""Test module for the GTK3ButtonBox class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3ButtonBox
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BOX_METHODS,
    EXPECTED_BOX_PROPERTIES,
    EXPECTED_BUTTONBOX_METHODS,
    EXPECTED_BUTTONBOX_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ButtonBox(BaseGTK3GObjectTests):
    """Test class for the GTK3ButtonBox class."""

    widget_class = GTK3ButtonBox
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BOX_METHODS
        + EXPECTED_BUTTONBOX_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BOX_PROPERTIES
        | EXPECTED_BUTTONBOX_PROPERTIES
    )

    def make_dut(self, orientation=Gtk.Orientation.HORIZONTAL):
        """Create a device under test for the GTK3ButtonBox."""
        return self.widget_class(orientation)

    @pytest.mark.unit
    def test_init_with_orientation(self):
        """Should create a GTK3ButtonBox with the passed orientation."""
        dut = self.make_dut(orientation=Gtk.Orientation.VERTICAL)

        assert dut.get_property("orientation") == Gtk.Orientation.VERTICAL

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("layout_style") == Gtk.ButtonBoxStyle.END

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                layout_style=Gtk.ButtonBoxStyle.EDGE,
            )
        )

        assert dut.get_property("layout_style") == Gtk.ButtonBoxStyle.EDGE
        assert dut.get_layout() == Gtk.ButtonBoxStyle.EDGE
