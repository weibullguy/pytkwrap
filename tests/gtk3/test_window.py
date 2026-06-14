"""Test module for the GTK3Window class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window import GTK3Window

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
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
    EXPECTED_WINDOW_HANDLER_IDS,
    EXPECTED_WINDOW_METHODS,
    EXPECTED_WINDOW_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Window(BaseGTK3GObjectTests):
    """Test class for the GTK3Window class."""

    widget_class = GTK3Window
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_WINDOW_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_WINDOW_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
    )

    def make_dut(self, wtype: Gtk.WindowType = Gtk.WindowType.TOPLEVEL):
        return self.widget_class(wtype)

    @pytest.mark.unit
    def test_init_as_popup(self):
        dut = self.make_dut(Gtk.WindowType.POPUP)

        assert dut.get_property("type") == Gtk.WindowType.POPUP

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("accept_focus")
        assert dut.do_get_property("application") is None
        assert dut.do_get_property("attached_to") is None
        assert dut.do_get_property("decorated")
        assert dut.do_get_property("default_height") == -1
        assert dut.do_get_property("default_width") == -1
        assert dut.do_get_property("deletable")
        assert not dut.do_get_property("destroy_with_parent")
        assert dut.do_get_property("focus_on_map")
        assert dut.do_get_property("focus_visible")
        assert dut.do_get_property("gravity") == Gdk.Gravity.NORTH_WEST
        assert not dut.do_get_property("has_toplevel_focus")
        assert not dut.do_get_property("hide_titlebar_when_maximized")
        assert dut.do_get_property("icon") is None
        assert dut.do_get_property("icon_name") is None
        assert dut.do_get_property("mnemonics_visible")
        assert not dut.do_get_property("modal")
        assert dut.do_get_property("resizable")
        assert dut.do_get_property("role") is None
        assert dut.do_get_property("screen") is None
        assert not dut.do_get_property("skip_taskbar_hint")
        assert dut.do_get_property("startup_id") is None
        assert dut.do_get_property("title") == "pytkwrap GTK3 window"
        assert dut.do_get_property("transient_for") is None
        assert dut.do_get_property("type") == Gtk.WindowType.TOPLEVEL
        assert dut.do_get_property("type_hint") == Gdk.WindowTypeHint.NORMAL
        assert not dut.do_get_property("urgency_hint")
        assert dut.do_get_property("window_position") == Gtk.WindowPosition.NONE

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _application = Gtk.Application()
        _attached_to = Gtk.Window()
        _icon = GdkPixbuf.Pixbuf()
        _window = Gtk.Window()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                accept_focus=False,
                application=_application,
                attached_to=_attached_to,
                decorated=False,
                default_height=100,
                default_width=50,
                deletable=False,
                destroy_with_parent=True,
                focus_on_map=False,
                focus_visible=False,
                gravity=Gdk.Gravity.CENTER,
                hide_titlebar_when_maximized=True,
                icon=_icon,
                icon_name=None,
                mnemonics_visible=False,
                modal=True,
                resizable=False,
                role="Test Role",
                skip_taskbar_hint=True,
                startup_id="Test Startup ID",
                title="Test Window Title",
                transient_for=_window,
                type_hint=Gdk.WindowTypeHint.TOOLTIP,
                urgency_hint=True,
                window_position=Gtk.WindowPosition.CENTER,
            )
        )

        assert not dut.get_property("accept_focus")
        assert dut.get_property("application") == _application
        assert dut.get_property("attached_to") == _attached_to
        assert not dut.get_property("decorated")
        assert dut.get_property("default_height") == 100
        assert dut.get_property("default_width") == 50
        assert not dut.get_property("deletable")
        assert dut.get_property("destroy_with_parent")
        assert not dut.get_property("focus_on_map")
        assert not dut.get_property("focus_visible")
        assert dut.get_property("gravity") == Gdk.Gravity.CENTER
        assert not dut.get_property("has_toplevel_focus")
        assert dut.get_property("hide_titlebar_when_maximized")
        assert dut.get_property("icon") == _icon
        assert dut.get_property("icon_name") is None
        assert not dut.get_property("mnemonics_visible")
        assert dut.get_property("modal")
        assert not dut.get_property("resizable")
        assert dut.get_property("role") == "Test Role"
        assert isinstance(dut.get_property("screen"), Gdk.Screen)
        assert dut.get_property("skip_taskbar_hint")
        assert dut.get_property("title") == "Test Window Title"
        assert dut.get_property("transient_for") == _window
        assert dut.get_property("type") == Gtk.WindowType.TOPLEVEL
        assert dut.get_property("type_hint") == Gdk.WindowTypeHint.TOOLTIP
        assert dut.get_property("urgency_hint")
        assert dut.get_property("window_position") == Gtk.WindowPosition.CENTER
