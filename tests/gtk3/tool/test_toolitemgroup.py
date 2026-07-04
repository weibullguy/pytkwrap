"""Test module for the GTK3ToolItemGroup class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool import GTK3ToolItemGroup
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
)
from tests.gtk3.tool.constants import (
    EXPECTED_TOOLITEMGROUP_METHODS,
    EXPECTED_TOOLITEMGROUP_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ToolItemGroup(BaseGTK3GObjectTests):
    """Test class for the GTK3ToolItemGroup class."""

    widget_class = GTK3ToolItemGroup
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
        + EXPECTED_TOOLITEMGROUP_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TOOLITEMGROUP_PROPERTIES
    )

    def make_dut(self, label: str = ""):
        return self.widget_class(label=label)

    @pytest.mark.unit
    def test_init_with_label(self):
        dut = self.make_dut("Test Label")

        assert dut.do_get_property("label") == "Test Label"
        assert dut.get_property("label") == "Test Label"
        assert dut.get_label() == "Test Label"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("collapsed")
        assert dut.do_get_property("ellipsize") == Pango.EllipsizeMode.NONE
        assert dut.do_get_property("header_relief") == Gtk.ReliefStyle.NORMAL
        assert dut.do_get_property("label") == ""
        assert dut.do_get_property("label_widget") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                collapsed=True,
                ellipsize=Pango.EllipsizeMode.MIDDLE,
                header_relief=Gtk.ReliefStyle.NONE,
                label="Test Label",
            )
        )

        assert dut.get_property("collapsed")
        assert dut.get_collapsed()
        assert dut.get_property("ellipsize") == Pango.EllipsizeMode.MIDDLE
        assert dut.get_ellipsize() == Pango.EllipsizeMode.MIDDLE
        assert dut.get_property("header_relief") == Gtk.ReliefStyle.NONE
        assert dut.get_header_relief() == Gtk.ReliefStyle.NONE
        assert dut.get_property("label") == "Test Label"
        assert dut.get_label() == "Test Label"
        assert dut.get_property("label_widget").get_text() == "Test Label"
        assert dut.get_label_widget().get_text() == "Test Label"

    @pytest.mark.unit
    def test_do_set_properties_label_widget(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                label_widget=Gtk.Label(label="Test Label Widget"),
            )
        )

        assert dut.get_property("label") == "Test Label Widget"
        assert dut.get_label() == "Test Label Widget"
        assert dut.get_property("label_widget").get_text() == "Test Label Widget"
        assert dut.get_label_widget().get_text() == "Test Label Widget"
