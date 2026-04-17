# Standard Library Imports
import os
import sys
from io import StringIO

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3.widget import GTK3WidgetProperties
from tests.common.test_widget_mixin import TestWidgetMixin
from tests.common.test_data_widget_mixin import TestDataWidgetMixin


@pytest.fixture(scope="function")
def image_file():
    _parent_dir_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _image_ = os.path.join(_parent_dir_, "data/pytkwrap.png")
    return _image_


@pytest.fixture(autouse=True)
def pubsub_cleanup():
    yield
    pub.unsubAll()


@pytest.fixture(scope="class")
def suppress_stderr():
    _stderr = sys.stderr
    sys.stderr = StringIO()
    yield
    sys.stderr = _stderr


class BaseGTK3WidgetTests(TestWidgetMixin):
    """Add GTK3-specific assertions to the common mixin tests."""
    widget_class = None
    expected_default_height = -1
    expected_default_width = -1

    def make_dut(self):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class()

    def mock_callback(self, widget) -> None:
        """Callback method for testing."""
        assert isinstance(widget, self.widget_class)

    def no_signal_error_handler(self, message):
        """Error handler for do_set_callbacks() errors."""
        assert (
                message == f"{self.widget_class.__name__}.do_set_callbacks(): Unknown signal name "
                           "'unk_signal'."
        )

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3BaseWidget."""
        dut = self.make_dut()

        assert isinstance(dut, self.widget_class)
        assert all(v == -1 for v in dut.dic_handler_id.values())
        assert dut.dic_error_message == {
            "unk_function": "{}: No such function {} exists.",
            "unk_signal": "{}: Unknown signal name '{}'.",
        }
        assert isinstance(dut.dic_properties, dict)

    @pytest.mark.unit
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed a non-existent attribute."""
        dut = self.make_dut()

        with pytest.raises(KeyError):
            dut.do_get_attribute("database_name")

    @pytest.mark.unit
    def test_do_set_callbacks(self):
        """do_set_callbacks should set the callbacks for a pytkwrap widget."""
        dut = self.make_dut()

        # For each signal associated with a pytkwrap widget, first we verify that the
        # handler ID = -1, then we assign a callback and verify the handler ID != -1.
        # This also verifies each signal in the signal list exists for a widget.
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


class BaseGTK3DataWidgetTests(BaseGTK3WidgetTests, TestDataWidgetMixin):
    """Adds data widget assertions for GTK3 data widgets."""

    def do_update_error_handler(self, message):
        """Error handler for do_update() errors."""
        assert message == (
            f"{self.widget_class.__name__}.do_update(): Unknown signal name "
            f"'edit_signal'."
        )

    def mock_handler(self, node_id, package) -> None:
        """Mock message handler."""
        assert package == self.expected_package[node_id]

    def on_changed_error_handler(self, message):
        """Error handler for on_changed() errors."""
        assert message == (f"{self.widget_class.__name__}.on_changed(): Unknown signal name "
                           f"'edit_signal'.")

    @pytest.mark.skip
    def test_do_update(self):
        pass

    @pytest.mark.skip
    def test_do_update_wrong_field(self):
        pass

    @pytest.mark.skip
    def test_on_changed(self):
        pass
