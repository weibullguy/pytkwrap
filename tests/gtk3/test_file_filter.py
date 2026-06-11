"""Test module for the GTK3FileFilter class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.file import GTK3FileFilter

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_FILE_FILTER_METHODS,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


class TestGTK3FileFilter(BaseGTK3GObjectTests):
    """Test class for the GTK3FileFilter class."""

    widget_class = GTK3FileFilter
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_FILE_FILTER_METHODS
