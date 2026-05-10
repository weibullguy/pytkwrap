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
    expected_handler_id = {
        "add": -1,
        "check-resize": -1,
        "destroy": -1,
        "direction-changed": -1,
        "hide": -1,
        "keynav-failed": -1,
        "map": -1,
        "mnemonic-activate": -1,
        "move-focus": -1,
        "notify": -1,
        "query-tooltip": -1,
        "realize": -1,
        "remove": -1,
        "set-focus-child": -1,
        "show": -1,
        "state-flags-changed": -1,
        "unmap": -1,
        "unrealize": -1,
    }
    expected_properties = {
        "border_width": 0,
        "can_default": False,
        "can_focus": False,
        "focus_on_click": True,
        "halign": Gtk.Align.FILL,
        "has_default": False,
        "has_focus": False,
        "has_tooltip": False,
        "height_request": -1,
        "hexpand": False,
        "hexpand_set": False,
        "is_focus": False,
        "margin": 0,
        "margin_bottom": 0,
        "margin_end": 0,
        "margin_start": 0,
        "margin_top": 0,
        "name": "pytkwrap GTK3 widget",
        "opacity": 1.0,
        "parent": None,
        "receives_default": False,
        "scale_factor": 1,
        "sensitive": True,
        "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
        "tooltip_text": "Missing tooltip, please file an issue to have one added.",
        "valign": Gtk.Align.FILL,
        "vexpand": False,
        "vexpand_set": False,
        "visible": False,
        "width_request": -1,
        "window": None,
    }
