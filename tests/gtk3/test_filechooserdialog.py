"""Test module for the GTK3FileChooserDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gtk
from pytkwrap.gtk3.file import GTK3FileChooserDialog

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
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


@pytest.mark.skip(
    reason=(
        "GTK3FileChooserDialog crashes at the C level when run as part of the full "
        "test suite due to GIO volume monitor initialization conflicts. Passes in "
        "isolation. Requires manual testing."
    )
)
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FileChooserDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3FileChooserDialog class."""

    widget_class = GTK3FileChooserDialog
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
    )
