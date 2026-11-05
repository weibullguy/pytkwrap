"""Test module for the GTK3ActionBar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3WidgetProperties

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.bar import GTK3ActionBar
from pytkwrap.gtk3.io import GTK3Label
from tests.gtk3.bar.constants import (
    EXPECTED_ACTIONBAR_METHODS,
    EXPECTED_ACTIONBAR_PROPERTIES,
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


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ActionBar(BaseGTK3GObjectTests):
    """Test class for the GTK3ActionBar class."""

    widget_class = GTK3ActionBar
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_ACTIONBAR_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_ACTIONBAR_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("center_widget") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _center_widget = GTK3Label("Center Widget")

        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(center_widget=_center_widget))

        assert dut.do_get_property("center_widget") == _center_widget
        assert dut.get_center_widget() == _center_widget

    @pytest.mark.unit
    def test_do_add_child_start(self):
        """Should add a child with reference to the start of the GTK3ActionBar."""
        _child = GTK3Label("Pack Start")

        dut = self.make_dut()
        dut.do_add_child(_child)

        assert dut.get_children()[0] == _child
        assert dut.get_children()[0].get_label() == "Pack Start"

    @pytest.mark.unit
    def test_do_add_child_end(self):
        """Should add a child with reference to the end of the GTK3ActionBar."""
        _child = GTK3Label("Pack End")

        dut = self.make_dut()
        dut.do_add_child(_child, False)

        assert dut.get_children()[0] == _child
        assert dut.get_children()[0].get_label() == "Pack End"
