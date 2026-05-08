"""Test module for the GTK3CellRenderer class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.cellrenderer import GTK3CellRenderer

# pytkwrap Local Imports
from .conftest import BaseGTK3GObjectTests


@pytest.mark.order(3)
class TestGTK3CellRenderer(BaseGTK3GObjectTests):
    """Test class for the GTK3CellRenderer class."""

    widget_class = GTK3CellRenderer
    expected_attributes = [
        "activate",
        "get_aligned_area",
        "get_alignment",
        "get_fixed_size",
        "get_padding",
        "get_preferred_height",
        "get_preferred_height_for_width",
        "get_preferred_size",
        "get_preferred_width",
        "get_preferred_width_for_height",
        "get_request_mode",
        "get_sensitive",
        # "get_size", # deprecated
        "get_state",
        "get_visible",
        "is_activatable",
        "render",
        "set_alignment",
        "set_fixed_size",
        "set_padding",
        "set_sensitive",
        "set_visible",
        "start_editing",
        "stop_editing",
    ]
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1
    expected_handler_id = {
        "editing-canceled": -1,
        "editing-started": -1,
        "notify": -1,
    }
    expected_properties = {
        "cell_background": None,
        "cell_background_rgba": None,
        "cell_background_set": False,
        "height": -1,
        "is_expanded": False,
        "is_expander": False,
        "mode": Gtk.CellRendererMode.INERT,
        "sensitive": True,
        "visible": True,
        "width": -1,
        "xalign": 0.0,
        "xpad": 0,
        "yalign": 0.0,
        "ypad": 0,
    }
