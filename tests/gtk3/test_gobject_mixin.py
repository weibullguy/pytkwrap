"""Test module for the GTK3GObjectMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import EXPECTED_GOBJECT_HANDLER_IDS, EXPECTED_GOBJECT_METHODS


@pytest.mark.order(2)
class TestGTK3GObjectMixin(BaseGTK3GObjectTests):
    """Test class for the GTK3GObjectMixin class."""

    widget_class = GTK3GObjectMixin
    expected_methods = EXPECTED_GOBJECT_METHODS
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_properties = {}
