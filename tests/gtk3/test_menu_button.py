"""Test module for the GTK3MenuButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3MenuButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_METHODS,
    EXPECTED_BUTTON_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_MENU_BUTTON_ATTRIBUTES,
    EXPECTED_MENU_BUTTON_METHODS,
    EXPECTED_MENU_BUTTON_PROPERTIES,
    EXPECTED_TOGGLE_BUTTON_HANDLER_IDS,
    EXPECTED_TOGGLE_BUTTON_METHODS,
    EXPECTED_TOGGLE_BUTTON_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3MenuButton(BaseGTK3WidgetTests):
    """Test class for the GTK3MenuButton."""

    widget_class = GTK3MenuButton
    expected_attributes = EXPECTED_WIDGET_ATTRIBUTES | EXPECTED_MENU_BUTTON_ATTRIBUTES
    expected_default_height = 30
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_TOGGLE_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_TOGGLE_BUTTON_METHODS
        + EXPECTED_MENU_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_TOGGLE_BUTTON_PROPERTIES
        | EXPECTED_MENU_BUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_set_properties(self):
        """Should set the properties to the values passed in the
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                direction=Gtk.ArrowType.UP,
                use_popover=False,
            )
        )

        assert dut.do_get_property("direction") == Gtk.ArrowType.UP
        assert not dut.do_get_property("use_popover")
