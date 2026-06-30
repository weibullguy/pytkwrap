"""Test module for the GTK3Menu class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.menu import GTK3Menu
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
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.menu.constants import (
    EXPECTED_MENU_HANDLER_IDS,
    EXPECTED_MENU_METHODS,
    EXPECTED_MENU_PROPERTIES,
    EXPECTED_MENUSHELL_HANDLER_IDS,
    EXPECTED_MENUSHELL_METHODS,
    EXPECTED_MENUSHELL_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Menu(BaseGTK3GObjectTests):
    """Test class for the GTK3Menu class."""

    widget_class = GTK3Menu
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_MENUSHELL_HANDLER_IDS
        | EXPECTED_MENU_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_MENUSHELL_METHODS
        + EXPECTED_MENU_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_MENUSHELL_PROPERTIES
        | EXPECTED_MENU_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("accel_group") is None
        assert dut.do_get_property("accel_path") is None
        assert dut.do_get_property("active") == -1
        assert dut.do_get_property("anchor_hints") == (
            Gdk.AnchorHints.FLIP_X
            | Gdk.AnchorHints.FLIP_Y
            | Gdk.AnchorHints.SLIDE_X
            | Gdk.AnchorHints.SLIDE_Y
            | Gdk.AnchorHints.RESIZE_X
            | Gdk.AnchorHints.RESIZE_Y
            | Gdk.AnchorHints.FLIP
            | Gdk.AnchorHints.SLIDE
            | Gdk.AnchorHints.RESIZE
        )
        assert dut.do_get_property("attach_widget") is None
        assert dut.do_get_property("menu_type_hint") == Gdk.WindowTypeHint.POPUP_MENU
        assert dut.do_get_property("monitor") == -1
        assert dut.do_get_property("rect_anchor_dx") == 0
        assert dut.do_get_property("rect_anchor_dy") == 0
        assert dut.do_get_property("reserve_toggle_size")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _accel_group = Gtk.AccelGroup()
        _attach_widget = Gtk.Entry()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                accel_group=_accel_group,
                active=2,
                anchor_hints=Gdk.AnchorHints.FLIP,
                attach_widget=_attach_widget,
                menu_type_hint=Gdk.WindowTypeHint.TOOLTIP,
                monitor=3,
                rect_anchor_dx=20,
                rect_anchor_dy=10,
                reserve_toggle_size=False,
            )
        )

        assert dut.get_property("accel_group") == _accel_group
        assert dut.get_accel_group() == _accel_group
        assert dut.get_property("accel_path") is None
        assert dut.get_accel_path() is None
        assert dut.get_property("active") == -1
        assert dut.get_active() is None
        assert dut.get_property("anchor_hints") == Gdk.AnchorHints.FLIP
        assert dut.get_property("attach_widget") == _attach_widget
        assert dut.get_attach_widget() == _attach_widget
        assert dut.get_property("menu_type_hint") == Gdk.WindowTypeHint.TOOLTIP
        assert dut.get_property("monitor") == 3
        assert dut.get_monitor() == 3
        assert dut.get_property("rect_anchor_dx") == 20
        assert dut.get_property("rect_anchor_dy") == 10
        assert not dut.get_property("reserve_toggle_size")
        assert not dut.get_reserve_toggle_size()
