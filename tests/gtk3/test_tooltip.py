"""Test module for the GTK3Tooltip class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import os

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Tooltip, do_construct_tooltip

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, Gtk
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_TOOLTIP_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Tooltip(BaseGTK3GObjectTests):
    """Test class for the GTK3Tooltip class."""

    widget_class = GTK3Tooltip
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_TOOLTIP_METHODS

    @pytest.mark.unit
    def test_do_set_icon_pixbuf(self):
        """Test the do_set_icon method with a GdkPixbuf.Pixbuf."""
        cwd = os.getcwd()

        _pixbuf = GdkPixbuf.Pixbuf.new_from_file(f"{cwd}/tests/data/pytkwrap.png")

        dut = self.widget_class()

        assert (
            dut.do_set_icon(
                icon=_pixbuf,
                gicon=None,
                icon_name=None,
                icon_size=Gtk.IconSize.BUTTON,
            )
            is None
        )

    @pytest.mark.unit
    def test_do_set_icon_gicon(self):
        """Test the do_set_icon method with a Gio.Icon."""
        _gicon = Gio.ThemedIcon.new("folder")

        dut = self.widget_class()

        assert (
            dut.do_set_icon(
                icon=None,
                gicon=_gicon,
                icon_name=None,
                icon_size=Gtk.IconSize.BUTTON,
            )
            is None
        )

    @pytest.mark.unit
    def test_do_set_icon_icon_name(self):
        """Test the do_set_icon method with an icon name."""
        dut = self.widget_class()

        assert (
            dut.do_set_icon(
                icon=None,
                gicon=None,
                icon_name="folder",
                icon_size=Gtk.IconSize.BUTTON,
            )
            is None
        )

    @pytest.mark.unit
    def test_do_set_tooltip_text(self):
        """Test the do_set_tooltip_text method."""
        dut = self.make_dut()

        assert dut.do_set_tooltip("Test tooltip", markup=False) is None

    @pytest.mark.unit
    def test_do_set_tooltip_markup(self):
        """Test the do_set_tooltip_markup method."""
        dut = self.make_dut()

        assert dut.do_set_tooltip("<b>Test tooltip</b>", markup=True) is None

    @pytest.mark.unit
    def test_do_construct_tooltip(self):
        """Test the do_construct_tooltip method."""
        _tooltip = do_construct_tooltip(
            tooltip="Test tooltip",
            markup=False,
            icon=None,
            gicon=None,
            icon_name=None,
            icon_size=Gtk.IconSize.BUTTON,
        )

        assert isinstance(_tooltip, GTK3Tooltip)
