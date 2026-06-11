"""Test module for the GTK3Alignment class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.alignment import GTK3Alignment

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


class TestGTK3Alignment(BaseGTK3GObjectTests):
    """Test class for the GTK3Alignment class."""

    widget_class = GTK3Alignment
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS
    expected_properties = EXPECTED_WIDGET_PROPERTIES
