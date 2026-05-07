"""Test module for the GTK3GObjectMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class TestGTK3GObjectMixin:
    """Test class for the GTK3GObjectMixin class."""

    @staticmethod
    def mock_callback(widget) -> None:
        """Callback method for testing."""
        assert isinstance(widget, GTK3GObjectMixin)

    @staticmethod
    def no_signal_error_handler(message):
        """Error handler for do_set_callbacks() errors."""
        assert (
            message
            == "GTK3GObjectMixin.do_set_callbacks(): Unknown signal 'unk_signal'."
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-GTK3-X-001")
    @pytest.mark.requirement("PTW-GTK3-X-002")
    @pytest.mark.requirement("PTW-GTK3-X-003")
    def test_init(self):
        """Should create an instance of the GTK3GObjectMixin class with attributes set
        to default values."""
        dut = GTK3GObjectMixin()

        # These are inherited from the BaseMixin.
        assert dut.dic_error_message == {
            "unk_function": "{}: Unknown function '{}'.",
            "unk_property": "{}: Unknown property '{}'.",
            "unk_signal": "{}: Unknown signal '{}'.",
        }
        assert dut.dic_properties == {}

        # These are added by the GTK3GObjectMixin.
        assert dut._GTK3_GOBJECT_SIGNALS == ["notify"]
        assert dut.dic_handler_id == {"notify": -1}

    @pytest.mark.requirement("PTW-COM-W-002")
    @pytest.mark.unit
    def test_toolkit_attributes_available(self):
        """Verifies all GObject.Object methods are available via pytkwrap."""
        dut = GTK3GObjectMixin()

        for _attribute in [
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
        ]:
            assert hasattr(dut, _attribute)

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-GTK3-X-004")
    def test_do_set_callbacks(self):
        """Should set callback function for a GTK3GObjectMixin signal."""
        dut = GTK3GObjectMixin()
        dut.do_set_callbacks("notify", self.mock_callback)

        assert dut.dic_handler_id["notify"] != -1

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-GTK3-X-004")
    def test_do_set_callbacks_unknown_signal(self):
        """Should raise an UnkSignalError when passed an unknown signal name."""
        dut = GTK3GObjectMixin()
        pub.subscribe(self.no_signal_error_handler, "do_log_error")

        with pytest.raises(UnkSignalError):
            dut.do_set_callbacks("unk_signal", self.mock_callback)

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-GTK3-X-005")
    def test_do_set_callbacks_after(self):
        """Should set callback function for a GTK3GObjectMixin signal."""
        dut = GTK3GObjectMixin()
        dut.do_set_callbacks("notify", self.mock_callback, True)

        assert dut.dic_handler_id["notify"] != -1
