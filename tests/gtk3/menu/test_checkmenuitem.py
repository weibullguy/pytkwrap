"""Test module for the GTK3CheckMenuItem class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.menu import GTK3CheckMenuItem
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
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.menu.constants import (
    EXPECTED_CHECKMENUITEM_HANDLER_IDS,
    EXPECTED_CHECKMENUITEM_METHODS,
    EXPECTED_CHECKMENUITEM_PROPERTIES,
    EXPECTED_MENUITEM_HANDLER_IDS,
    EXPECTED_MENUITEM_METHODS,
    EXPECTED_MENUITEM_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CheckMenuItem(BaseGTK3GObjectTests):
    """Test class for the GTK3CheckMenuItem class."""

    widget_class = GTK3CheckMenuItem
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_MENUITEM_HANDLER_IDS
        | EXPECTED_CHECKMENUITEM_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_MENUITEM_METHODS
        + EXPECTED_CHECKMENUITEM_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_MENUITEM_PROPERTIES
        | EXPECTED_CHECKMENUITEM_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("active")
        assert not dut.do_get_property("draw_as_radio")
        assert not dut.do_get_property("inconsistent")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                active=True,
                draw_as_radio=True,
                inconsistent=True,
            )
        )

        assert dut.do_get_property("active")
        assert dut.do_get_property("draw_as_radio")
        assert dut.do_get_property("inconsistent")
