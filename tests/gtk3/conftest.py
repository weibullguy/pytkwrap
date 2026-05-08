# Standard Library Imports
import os
import sys
from io import StringIO

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkAttributeError, UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.common.test_pytkwrap_mixin import TestPyTkWrapMixin
from tests.common.test_toolkit_mixin import TestToolkitMixin


@pytest.fixture(scope="function")
def image_file():
    _parent_dir_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _image_ = os.path.join(_parent_dir_, "data/pytkwrap.png")
    return _image_


@pytest.mark.order(3)
class BaseGTK3GObjectTests(TestToolkitMixin):
    """Add GTK3-specific assertions to the common mixin tests."""

    widget_class = None
    expected_attributes = []
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1
    expected_handler_id = {}
    expected_properties = {}

    def make_dut(self):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class()

    def mock_callback(self, widget) -> None:
        """Callback method for testing."""
        assert isinstance(widget, self.widget_class)

    def no_signal_error_handler(self, message):
        """Error handler for do_set_callbacks() errors."""
        assert (
            message
            == f"{self.widget_class.__name__}.do_set_callbacks(): Unknown signal 'unk_signal'."
        )

    def no_value_error_handler(self, message):
        """Error handler for do_get_value() errors."""
        assert (
            message == f"{self.widget_class.__name__}.do_get_value(): No value set "
            f"or no method to "
            "retrieve value."
        )

    def wrong_type_error_handler(self, message) -> None:
        """Error handler for do_set_value() errors."""
        assert (
            f"{self.widget_class.__name__}.do_set_value(): Wrong type for value"
            in message
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-GTK3-X-001")
    @pytest.mark.requirement("PTW-GTK3-X-002")
    @pytest.mark.requirement("PTW-GTK3-X-003")
    def test_init(self):
        """Should create an instance of the GTK3GObjectMixin class with attributes set
        to default values."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)

        # These are inherited from the ToolkitMixin.
        assert dut._DEFAULT_HEIGHT == -1
        assert (
            dut._DEFAULT_TOOLTIP
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut._DEFAULT_WIDTH == -1
        assert dut.dic_error_message == {
            "no_value": "{}: No value set or no method to retrieve value.",
            "unk_function": "{}: Unknown function '{}'.",
            "unk_property": "{}: Unknown property '{}'.",
            "unk_signal": "{}: Unknown signal '{}'.",
            "wrong_type": "{}: Wrong type for value '{}': {}.",
        }
        assert dut.dic_properties == self.expected_properties

        # These are added by the GTK3GObjectMixin.
        assert dut._GTK3_GOBJECT_SIGNALS == ["notify"]
        assert dut.dic_handler_id == self.expected_handler_id

    @pytest.mark.requirement("PTW-COM-W-002")
    @pytest.mark.unit
    def test_toolkit_attributes_available(self):
        """Verifies all GObject.Object methods are available via pytkwrap."""
        dut = self.make_dut()

        for _attribute in self.expected_attributes:
            assert hasattr(dut, _attribute)

    @pytest.mark.unit
    def test_do_set_callbacks(self):
        """do_set_callbacks should set the callbacks for a pytkwrap widget."""
        dut = self.make_dut()

        # For each signal associated with a pytkwrap GTK3 widget, first we verify that
        # the handler ID = -1, then we assign a callback and verify the handler
        # ID != -1.  This also verifies each signal in the signal list exists for a
        # widget.
        for signal, handler_id in dut.dic_handler_id.items():
            assert handler_id == -1, f"Expected {signal} to be -1, got {handler_id}."
            dut.do_set_callbacks(signal, self.mock_callback)
            assert dut.dic_handler_id[signal] != -1

    @pytest.mark.unit
    def test_do_set_callbacks_no_signal(self):
        """Should raise an UnkSignalError when the signal name does not exist."""
        dut = self.make_dut()
        pub.subscribe(self.no_signal_error_handler, "do_log_error")

        with pytest.raises(UnkSignalError):
            dut.do_set_callbacks("unk_signal", self.mock_callback)

    @pytest.mark.unit
    def test_do_set_callbacks_no_callback(self):
        """Should raise an AttributeError when the callback does not exist."""
        dut = self.make_dut()

        with pytest.raises(AttributeError):
            dut.do_set_callbacks("event", dut.non_existent_callback)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties


@pytest.mark.order(3)
class BaseGTK3WidgetTests(TestPyTkWrapMixin):
    """Add GTK3-specific assertions to the common mixin tests."""

    widget_class = None
    expected_attributes = []
    expected_handler_id = {}
    expected_properties = {}

    def make_dut(self):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class()

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3BaseWidget."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)

        # These are inherited from GTK3GObjectMixin.
        assert dut._DEFAULT_HEIGHT == -1
        assert (
            dut._DEFAULT_TOOLTIP
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut._DEFAULT_WIDTH == -1
        assert dut.dic_attributes == {
            "index": -1,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_error_message == {
            "no_value": "{}: No value set or no method to retrieve value.",
            "unk_attribute": "{}: Unknown attribute '{}'.",
            "unk_function": "{}: Unknown function '{}'.",
            "unk_property": "{}: Unknown property '{}'.",
            "unk_signal": "{}: Unknown signal '{}'.",
            "wrong_type": "{}: Wrong type for value '{}': {}.",
        }

        # These are added by GTK3Widget.
        assert dut._GTK3_WIDGET_PROPERTIES == {
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
            "tooltip_markup": "",
            "tooltip_text": "",
            "valign": Gtk.Align.FILL,
            "vexpand": False,
            "vexpand_set": False,
            "visible": False,
            "width_request": -1,
            "window": None,
        }
        assert dut._GTK3_WIDGET_SIGNALS == [
            "destroy",
            "direction-changed",
            "hide",
            "keynav-failed",
            "map",
            "mnemonic-activate",
            "move-focus",
            "query-tooltip",
            "realize",
            "show",
            "state-flags-changed",
            "unmap",
            "unrealize",
        ]
        assert dut.dic_handler_id == self.expected_handler_id
        assert dut.dic_properties == self.expected_properties

    @pytest.mark.requirement("PTW-COM-W-002")
    @pytest.mark.unit
    def test_toolkit_attributes_available(self):
        """Verifies all Gtk methods are available via pytkwrap."""
        dut = self.make_dut()

        for _attribute in self.expected_attributes:
            assert hasattr(dut, _attribute)

    @pytest.mark.unit
    def test_do_get_attribute_unknown(self):
        """Should raise an UnkAttributeError when passed a non-existent attribute."""
        dut = self.make_dut()

        with pytest.raises(UnkAttributeError):
            dut.do_get_attribute("database_name")

    @pytest.mark.unit
    def test_do_set_properties_zero_height(self):
        """Should use _DEFAULT_HEIGHT when height_request is 0."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(height_request=0))

        assert (
            dut.dic_properties["height_request"] == self.expected_default_height
        )  # falls back to _DEFAULT_HEIGHT

    @pytest.mark.unit
    def test_do_set_properties_zero_width(self):
        """Should use _DEFAULT_WIDTH when width_request is 0."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(width_request=0))

        assert (
            dut.dic_properties["width_request"] == self.expected_default_width
        )  # falls back to _DEFAULT_WIDTH
