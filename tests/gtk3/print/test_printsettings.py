"""Test module for the GTK3PrintSettings class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GLib, Gtk
from pytkwrap.gtk3.print import GTK3PrintSettings
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.print.constants import EXPECTED_PRINTSETTINGS_METHODS


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3PrintSettings(BaseGTK3GObjectTests):
    """Test class for the GTK3PrintSettings class."""

    widget_class = GTK3PrintSettings
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_PRINTSETTINGS_METHODS

    def make_dut(
        self,
        file_name: str | None = None,
        group_name: str | None = None,
    ) -> GTK3PrintSettings:
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
        dut = self.make_dut(file_name="tests/data/test_printsettings.ini")

        assert isinstance(dut, GTK3PrintSettings)
        assert isinstance(dut, Gtk.PrintSettings)
        assert dut.file_name == "tests/data/test_printsettings.ini"
        assert dut.get_collate()
        assert dut.get_dither() == "full"
        assert dut.get_duplex() == Gtk.PrintDuplex.SIMPLEX
        assert dut.get_finishings() == "finishings"
        assert dut.get_media_type() == "stationery"
        assert dut.get_n_copies() == 2
        assert dut.get_number_up() == 4
        assert dut.get_number_up_layout() == Gtk.NumberUpLayout.LRTB
        assert dut.get_orientation() == Gtk.PageOrientation.LANDSCAPE
        assert dut.get_output_bin() == "auto"
        assert isinstance(dut.get_page_ranges()[0], Gtk.PageRange)
        assert isinstance(dut.get_page_ranges()[1], Gtk.PageRange)
        assert dut.get_page_set() == Gtk.PageSet.EVEN
        assert dut.get_paper_height(Gtk.Unit.INCH) == pytest.approx(11.0)
        assert isinstance(dut.get_paper_size(), Gtk.PaperSize)
        assert dut.get_paper_width(Gtk.Unit.INCH) == pytest.approx(8.5)
        assert dut.get_print_pages() == Gtk.PrintPages.CURRENT
        assert dut.get_printer() == "my_printer"
        assert dut.get_printer_lpi() == 5
        assert dut.get_resolution() == 600
        assert dut.get_resolution_x() == 600
        assert dut.get_resolution_y() == 600
        assert not dut.get_reverse()
        assert dut.get_scale() == 1.0
        assert dut.get_use_color()

    @pytest.mark.unit
    def test_init_from_key_file(self):
        """Test that GTK3PageSetup can be initialized from a file."""
        dut = self.make_dut(
            file_name="tests/data/test_printsettings.ini", group_name="Print Settings"
        )

        assert isinstance(dut, GTK3PrintSettings)
        assert isinstance(dut, Gtk.PrintSettings)
        assert dut.file_name == "tests/data/test_printsettings.ini"
        assert dut.get_collate()
        assert dut.get_dither() == "full"
        assert dut.get_duplex() == Gtk.PrintDuplex.SIMPLEX
        assert dut.get_finishings() == "finishings"
        assert dut.get_media_type() == "stationery"
        assert dut.get_n_copies() == 2
        assert dut.get_number_up() == 4
        assert dut.get_number_up_layout() == Gtk.NumberUpLayout.LRTB
        assert dut.get_orientation() == Gtk.PageOrientation.LANDSCAPE
        assert dut.get_output_bin() == "auto"
        assert isinstance(dut.get_page_ranges()[0], Gtk.PageRange)
        assert isinstance(dut.get_page_ranges()[1], Gtk.PageRange)
        assert dut.get_page_set() == Gtk.PageSet.EVEN
        assert dut.get_paper_height(Gtk.Unit.INCH) == pytest.approx(11.0)
        assert isinstance(dut.get_paper_size(), Gtk.PaperSize)
        assert dut.get_paper_width(Gtk.Unit.INCH) == pytest.approx(8.5)
        assert dut.get_print_pages() == Gtk.PrintPages.CURRENT
        assert dut.get_printer() == "my_printer"
        assert dut.get_printer_lpi() == 5
        assert dut.get_resolution() == 600
        assert dut.get_resolution_x() == 600
        assert dut.get_resolution_y() == 600
        assert not dut.get_reverse()
        assert dut.get_scale() == 1.0
        assert dut.get_use_color()

    @pytest.mark.unit
    def test_do_save_page_setup(self):
        """Test that the save page setup callback works correctly."""
        dut = self.make_dut(file_name="tests/data/test_printsettings.ini")
        dut.set_collate(False)
        dut.set_n_copies(10)
        dut.file_name = "/tmp/test_printsettings_saved.ini"
        dut.do_save_page_setup()

        with open("/tmp/test_printsettings_saved.ini", "r") as f:
            contents = f.read()
            assert "[Print Settings]" in contents
            assert "page-set=even" in contents
            assert "number-up=4" in contents
            assert "collate=false" in contents
            assert "n-copies=10" in contents
            assert "printer=my_printer" in contents
