"""Test module for the GTK3Stack class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Stack
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
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
    EXPECTED_STACK_METHODS,
    EXPECTED_STACK_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Stack(BaseGTK3GObjectTests):
    """Test class for the GTK3Stack class."""

    widget_class = GTK3Stack
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
        + EXPECTED_STACK_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_STACK_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("hhomogeneous")
        assert dut.do_get_property("homogeneous")
        assert not dut.do_get_property("interpolate_size")
        assert dut.do_get_property("transition_duration") == 200
        assert dut.do_get_property("transition_type") == Gtk.StackTransitionType.NONE
        assert dut.do_get_property("vhomogeneous")
        assert dut.do_get_property("visible_child") is None
        assert dut.do_get_property("visible_child_name") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _child = Gtk.Label()
        _child.show()

        dut = self.make_dut()
        dut.add_named(_child, "Test Child")
        dut.do_set_properties(
            GTK3WidgetProperties(
                hhomogeneous=False,
                homogeneous=False,
                interpolate_size=True,
                transition_duration=500,
                transition_type=Gtk.StackTransitionType.UNDER_UP,
                vhomogeneous=False,
                visible_child=_child,
                visible_child_name="Test Child",
            )
        )

        assert not dut.get_property("hhomogeneous")
        assert not dut.get_hhomogeneous()
        assert not dut.get_property("homogeneous")
        assert not dut.get_homogeneous()
        assert dut.get_property("interpolate_size")
        assert dut.get_interpolate_size()
        assert dut.get_property("transition_duration") == 500
        assert dut.get_transition_duration() == 500
        assert dut.get_property("transition_type") == Gtk.StackTransitionType.UNDER_UP
        assert dut.get_transition_type() == Gtk.StackTransitionType.UNDER_UP
        assert not dut.get_property("vhomogeneous")
        assert not dut.get_vhomogeneous()
        assert dut.get_property("visible_child") == _child
        assert dut.get_visible_child() == _child
        assert dut.get_property("visible_child_name") == "Test Child"
        assert dut.get_visible_child_name() == "Test Child"
