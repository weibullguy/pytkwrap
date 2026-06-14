"""Test module for the GTK3RadioToolButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button import GTK3RadioButton
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool import GTK3RadioToolButton

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
    EXPECTED_RADIOTOOLBUTTON_METHODS,
    EXPECTED_RADIOTOOLBUTTON_PROPERTIES,
    EXPECTED_TOGGLETOOLBUTTON_HANDLER_IDS,
    EXPECTED_TOGGLETOOLBUTTON_METHODS,
    EXPECTED_TOGGLETOOLBUTTON_PROPERTIES,
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


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3RadioToolButton(BaseGTK3GObjectTests):
    """Test class for the GTK3RadioToolButton class."""

    widget_class = GTK3RadioToolButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TOOLITEM_HANDLER_IDS
        | EXPECTED_TOOLBUTTON_HANDLER_IDS
        | EXPECTED_TOGGLETOOLBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_TOOLITEM_METHODS
        + EXPECTED_TOOLBUTTON_METHODS
        + EXPECTED_TOGGLETOOLBUTTON_METHODS
        + EXPECTED_RADIOTOOLBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TOOLITEM_PROPERTIES
        | EXPECTED_TOOLBUTTON_PROPERTIES
        | EXPECTED_TOGGLETOOLBUTTON_PROPERTIES
        | EXPECTED_RADIOTOOLBUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("group") is None

    @pytest.mark.skip(
        reason=(
            "GTK3RadioToolButton crashes at the C level when run as part of the "
            "full test suite due to GIO volume monitor initialization conflicts. "
            "Passes in isolation. Requires manual testing."
        )
    )
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _radiobutton = GTK3RadioButton()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                group=[_radiobutton],
            )
        )

        assert dut.do_get_property("group") == [_radiobutton]
