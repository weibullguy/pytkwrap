"""Test module for the GTK3Tooltip class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Tooltip

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_TOOLTIP_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Tooltip(BaseGTK3GObjectTests):
    """Test class for the GTK3Tooltip class."""

    widget_class = GTK3Tooltip
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_TOOLTIP_METHODS
