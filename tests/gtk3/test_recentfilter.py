"""Test module for the GTK3RecentFilter class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.file import GTK3RecentFilter

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_RECENT_FILTER_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3RecentFilter(BaseGTK3GObjectTests):
    """Test class for the GTK3RecentFilter class."""

    widget_class = GTK3RecentFilter
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_RECENT_FILTER_METHODS
