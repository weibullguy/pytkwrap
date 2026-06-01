"""Test module for the GTK3AppChooserButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import GTK3AppChooserButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests
from .test_constants import (
    EXPECTED_APP_CHOOSER_BUTTON_HANDLER_IDS,
    EXPECTED_APP_CHOOSER_BUTTON_METHODS,
    EXPECTED_APP_CHOOSER_BUTTON_PROPERTIES,
    EXPECTED_BIN_METHODS,
    EXPECTED_COMBOBOX_ATTRIBUTES,
    EXPECTED_COMBOBOX_HANDLER_IDS,
    EXPECTED_COMBOBOX_METHODS,
    EXPECTED_COMBOBOX_PROPERTIES,
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
class TestGTK3AppChooserButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3AppChooserButton."""

    widget_class = GTK3AppChooserButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | (
        EXPECTED_WIDGET_ATTRIBUTES | EXPECTED_COMBOBOX_ATTRIBUTES
    )
    expected_default_height = 30
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_COMBOBOX_HANDLER_IDS
        | EXPECTED_APP_CHOOSER_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_COMBOBOX_METHODS
        + EXPECTED_APP_CHOOSER_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_COMBOBOX_PROPERTIES
        | EXPECTED_APP_CHOOSER_BUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties to the values passed in the
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                heading="Test Heading",
                show_default_item=True,
                show_dialog_item=True,
            )
        )

        assert dut.do_get_property("heading") == "Test Heading"
        assert dut.do_get_property("show_default_item")
        assert dut.do_get_property("show_dialog_item")
