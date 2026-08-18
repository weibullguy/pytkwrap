"""Test module for the GTK3IconTheme class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import os

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.icon import GTK3IconTheme
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.icon.constants import (
    EXPECTED_ICONTHEME_HANDLER_IDS,
    EXPECTED_ICONTHEME_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3IconTheme(BaseGTK3GObjectTests):
    """Test class for the GTK3IconTheme class."""

    widget_class = GTK3IconTheme
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_ICONTHEME_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_ICONTHEME_METHODS

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    def test_do_get_icon_name(self, image_file):
        """Should return a Gtk.IconInfo for the icon name."""
        _icon_name = os.path.basename(image_file).split(".")[0]
        _icon_dir = os.path.dirname(image_file)

        dut = self.make_dut()
        dut.prepend_search_path(_icon_dir)

        icon_name = dut.do_get_icon([_icon_name], 12, 16)

        assert isinstance(icon_name, Gtk.IconInfo)
        assert icon_name.get_filename() == image_file

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    def test_do_get_icon_name_at_scale(self, image_file):
        """Should return a Gtk.IconInfo for the icon name."""
        _icon_name = os.path.basename(image_file).split(".")[0]
        _icon_dir = os.path.dirname(image_file)

        dut = self.make_dut()
        dut.prepend_search_path(_icon_dir)

        icon_name = dut.do_get_icon([_icon_name], 12, 16, 4)

        assert isinstance(icon_name, Gtk.IconInfo)
        assert icon_name.get_filename() == image_file
        assert icon_name.get_base_scale() == 1
        assert icon_name.get_base_size() == 12

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    def test_do_get_icon_name_from_list(self, image_file):
        """Should return a Gtk.IconInfo for the icon name."""
        _icon_name = os.path.basename(image_file).split(".")[0]
        _icon_dir = os.path.dirname(image_file)

        dut = self.make_dut()
        dut.prepend_search_path(_icon_dir)

        icon_name = dut.do_get_icon(
            ["zoom-zoom", "zoom-zoom-zoom", _icon_name, None], 12, 16
        )

        assert isinstance(icon_name, Gtk.IconInfo)
        assert icon_name.get_filename() == image_file

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    def test_do_get_icon_name_at_scale_from_list(self, image_file):
        """Should return a Gtk.IconInfo for the icon name."""
        _icon_name = os.path.basename(image_file).split(".")[0]
        _icon_dir = os.path.dirname(image_file)

        dut = self.make_dut()
        dut.prepend_search_path(_icon_dir)

        icon_name = dut.do_get_icon(
            ["zoom-zoom", "zoom-zoom-zoom", _icon_name, None], 12, 16, 4
        )

        assert isinstance(icon_name, Gtk.IconInfo)
        assert icon_name.get_filename() == image_file

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    def test_do_get_icon_information(self, image_file):
        """Should return a dict of information about the passed Gtk.IconInfo."""
        _icon_name = os.path.basename(image_file).split(".")[0]
        _icon_dir = os.path.dirname(image_file)

        dut = self.make_dut()
        dut.prepend_search_path(_icon_dir)

        icon_name = dut.do_get_icon(
            ["zoom-zoom", "zoom-zoom-zoom", _icon_name, None], 12, 16, 4
        )

        _icon_info = dut.do_get_icon_info(icon_name)

        assert isinstance(_icon_info, dict)
        assert _icon_info["base_scale"] == 1
        assert _icon_info["base_size"] == 12
        assert _icon_info["filename"] == image_file
        assert not _icon_info["symbolic"]
