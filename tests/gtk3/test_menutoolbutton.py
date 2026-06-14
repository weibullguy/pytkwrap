"""Test module for the GTK3MenuToolButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool import GTK3MenuToolButton

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
    EXPECTED_MENUTOOLBUTTON_HANDLER_IDS,
    EXPECTED_MENUTOOLBUTTON_METHODS,
    EXPECTED_MENUTOOLBUTTON_PROPERTIES,
    EXPECTED_TOOLBUTTON_HANDLER_IDS,
    EXPECTED_TOOLBUTTON_METHODS,
    EXPECTED_TOOLBUTTON_PROPERTIES,
    EXPECTED_TOOLITEM_HANDLER_IDS,
    EXPECTED_TOOLITEM_METHODS,
    EXPECTED_TOOLITEM_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


class TestGTK3MenuToolButton(BaseGTK3GObjectTests):
    """Test class for the GTK3MenuToolButton class."""

    widget_class = GTK3MenuToolButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TOOLITEM_HANDLER_IDS
        | EXPECTED_TOOLBUTTON_HANDLER_IDS
        | EXPECTED_MENUTOOLBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_TOOLITEM_METHODS
        + EXPECTED_TOOLBUTTON_METHODS
        + EXPECTED_MENUTOOLBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TOOLITEM_PROPERTIES
        | EXPECTED_TOOLBUTTON_PROPERTIES
        | EXPECTED_MENUTOOLBUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("menu") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _menu = Gtk.Menu()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                menu=_menu,
            )
        )

        assert dut.get_property("menu") == _menu
