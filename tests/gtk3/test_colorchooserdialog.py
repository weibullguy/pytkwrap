"""Test module for the GTK3ColorChooserDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, Gtk
from pytkwrap.gtk3.color import GTK3ColorChooserDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_COLORCHOOSERDIALOG_PROPERTIES,
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


@pytest.mark.skip(
    reason=(
        "GTK3ColorChooserDialog crashes at the C level when run as part of the full "
        "test suite due to GIO volume monitor initialization conflicts. "
        "Passes in isolation. Requires manual testing."
    )
)
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ColorChooserDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3ColorChooserDialog class."""

    widget_class = GTK3ColorChooserDialog
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
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
        | EXPECTED_DIALOG_PROPERTIES
        | EXPECTED_COLORCHOOSERDIALOG_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("show_editor")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                show_editor=True,
            )
        )

        assert dut.get_property("show_editor")
