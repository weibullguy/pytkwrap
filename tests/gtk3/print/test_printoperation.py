"""Test module for the GTK3PrintOperation class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.print import GTK3PrintOperation
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.print.constants import (
    EXPECTED_PRINTOPERATION_HANDLER_IDS,
    EXPECTED_PRINTOPERATION_METHODS,
    EXPECTED_PRINTOPERATION_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3PrintOperation(BaseGTK3GObjectTests):
    """Test class for the GTK3PrintOperation class."""

    widget_class = GTK3PrintOperation
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_PRINTOPERATION_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_PRINTOPERATION_METHODS
    expected_properties = EXPECTED_PRINTOPERATION_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("allow_async")
        assert dut.do_get_property("current_page") == -1
        assert dut.do_get_property("custom_tab_label") is None
        assert dut.do_get_property("default_page_setup") is None
        assert not dut.do_get_property("embed_page_setup")
        assert dut.do_get_property("export_filename") is None
        assert not dut.do_get_property("has_selection")
        assert dut.do_get_property("job_name") == ""
        assert dut.do_get_property("n_pages") == -1
        assert dut.do_get_property("print_settings") is None
        assert not dut.do_get_property("show_progress")
        assert not dut.do_get_property("support_selection")
        assert not dut.do_get_property("track_print_status")
        assert dut.do_get_property("unit") == Gtk.Unit.NONE
        assert not dut.do_get_property("use_full_page")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _page_setup = Gtk.PageSetup.new()
        _print_settings = Gtk.PrintSettings.new()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                allow_async=True,
                current_page=2,
                custom_tab_label="Custom Tab Label",
                default_page_setup=_page_setup,
                embed_page_setup=True,
                export_filename="Export Filename",
                has_selection=True,
                job_name="Test Job Name",
                n_pages=5,
                print_settings=_print_settings,
                show_progress=True,
                support_selection=True,
                track_print_status=True,
                unit=Gtk.Unit.POINTS,
                use_full_page=True,
            )
        )

        assert dut.get_property("allow_async")
        assert dut.get_property("current_page") == 2
        assert dut.get_property("custom_tab_label") == "Custom Tab Label"
        assert dut.get_property("default_page_setup") == _page_setup
        assert dut.get_default_page_setup() == _page_setup
        assert dut.get_property("embed_page_setup")
        assert dut.get_embed_page_setup()
        assert dut.get_property("export_filename") == "Export Filename"
        assert dut.get_property("has_selection")
        assert dut.get_has_selection()
        assert dut.get_property("job_name") == "Test Job Name"
        assert dut.get_property("n_pages") == 5
        assert dut.get_property("print_settings") == _print_settings
        assert dut.get_print_settings() == _print_settings
        assert dut.get_property("show_progress")
        assert dut.get_property("support_selection")
        assert dut.get_support_selection()
        assert dut.get_property("track_print_status")
        assert dut.get_property("unit") == Gtk.Unit.POINTS
        assert dut.get_property("use_full_page")
