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


@pytest.mark.order(2)
class TestGTK3GObjectMixin(BaseGTK3GObjectTests):
    """Test class for the GTK3GObjectMixin class."""

    widget_class = GTK3GObjectMixin
    expected_attributes = [
        "bind_property",
        "connect",
        "connect_after",
        "disconnect",
        "emit",
        "force_floating",
        "get_data",
        "get_property",
        "get_qdata",
        "getv",
        "handler_block",
        "handler_unblock",
        "is_floating",
        "notify",
        "notify_by_pspec",
        "ref",
        "ref_sink",
        "run_dispose",
        "set_data",
        "set_property",
        "steal_data",
        "steal_qdata",
        "thaw_notify",
        "unref",
        "watch_closure",
    ]
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1
    expected_handler_id = {"notify": -1}
    expected_properties = {}

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-GTK3-X-005")
    def test_do_set_callbacks_after(self):
        """Should set callback function for a GTK3GObjectMixin signal."""
        dut = self.make_dut()
        dut.do_set_callbacks("notify", self.mock_callback, True)

        assert dut.dic_handler_id["notify"] != -1
