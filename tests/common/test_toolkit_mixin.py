"""Test module for the ToolkitMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap import NoValueError, PytkwrapError, UnkPropertyError
from pytkwrap.common.mixins import ToolkitMixin
from pytkwrap.exceptions import WrongTypeError


@pytest.mark.order(0)
class TestToolkitMixin:
    """Test class for the ToolkitMixin class."""

    @staticmethod
    def unknown_property_error_handler(message):
        """Error handler for do_get_property() errors."""
        assert (
            message
            == "ToolkitMixin.do_get_property(): Unknown property 'unk_property'."
        )

    @staticmethod
    def none_property_error_handler(message):
        """Error handler for do_set_property() errors."""
        assert (
            message == "ToolkitMixin.do_set_properties(): Properties are None or a "
            "non-iterable object: 'None'."
        )

    @staticmethod
    def non_iterable_property_error_handler(message):
        """Error handler for do_set_property() errors."""
        assert (
            message == "ToolkitMixin.do_set_properties(): Properties are not valid "
            "key-value pairs: 'Non-iterable property'."
        )

    @staticmethod
    def no_value_error_handler(message):
        """Error handler for do_get_value() errors."""
        assert (
            message == "ToolkitMixin.do_get_value(): No value set or no method to "
            "retrieve value."
        )

    @staticmethod
    def wrong_type_error_handler(message):
        """Error handler for do_set_value() errors."""
        assert (
            message == "ToolkitMixin.do_set_value(): Wrong type for value 'None': "
            "<class 'NoneType'>."
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-001")
    @pytest.mark.requirement("PTW-COM-X-002")
    @pytest.mark.requirement("PTW-COM-X-003")
    @pytest.mark.requirement("PTW-COM-X-004")
    @pytest.mark.requirement("PTW-COM-X-006")
    def test_init(self):
        """Should create an instance of the ToolkitMixin class with attributes set to
        default values."""
        dut = ToolkitMixin()

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
        assert dut.dic_handler_id == {}
        assert dut.dic_properties == {}

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-002")
    def test_dic_properties_not_shared(self):
        """Should not share dic_properties between instances."""
        dut1 = ToolkitMixin()
        dut2 = ToolkitMixin()

        assert not dut1.dic_properties is dut2.dic_properties

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-005")
    def test_no_toolkit_imports(self):
        """Should not import any toolkit-specific modules."""
        # Standard Library Imports
        import ast
        import inspect

        # pytkwrap Package Imports
        import pytkwrap.common.mixins as mixins_module

        _source = inspect.getsource(mixins_module)
        _tree = ast.parse(_source)

        _toolkit_names = {"Gdk", "GdkPixbuf", "Gio", "GLib", "GObject", "Gtk", "Pango"}
        _imports = set()

        for _node in ast.walk(_tree):
            if isinstance(_node, ast.Import):
                for _alias in _node.names:
                    _imports.add(_alias.name.split(".")[0])
            elif isinstance(_node, ast.ImportFrom):
                if _node.module:
                    _imports.add(_node.module.split(".")[0])

        assert not _toolkit_names & _imports, (
            f"Toolkit-specific imports found in common layer: "
            f"{_toolkit_names & _imports}"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-008")
    def test_do_get_property_unknown(self):
        """Should raise an UnkPropertyError."""
        dut = ToolkitMixin()
        pub.subscribe(self.unknown_property_error_handler, "do_log_error")

        with pytest.raises(UnkPropertyError):
            dut.do_get_property("unk_property")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_property(self):
        """Should set dic_properties to new values when passed a dict."""
        dut = ToolkitMixin()
        dut.do_set_properties({"new_prop": 14})

        assert dut.dic_properties["new_prop"] == 14

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_property_list_list(self):
        """Should set dic_properties to new values when passed a list of lists."""
        dut = ToolkitMixin()
        dut.do_set_properties([["new_prop", 14], ["new_prop_2", "Twenty-two"]])

        assert dut.dic_properties["new_prop"] == 14
        assert dut.dic_properties["new_prop_2"] == "Twenty-two"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_property_list_tuple(self):
        """Should set dic_properties to new values when passed a list of tuples."""
        dut = ToolkitMixin()
        dut.do_set_properties([("new_prop", 14), ("new_prop_2", "Twenty-two")])

        assert dut.dic_properties["new_prop"] == 14
        assert dut.dic_properties["new_prop_2"] == "Twenty-two"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-010")
    def test_do_set_property_type_error(self):
        """Should raise a PytkwrapError and send a do_log_error message when passed
        None."""
        dut = ToolkitMixin()
        pub.subscribe(self.none_property_error_handler, "do_log_error")

        with pytest.raises(PytkwrapError):
            dut.do_set_properties(None)

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-010")
    def test_do_set_property_value_error(self):
        """Should raise a PytkwrapError and send a do_log_error message when passed a
        non-iterable properties."""
        dut = ToolkitMixin()
        pub.subscribe(self.non_iterable_property_error_handler, "do_log_error")

        with pytest.raises(PytkwrapError):
            dut.do_set_properties("Non-iterable property")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-024")
    def test_dic_properties_is_sole_store(self):
        """ToolkitMixin should not store property values outside dic_properties."""
        dut = ToolkitMixin()

        _instance_attrs = set(vars(dut).keys())
        _expected = {"dic_properties", "dic_error_message", "dic_handler_id"}

        assert _instance_attrs == _expected

    @pytest.mark.unit
    def test_do_get_value_missing(self):
        """Should raise a NoValueError and send a do_log_error message when called."""
        dut = ToolkitMixin()
        pub.subscribe(self.no_value_error_handler, "do_log_error")

        with pytest.raises(NoValueError):
            dut.do_get_value()

    @pytest.mark.unit
    def test_do_set_value_wrong_type(self):
        """Should raise a WrongTypeError and send a do_log_error message when called."""
        dut = ToolkitMixin()
        pub.subscribe(self.wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(None)
