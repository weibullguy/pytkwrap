"""Test module for the GTK3Container class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Container

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests
from .test_constants import (
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.order(3)
class TestGTK3Container(BaseGTK3WidgetTests):
    """Test class for the GTK3Container class."""

    widget_class = GTK3Container
    expected_attributes = [
        "add",
        "check_resize",
        "child_get",
        "child_get_property",
        "child_notify",
        "child_notify_by_pspec",
        "child_set",
        "child_set_property",
        "child_type",
        "forall",
        "foreach",
        "get_border_width",
        "get_children",
        # "get_focus_chain", # deprecated
        "get_focus_child",
        "get_focus_hadjustment",
        "get_focus_vadjustment",
        "get_path_for_child",
        # "get_resize_mode", # deprecated
        "propagate_draw",
        "remove",
        # "resize_children", # deprecated
        "set_border_width",
        # "set_focus_chain", # deprecated
        "set_focus_child",
        "set_focus_hadjustment",
        "set_focus_vadjustment",
        # "set_reallocate_redraws", # deprecated
        # "set_resize_mode", # deprecated
        # "unset_focus_chain", # deprecated
    ]
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = EXPECTED_WIDGET_HANDLER_IDS | EXPECTED_CONTAINER_HANDLER_IDS
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_CONTAINER_PROPERTIES
