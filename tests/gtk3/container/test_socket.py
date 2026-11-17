"""Test module for the GTK3Socket class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk
from pytkwrap.gtk3.container import GTK3Socket
from pytkwrap.gtk3.window import GTK3Plug, GTK3Window
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.container.constants import (
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_SOCKET_HANDLER_IDS,
    EXPECTED_SOCKET_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Socket(BaseGTK3GObjectTests):
    """Test class for the GTK3Socket class."""

    widget_class = GTK3Socket
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_SOCKET_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_SOCKET_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_CONTAINER_PROPERTIES

    @pytest.mark.unit
    def test_id(self):
        """Should return the window ID of the GTK3Socket."""
        _window = GTK3Window()
        _plug = GTK3Plug()

        dut = self.make_dut()
        _window.add(dut)
        dut.add_id(_plug.get_id())

        assert isinstance(dut.id, int)

    @pytest.mark.unit
    def test_plug_window(self):
        """Should return the Gdk.Window associated with the GTK3Plug."""
        _window = GTK3Window()
        _plug = GTK3Plug()

        dut = self.make_dut()
        _window.add(dut)
        dut.add_id(_plug.get_id())

        assert isinstance(dut.plug_window, Gdk.Window)
