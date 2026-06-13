"""Test module for the GTK3Popover class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Popover

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_POPOVER_HANDLER_IDS,
    EXPECTED_POPOVER_METHODS,
    EXPECTED_POPOVER_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


class TestGTK3Popover(BaseGTK3GObjectTests):
    """Test class for the GTK3Popover class."""

    widget_class = GTK3Popover
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_POPOVER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_POPOVER_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_POPOVER_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("constrain_to") == Gtk.PopoverConstraint.WINDOW
        assert dut.do_get_property("modal")
        assert dut.do_get_property("pointing_to") is None
        assert dut.do_get_property("position") == Gtk.PositionType.TOP
        assert dut.do_get_property("relative_to") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _rectangle = Gdk.Rectangle()
        _widget = Gtk.Entry()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                constrain_to=Gtk.PopoverConstraint.NONE,
                modal=False,
                pointing_to=_rectangle,
                position=Gtk.PositionType.LEFT,
                relative_to=_widget,
            )
        )

        assert dut.get_property("constrain_to") == Gtk.PopoverConstraint.NONE
        assert not dut.get_property("modal")
        assert isinstance(dut.get_property("pointing_to"), Gdk.Rectangle)
        assert dut.get_property("position") == Gtk.PositionType.LEFT
        assert dut.get_property("relative_to") == _widget
