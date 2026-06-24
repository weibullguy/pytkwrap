"""Test module for the GTK3ShortcutsShortcut class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.shortcut import GTK3ShortcutsShortcut

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BOX_METHODS,
    EXPECTED_BOX_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_SHORTCUTSSHORTCUT_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ShortcutsShortcut(BaseGTK3GObjectTests):
    """Test class for the GTK3ShortcutsShortcut class."""

    widget_class = GTK3ShortcutsShortcut
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
        + EXPECTED_BOX_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BOX_PROPERTIES
        | EXPECTED_SHORTCUTSSHORTCUT_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("accel_size_group") is None
        assert dut.do_get_property("accelerator") is None
        assert dut.do_get_property("action_name") is None
        assert dut.do_get_property("direction") == Gtk.TextDirection.NONE
        assert dut.do_get_property("icon") is None
        assert not dut.do_get_property("icon_set")
        assert dut.do_get_property("shortcut_type") == Gtk.ShortcutType.ACCELERATOR
        assert dut.do_get_property("subtitle") == ""
        assert not dut.do_get_property("subtitle_set")
        assert dut.do_get_property("title") == ""
        assert dut.do_get_property("title_size_group") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _asizegroup = Gtk.SizeGroup(mode=Gtk.SizeGroupMode.VERTICAL)
        _tsizegroup = Gtk.SizeGroup(mode=Gtk.SizeGroupMode.HORIZONTAL)
        _icon = Gio.FileIcon.new(Gio.File.new_for_path("../data/pytkwrap.png"))

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                accel_size_group=_asizegroup,
                accelerator="<ctrl>t",
                action_name="Test Action Name",
                direction=Gtk.TextDirection.LTR,
                icon=_icon,
                icon_set=True,
                shortcut_type=Gtk.ShortcutType.GESTURE,
                subtitle="Test Subtitle",
                subtitle_set=True,
                title="Test Title",
                title_size_group=_tsizegroup,
            )
        )

        # These properties are write only.
        assert dut.do_get_property("accel_size_group") == _asizegroup
        assert dut.do_get_property("title_size_group") == _tsizegroup

        assert dut.get_property("accelerator") == "<ctrl>t"
        assert dut.get_property("action_name") == "Test Action Name"
        assert dut.get_property("direction") == Gtk.TextDirection.LTR
        assert dut.get_property("icon") == _icon
        assert dut.get_property("icon_set")
        assert dut.get_property("shortcut_type") == Gtk.ShortcutType.GESTURE
        assert dut.get_property("subtitle") == "Test Subtitle"
        assert dut.get_property("subtitle_set")
        assert dut.get_property("title") == "Test Title"
