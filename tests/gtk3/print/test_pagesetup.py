"""Test module for the GTK3PageSetup class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GLib, Gtk
from pytkwrap.gtk3.print import GTK3PageSetup
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.print.constants import EXPECTED_PAGESETUP_METHODS


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3PageSetup(BaseGTK3GObjectTests):
    """Test class for the GTK3PageSetup class."""

    widget_class = GTK3PageSetup
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_PAGESETUP_METHODS

    def make_dut(
        self,
        file_name: str | None = None,
        group_name: str | None = None,
    ) -> GTK3PageSetup:
        """Make a device under test (DUT) instance of GTK3PageSetup.

        Parameters
        ----------
        file_name : str | None, optional
            The name of the file to load the page setup from. If None, a new
            page setup is created. Defaults to None.
        group_name : str | None, optional
            The name of the group in the file to load the page setup from. If
            None, the default group is used. Defaults to None.

        Returns
        -------
        GTK3PageSetup
            An instance of GTK3PageSetup.
        """
        return self.widget_class(file_name=file_name, group_name=group_name)

    @pytest.mark.unit
    def test_init_from_file(self):
        """Test that GTK3PageSetup can be initialized from a file."""
        dut = self.make_dut(file_name="tests/data/test_pagesetup.ini")
        _paper_size = dut.get_paper_size()

        assert isinstance(dut, GTK3PageSetup)
        assert isinstance(dut, Gtk.PageSetup)
        assert dut.file_name == "tests/data/test_pagesetup.ini"
        assert dut.get_bottom_margin(Gtk.Unit.MM) == 14.224
        assert dut.get_left_margin(Gtk.Unit.MM) == pytest.approx(6.35)
        assert dut.get_right_margin(Gtk.Unit.MM) == pytest.approx(6.35)
        assert dut.get_top_margin(Gtk.Unit.MM) == pytest.approx(6.35)
        assert dut.get_orientation() == Gtk.PageOrientation.PORTRAIT
        assert dut.get_page_height(Gtk.Unit.MM) == pytest.approx(258.8259939)
        assert dut.get_page_width(Gtk.Unit.MM) == pytest.approx(203.1999999)
        assert isinstance(_paper_size, Gtk.PaperSize)
        assert _paper_size.get_display_name() == "US Letter"
        assert _paper_size.get_name() == "na_letter"
        assert _paper_size.get_ppd_name() == "Letter"

    @pytest.mark.unit
    def test_init_from_key_file(self):
        """Test that GTK3PageSetup can be initialized from a file."""
        dut = self.make_dut(
            file_name="tests/data/test_pagesetup.ini", group_name="Page Setup"
        )
        _paper_size = dut.get_paper_size()

        assert isinstance(dut, GTK3PageSetup)
        assert isinstance(dut, Gtk.PageSetup)
        assert dut.file_name == "tests/data/test_pagesetup.ini"
        assert isinstance(dut.key_file, GLib.KeyFile)
        assert dut.get_bottom_margin(Gtk.Unit.MM) == 14.224
        assert dut.get_left_margin(Gtk.Unit.MM) == pytest.approx(6.35)
        assert dut.get_right_margin(Gtk.Unit.MM) == pytest.approx(6.35)
        assert dut.get_top_margin(Gtk.Unit.MM) == pytest.approx(6.35)
        assert dut.get_orientation() == Gtk.PageOrientation.PORTRAIT
        assert dut.get_page_height(Gtk.Unit.MM) == pytest.approx(258.8259939)
        assert dut.get_page_width(Gtk.Unit.MM) == pytest.approx(203.1999999)
        assert isinstance(_paper_size, Gtk.PaperSize)
        assert _paper_size.get_display_name() == "US Letter"
        assert _paper_size.get_name() == "na_letter"
        assert _paper_size.get_ppd_name() == "Letter"

    @pytest.mark.unit
    def test_do_save_page_setup(self):
        """Test that the save page setup callback works correctly."""
        dut = self.make_dut(file_name="tests/data/test_pagesetup.ini")
        dut.set_bottom_margin(15, Gtk.Unit.MM)
        dut.set_paper_size(Gtk.PaperSize.new("iso_a4_210x297mm"))
        dut.file_name = "/tmp/test_pagesetup_saved.ini"
        dut.do_save_page_setup()

        with open("/tmp/test_pagesetup_saved.ini", "r") as f:
            contents = f.read()
            assert "[Page Setup]" in contents
            assert "MarginBottom=15" in contents
            assert "PPDName=A4" in contents
            assert "DisplayName=A4" in contents
            assert "Width=210" in contents
            assert "Height=297" in contents
