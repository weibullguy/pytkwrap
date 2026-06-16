"""Test module for the GTK3AboutDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gtk
from pytkwrap.gtk3.dialog import GTK3AboutDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_ABOUTDIALOG_HANDLER_IDS,
    EXPECTED_ABOUTDIALOG_METHODS,
    EXPECTED_ABOUTDIALOG_PROPERTIES,
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_DIALOG_HANDLER_IDS,
    EXPECTED_DIALOG_METHODS,
    EXPECTED_DIALOG_PROPERTIES,
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
class TestGTK3AboutDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3AboutDialog class."""

    widget_class = GTK3AboutDialog
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_WINDOW_HANDLER_IDS
        | EXPECTED_DIALOG_HANDLER_IDS
        | EXPECTED_ABOUTDIALOG_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_WINDOW_METHODS
        + EXPECTED_DIALOG_METHODS
        + EXPECTED_ABOUTDIALOG_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
        | EXPECTED_DIALOG_PROPERTIES
        | EXPECTED_ABOUTDIALOG_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("artists") == []
        assert dut.do_get_property("authors") == []
        assert dut.do_get_property("comments") is None
        assert dut.do_get_property("copyright") is None
        assert dut.do_get_property("documenters") == []
        assert dut.do_get_property("license") is None
        assert dut.do_get_property("license_type") == Gtk.License.UNKNOWN
        assert dut.do_get_property("logo") is None
        assert dut.do_get_property("logo_icon_name") == "image-missing"
        assert dut.do_get_property("program_name") is None
        assert dut.do_get_property("translator_credits") is None
        assert dut.do_get_property("version") is None
        assert dut.do_get_property("website") is None
        assert dut.do_get_property("website_label") is None
        assert not dut.do_get_property("wrap_license")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetPRoperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                artists=["Doyle Rowland"],
                authors=["Doyle Rowland"],
                comments="These are some comments for the AboutDialog.",
                copyright="2026, Doyle 'weibullguy' Rowland",
                documenters=["Doyle Rowland"],
                license="",
                license_type=Gtk.License.BSD_3,
                logo=None,
                logo_icon_name="pytkwrap logo",
                program_name="pytkwrap",
                translator_credits="Doyle Rowland",
                version="0.1.0",
                website="www.no_website.org",
                website_label="Go to the website.",
                wrap_license=True,
            )
        )

        assert dut.do_get_property("artists") == ["Doyle Rowland"]
        assert dut.do_get_property("authors") == ["Doyle Rowland"]
        assert dut.do_get_property("comments") == (
            "These are some comments for the AboutDialog."
        )
        assert dut.do_get_property("copyright") == "2026, Doyle 'weibullguy' Rowland"
        assert dut.do_get_property("documenters") == ["Doyle Rowland"]
        assert dut.do_get_property("license") == ""
        assert dut.do_get_property("license_type") == Gtk.License.BSD_3
        assert dut.do_get_property("logo") is None
        assert dut.do_get_property("logo_icon_name") == "pytkwrap logo"
        assert dut.do_get_property("program_name") == "pytkwrap"
        assert dut.do_get_property("translator_credits") == "Doyle Rowland"
        assert dut.do_get_property("version") == "0.1.0"
        assert dut.do_get_property("website") == "www.no_website.org"
        assert dut.do_get_property("website_label") == "Go to the website."
        assert dut.do_get_property("wrap_license")
