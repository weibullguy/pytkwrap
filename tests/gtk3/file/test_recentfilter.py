"""Test module for the GTK3RecentFilter class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from pathlib import Path

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.file import GTK3RecentFilter
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.file.constants import EXPECTED_RECENTFILTER_METHODS


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3RecentFilter(BaseGTK3GObjectTests):
    """Test class for the GTK3RecentFilter class."""

    widget_class = GTK3RecentFilter
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_RECENTFILTER_METHODS

    @staticmethod
    def custom_filter(_filter, _data):
        """Custom filter function."""
        _filename = Path(_data).name

        if _filename == "pytkwrap.txt":
            return True
        return False

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_mime_type_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using a mime type."""
        _filter = Gtk.RecentFilterInfo()
        _filter.contains = Gtk.RecentFilterFlags.MIME_TYPE
        _filter.mime_type = "text/plain"

        dut = self.make_dut()
        dut.do_set_filter(mime_types=["text/plain"])

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_pattern_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using a glob pattern."""
        _filter = Gtk.RecentFilterInfo()
        _filter.contains = Gtk.RecentFilterFlags.DISPLAY_NAME
        _filter.display_name = text_file

        dut = self.make_dut()
        dut.do_set_filter(patterns=["*.txt"])

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_custom_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using a custom filter."""
        _filter = Gtk.RecentFilterInfo()
        _filter.contains = Gtk.RecentFilterFlags.URI
        _filter.uri = text_file

        dut = self.make_dut()
        dut.do_set_filter(
            text_file,
            needed=Gtk.RecentFilterFlags.URI,
            func=self.custom_filter,
        )

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_filter_prefer_mime_type(self, text_file):
        """Should set the filter of the GTK3FileFilter using a custom filter."""
        _filter = Gtk.RecentFilterInfo()
        _filter.contains = Gtk.RecentFilterFlags.MIME_TYPE
        _filter.mime_type = "text/plain"

        dut = self.make_dut()
        dut.do_set_filter(
            text_file,
            mime_types=["text/plain"],
            patterns=["*.txt"],
            needed=Gtk.RecentFilterFlags.URI,
            func=self.custom_filter,
        )

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_age_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using file age."""
        _filter = Gtk.RecentFilterInfo()
        _filter.contains = Gtk.RecentFilterFlags.AGE | Gtk.RecentFilterFlags.MIME_TYPE
        _filter.age = 10
        _filter.mime_type = "text/plain"

        dut = self.make_dut()
        dut.do_set_filter(
            text_file,
            mime_types=["text/plain"],
            age=10,
        )

        assert dut.filter(_filter)

    @pytest.mark.unit
    def test_do_set_applications_filter(self):
        """Should set the filter of the GTK3FileFilter using file applications."""
        dut = self.make_dut()

        assert dut.get_needed() == 0

        dut.do_set_filter(
            applications=["gedit"],
        )

        assert dut.get_needed() == Gtk.RecentFilterFlags.APPLICATION
