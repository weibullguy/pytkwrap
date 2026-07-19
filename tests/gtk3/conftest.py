# Standard Library Imports
import os

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError, WrongTypeError

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.common.test_pytkwrap_mixin import TestPyTkWrapMixin

# pytkwrap Local Imports
from .constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)


@pytest.fixture(scope="function")
def image_file():
    _parent_dir_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _image_ = os.path.join(_parent_dir_, "data/pytkwrap.png")
    return _image_


@pytest.fixture(scope="class")
def skip_if_not_isolated(request):
    """Skip the test if the class needs to be tested in isolation."""
    if not request.config.getoption("--isolated", default=False):
        pytest.skip(
            "Testing this widget crashes at the C level when run as part of the full "
            "test suite due to GIO volume monitor initialization conflicts. Passes in "
            "isolation. --isolated was not specified."
        )


class BaseGTK3GObjectTests(TestPyTkWrapMixin):
    """Add GTK3-specific assertions to the common mixin tests."""

    widget_class = None
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_default_height = -1
    expected_default_tooltip = (
        "Missing tooltip, please file an issue to have one added."
    )
    expected_default_width = -1
    expected_get_value = []
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS
    expected_properties = {}
    expected_set_value = []
    expected_set_value_wrong_types = []

    def make_dut(self):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class()

    def mock_callback(self, widget, unk=None) -> None:
        """Callback method for testing."""
        assert isinstance(widget, self.widget_class)
        if unk is not None:
            print(unk)

    def mock_handler(self, package):
        """Mock handler for on_changed() calls."""
        assert isinstance(package, dict)

    def do_update_error_handler(self, message):
        """Error handler for do_update() errors."""
        assert (
            message
            == f"{self.widget_class.__name__}.do_update(): Unknown signal 'unk_signal'."
        )

    def get_attribute_error_handler(self, message):
        """Error handler for get_attribute() errors."""
        assert (
            message
            == f"{self.widget_class.__name__}.do_get_attribute(): Unknown attribute "
            f"'unk_attribute'."
        )

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

    def on_changed_error_handler(self, message):
        """Error handler for on_changed() errors."""
        assert (
            message
            == f"{self.widget_class.__name__}.on_changed(): Unknown signal 'unk_signal'."
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
        """Should create an instance of the widget class with attributes set to default
        values."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)

        # These are inherited from the PyTkWrapMixin.
        assert dut._DEFAULT_HEIGHT == self.expected_default_height
        assert dut._DEFAULT_TOOLTIP == self.expected_default_tooltip
        assert dut._DEFAULT_WIDTH == self.expected_default_width
        assert dut.dic_attributes == self.expected_attributes
        assert dut.dic_error_message == {
            "no_value": "{}: No value set or no method to retrieve value.",
            "unk_attribute": "{}: Unknown attribute '{}'.",
            "unk_function": "{}: Unknown function '{}'.",
            "unk_property": "{}: Unknown property '{}'.",
            "unk_signal": "{}: Unknown signal '{}'.",
            "wrong_type": "{}: Wrong type for value '{}': {}.",
        }
        assert dut.dic_handler_id == self.expected_handler_id
        assert dut.dic_properties == self.expected_properties

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-W-002")
    def test_toolkit_methods_available(self):
        """Verifies all GTK3 methods are available via pytkwrap."""
        dut = self.make_dut()

        for _method in self.expected_methods:
            assert hasattr(dut, _method)

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-015")
    def test_do_set_attributes(self):
        """Should set properties to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                column_types=[GObject.TYPE_STRING],
                index=3,
                listen_topic="test_listen_topic",
                send_topic="test_send_topic",
            )
        )

        assert dut.do_get_attribute("column_types") == [GObject.TYPE_STRING]
        assert dut.do_get_attribute("index") == 3
        assert dut.do_get_attribute("listen_topic") == "test_listen_topic"
        assert dut.do_get_attribute("send_topic") == "test_send_topic"

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
    @pytest.mark.requirement("PTW-GTK3-X-005")
    def test_do_set_callbacks_after(self):
        """Should set callback function for a GTK3GObjectMixin signal."""
        dut = self.make_dut()
        dut.do_set_callbacks("notify", self.mock_callback, True)

        assert dut.dic_handler_id["notify"] != -1

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


class BaseGTK3DataWidgetTests(BaseGTK3GObjectTests):
    """Add GTK3 data manipulation widget-specific assertions to the GObject mixin
    tests."""

    @pytest.mark.unit
    def test_do_set_value(self):
        """Should set the date."""
        dut = self.make_dut()

        for _value in self.expected_set_value:
            dut.do_set_value(_value[0])
            assert dut.do_get_value() == _value[1]

    @pytest.mark.unit
    def test_do_set_value_wrong_type(self):
        """Should raise a WrongTypeError and send a do_log_error message when passed the
        wrong data type."""
        dut = self.make_dut()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        for _wrong_type in self.expected_set_value_wrong_types:
            with pytest.raises(WrongTypeError):
                dut.do_set_value(_wrong_type)

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current date."""
        dut = self.make_dut()

        for _value in self.expected_get_value:
            dut.do_set_value(_value[0])
            assert dut.do_get_value() == _value[1]

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should update the properties with the default values when passed a data
        package with a value of None."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={-1: None})

        assert dut.dic_attributes == self.expected_attributes

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Should raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()

        if dut.dic_attributes["edit_signal"] is not None:
            dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
            pub.subscribe(self.do_update_error_handler, "do_log_error")
            pub.subscribe(dut.do_update, "rootTopic")
            dut.dic_attributes["edit_signal"] = "unk_signal"

            with pytest.raises(UnkSignalError):
                pub.sendMessage("rootTopic", package={-1: "Test Package"})

    @pytest.mark.unit
    def test_do_update_wrong_index(self):
        """Should do nothing when the data package key doesn't match the widget's
        index."""
        dut = self.make_dut()

        if dut.dic_attributes["edit_signal"] is not None:
            dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
            pub.subscribe(dut.do_update, "rootTopic")

            pub.sendMessage("rootTopic", package={10: False})

            assert dut.dic_attributes == self.expected_attributes
