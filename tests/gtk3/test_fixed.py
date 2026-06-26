"""Test module for the GTK3Fixed class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Fixed
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests
from .test_constants import (
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_FIXED_METHODS,
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Fixed(BaseGTK3GObjectTests):
    """Test class for the GTK3Fixed class."""

    widget_class = GTK3Fixed
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_FIXED_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_CONTAINER_PROPERTIES
