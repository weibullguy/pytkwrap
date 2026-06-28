"""Test module for the GTK3ToolButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool import GTK3ToolButton
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
from tests.gtk3.tool.constants import (
    EXPECTED_TOOLBUTTON_HANDLER_IDS,
    EXPECTED_TOOLBUTTON_METHODS,
    EXPECTED_TOOLBUTTON_PROPERTIES,
    EXPECTED_TOOLITEM_HANDLER_IDS,
    EXPECTED_TOOLITEM_METHODS,
    EXPECTED_TOOLITEM_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ToolButton(BaseGTK3GObjectTests):
    """Test class for the GTK3ToolButton class."""

    widget_class = GTK3ToolButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TOOLITEM_HANDLER_IDS
        | EXPECTED_TOOLBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_TOOLITEM_METHODS
        + EXPECTED_TOOLBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TOOLITEM_PROPERTIES
        | EXPECTED_TOOLBUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("icon_name") is None
        assert dut.do_get_property("icon_widget") is None
        assert dut.do_get_property("label") is None
        assert dut.do_get_property("label_widget") is None
        assert not dut.do_get_property("use_underline")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _label = Gtk.Label(label="Test Label")
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                icon_name=None,
                icon_widget=None,
                label="Test Label",
                label_widget=_label,
                use_underline=True,
            )
        )

        assert dut.get_property("icon_name") is None
        assert dut.get_property("icon_widget") is None
        assert dut.get_property("label") == "Test Label"
        assert dut.get_property("label_widget") == _label
        assert dut.get_property("use_underline")
