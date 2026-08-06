"""Test module for the GTK3SearchEntry class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from datetime import datetime

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk, Pango
from pytkwrap.gtk3.io import GTK3SearchEntry
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.utilities import FontDescription
from tests.gtk3.conftest import BaseGTK3DataWidgetTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.io.constants import (
    EXPECTED_ENTRY_ATTRIBUTES,
    EXPECTED_ENTRY_HANDLER_IDS,
    EXPECTED_ENTRY_METHODS,
    EXPECTED_ENTRY_PROPERTIES,
    EXPECTED_SEARCHENTRY_HANDLER_IDS,
    EXPECTED_SEARCHENTRY_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3SearchEntry(BaseGTK3DataWidgetTests):
    """Test class for the GTK3SearchEntry class."""

    widget_class = GTK3SearchEntry
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_ENTRY_ATTRIBUTES
    )
    expected_default_height = 25
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_ENTRY_HANDLER_IDS
        | EXPECTED_SEARCHENTRY_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_ENTRY_METHODS
        + EXPECTED_SEARCHENTRY_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_ENTRY_PROPERTIES
