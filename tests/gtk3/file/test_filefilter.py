"""Test module for the GTK3FileFilter class.

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
from pytkwrap.gtk3.file import GTK3FileFilter
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.file.constants import EXPECTED_FILEFILTER_METHODS


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FileFilter(BaseGTK3GObjectTests):
    """Test class for the GTK3FileFilter class."""

    widget_class = GTK3FileFilter
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_FILEFILTER_METHODS

    def custom_filter(self, _filter, _data):
        """Custom filter function."""
        _filename = Path(_data).name

        if _filename == "pytkwrap.txt":
            return True
        return False

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_mime_type_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using a mime type."""
        _filter = Gtk.FileFilterInfo()
        _filter.contains = Gtk.FileFilterFlags.MIME_TYPE
        _filter.mime_type = "text/plain"

        dut = self.make_dut()
        dut.do_set_filter(mime_types=["text/plain"])

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_pattern_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using a glob pattern."""
        _filter = Gtk.FileFilterInfo()
        _filter.contains = Gtk.FileFilterFlags.DISPLAY_NAME
        _filter.display_name = text_file

        dut = self.make_dut()
        dut.do_set_filter(patterns=["*.txt"])

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_custom_filter(self, text_file):
        """Should set the filter of the GTK3FileFilter using a custom filter."""
        _filter = Gtk.FileFilterInfo()
        _filter.contains = Gtk.FileFilterFlags.FILENAME
        _filter.filename = text_file

        dut = self.make_dut()
        dut.do_set_filter(
            text_file,
            needed=Gtk.FileFilterFlags.FILENAME,
            func=self.custom_filter,
        )

        assert dut.filter(_filter)

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_set_filter_prefer_mime_type(self, text_file):
        """Should set the filter of the GTK3FileFilter using a custom filter."""
        _filter = Gtk.FileFilterInfo()
        _filter.contains = Gtk.FileFilterFlags.MIME_TYPE
        _filter.mime_type = "text/plain"

        dut = self.make_dut()
        dut.do_set_filter(
            text_file,
            mime_types=["text/plain"],
            patterns=["*.txt"],
            needed=Gtk.FileFilterFlags.FILENAME,
            func=self.custom_filter,
        )

        assert dut.filter(_filter)
