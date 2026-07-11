"""Test module for the GTK3GLArea class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.layout import GTK3GLArea
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GLAREA_HANDLER_IDS,
    EXPECTED_GLAREA_METHODS,
    EXPECTED_GLAREA_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3GLArea(BaseGTK3GObjectTests):
    """Test class for the GTK3GLArea class."""

    widget_class = GTK3GLArea
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_GLAREA_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_GLAREA_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_GLAREA_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("auto_render")
        assert not dut.do_get_property("has_alpha")
        assert not dut.do_get_property("has_depth_buffer")
        assert not dut.do_get_property("has_stencil_buffer")
        assert not dut.do_get_property("use_es")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                auto_render=False,
                has_alpha=True,
                has_depth_buffer=True,
                has_stencil_buffer=True,
                use_es=True,
            )
        )

        assert not dut.get_property("auto_render")
        assert not dut.get_auto_render()
        assert dut.get_property("has_alpha")
        assert dut.get_has_alpha()
        assert dut.get_property("has_depth_buffer")
        assert dut.get_has_depth_buffer()
        assert dut.get_property("has_stencil_buffer")
        assert dut.get_has_stencil_buffer()
        assert dut.get_property("use_es")
        assert dut.get_use_es()
