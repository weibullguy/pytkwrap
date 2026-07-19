"""Test module for the GTK3PrintSettings class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
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
