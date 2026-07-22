"""Test module for the GTK3StyleContext class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import (
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
    set_widget_sensitivity,
)
from pytkwrap.gtk3.style import GTK3StyleContext
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.style.constants import (
    EXPECTED_STYLECONTEXT_HANDLER_IDS,
    EXPECTED_STYLECONTEXT_METHODS,
    EXPECTED_STYLECONTEXT_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3StyleContext(BaseGTK3GObjectTests):
    """Test class for the GTK3StyleContext class."""

    widget_class = GTK3StyleContext
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_STYLECONTEXT_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_STYLECONTEXT_METHODS
    expected_properties = EXPECTED_STYLECONTEXT_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("paint_clock") is None
        assert dut.do_get_property("parent") is None
        assert dut.do_get_property("screen") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _parent = Gtk.StyleContext()
        _screen = Gdk.Screen().get_default()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                paint_clock=None,
                parent=_parent,
                screen=_screen,
            )
        )

        assert dut.get_frame_clock() is None
        assert dut.get_parent() == _parent
        assert dut.get_screen() == _screen
