"""Test module for the GTK3Clipboard class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.clipboard import GTK3Clipboard
from pytkwrap.gtk3.mixins import (
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
    set_widget_sensitivity,
)
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_CLIPBOARD_HANDLER_IDS,
    EXPECTED_CLIPBOARD_METHODS,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Clipboard(BaseGTK3GObjectTests):
    """Test class for the GTK3Clipboard class."""

    widget_class = GTK3Clipboard
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_CLIPBOARD_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_CLIPBOARD_METHODS
