"""Test module for the GTK3AppChooserButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GObject, Gtk
from pytkwrap.gtk3.button import GTK3AppChooserButton
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.button.constants import (
    EXPECTED_APPCHOOSERBUTTON_HANDLER_IDS,
    EXPECTED_APPCHOOSERBUTTON_METHODS,
    EXPECTED_APPCHOOSERBUTTON_PROPERTIES,
)
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
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.io.constants import (
    EXPECTED_COMBOBOX_ATTRIBUTES,
    EXPECTED_COMBOBOX_HANDLER_IDS,
    EXPECTED_COMBOBOX_METHODS,
    EXPECTED_COMBOBOX_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3AppChooserButton(BaseGTK3GObjectTests):
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
        | EXPECTED_APPCHOOSERBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_COMBOBOX_METHODS
        + EXPECTED_APPCHOOSERBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_COMBOBOX_PROPERTIES
        | EXPECTED_APPCHOOSERBUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.do_get_attribute("column_types") == [GObject.TYPE_STRING]
        assert dut.do_get_attribute("default_value") == -1
        assert dut.do_get_attribute("edit_signal") == "changed"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                column_types=[GObject.TYPE_INT],
                default_value=1,
                edit_signal="combobox_changed",
            )
        )

        assert dut.do_get_attribute("column_types") == [GObject.TYPE_INT]
        assert dut.do_get_attribute("default_value") == 1
        assert dut.do_get_attribute("edit_signal") == "combobox_changed"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("heading") is None
        assert not dut.do_get_property("show_default_item")
        assert not dut.do_get_property("show_dialog_item")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
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
