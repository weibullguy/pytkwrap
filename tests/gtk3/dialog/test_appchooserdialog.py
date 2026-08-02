"""Test module for the GTK3AppChooserDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, Gtk
from pytkwrap.gtk3.dialog import GTK3AppChooserDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.container.constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.dialog.constants import (
    EXPECTED_APPCHOOSERDIALOG_METHODS,
    EXPECTED_APPCHOOSERDIALOG_PROPERTIES,
    EXPECTED_DIALOG_HANDLER_IDS,
    EXPECTED_DIALOG_METHODS,
    EXPECTED_DIALOG_PROPERTIES,
)
from tests.gtk3.window.constants import (
    EXPECTED_WINDOW_HANDLER_IDS,
    EXPECTED_WINDOW_METHODS,
    EXPECTED_WINDOW_PROPERTIES,
)


@pytest.mark.filter_warning("G_IS_OBJECT")
@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3AppChooserDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3AppChooserDialog class."""

    widget_class = GTK3AppChooserDialog
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_WINDOW_HANDLER_IDS
        | EXPECTED_DIALOG_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_WINDOW_METHODS
        + EXPECTED_DIALOG_METHODS
        + EXPECTED_APPCHOOSERDIALOG_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
        | EXPECTED_DIALOG_PROPERTIES
        | EXPECTED_APPCHOOSERDIALOG_PROPERTIES
    )

    def make_dut(self, parent=None, flags=0, gfile=None):
        return GTK3AppChooserDialog(parent=parent, flags=flags, gfile=gfile)

    @pytest.mark.unit
    @pytest.mark.filterwarnings("ignore:g_file_info_get_content_type")
    @pytest.mark.filterwarnings("ignore:g_object_unref:Warning")
    def test_init_with_gfile(self, filter_stderr):
        _gfile = Gio.File.new_for_path("../data/pytkwrap.png")
        dut = self.make_dut(gfile=_gfile)

        assert dut.do_get_property("gfile") == _gfile

    @pytest.mark.unit
    @pytest.mark.filterwarnings(
        "ignore:Gtk.Window.set_opacity is deprecated:DeprecationWarning"
    )
    def test_do_set_properties_default(self, filter_stderr):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("gfile") is None
        assert dut.do_get_property("heading") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                gfile=None,
                heading="Test Heading",
            )
        )

        assert dut.get_property("gfile") is None
        assert dut.get_property("heading") == "Test Heading"
        assert dut.get_heading() == "Test Heading"
