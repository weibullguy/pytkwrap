"""Test module for the GTK3StyleContext class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.style import GTK3CssProvider, GTK3StyleContext
from pytkwrap.gtk3.window import GTK3Window
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
        assert dut.do_get_property("frame_clock") is None
        assert dut.do_get_property("parent") is None
        assert dut.do_get_property("path") is None
        assert dut.do_get_property("scale") == 1
        assert dut.do_get_property("screen") is None
        assert dut.do_get_property("sides") is None
        assert dut.do_get_property("state") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _parent = Gtk.StyleContext()
        _path = Gtk.WidgetPath()
        _path.append_for_widget(GTK3Window())
        _screen = Gdk.Screen().get_default()
        _sides = Gtk.JunctionSides.RIGHT
        _state = Gtk.StateFlags.NORMAL

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                frame_clock=None,
                parent=_parent,
                path=_path,
                scale=2,
                screen=_screen,
                sides=_sides,
                state=_state,
            )
        )

        assert dut.do_get_property("frame_clock") is None
        assert dut.get_frame_clock() is None
        assert dut.do_get_property("parent") == _parent
        assert dut.get_parent() == _parent
        assert dut.do_get_property("path") == _path
        assert dut.get_path().to_string() == _path.to_string()
        assert dut.do_get_property("scale") == 2
        assert dut.get_scale() == 2
        assert dut.do_get_property("screen") == _screen
        assert dut.get_screen() == _screen
        assert dut.do_get_property("sides") == _sides
        assert dut.get_junction_sides() == _sides
        assert dut.do_get_property("state") == _state
        assert dut.get_state() == _state

    @pytest.mark.unit
    def test_do_add_style_provider_global(self):
        """Should add a global style provider."""
        _provider = GTK3CssProvider()
        _screen = Gdk.Screen().get_default()

        dut = self.make_dut()
        dut.do_add_style_provider(_provider, 1, screen=_screen)

        assert dut.dic_providers[_provider] == 1

    @pytest.mark.unit
    def test_do_add_style_provider(self):
        """Should add a local style provider."""
        _provider = GTK3CssProvider()

        dut = self.make_dut()
        dut.do_add_style_provider(_provider, 10)

        assert dut.dic_providers[_provider] == 10

    @pytest.mark.unit
    def test_do_get_stateful_property(self):
        """Should return the value of the requested stateful property."""
        dut = self.make_dut()

        assert isinstance(
            dut.do_get_stateful_property("border", Gtk.StateFlags.NORMAL), Gtk.Border
        )
        assert isinstance(
            dut.do_get_stateful_property("color", Gtk.StateFlags.NORMAL), Gdk.RGBA
        )
        assert isinstance(
            dut.do_get_stateful_property("margin", Gtk.StateFlags.NORMAL), Gtk.Border
        )
        assert isinstance(
            dut.do_get_stateful_property("padding", Gtk.StateFlags.NORMAL), Gtk.Border
        )

    @pytest.mark.unit
    def test_do_remove_style_provider(self):
        """Should remove the requested GTK3CssProvider."""
        _global_provider = GTK3CssProvider()
        _local_provider = GTK3CssProvider()
        _screen = Gdk.Screen().get_default()

        dut = self.make_dut()
        dut.do_add_style_provider(_global_provider, 1, screen=_screen)
        dut.do_add_style_provider(_local_provider, 10)

        assert dut.dic_providers[_global_provider] == 1
        assert dut.dic_providers[_local_provider] == 10

        dut.do_remove_style_provider(_global_provider)

        assert dut.dic_providers[_local_provider] == 10
        with pytest.raises(KeyError):
            print(dut.dic_providers[_global_provider])
