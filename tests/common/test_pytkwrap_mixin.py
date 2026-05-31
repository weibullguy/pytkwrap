"""Test module for the PyTkWrapMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap import NoValueError, PytkwrapError, UnkAttributeError, UnkPropertyError
from pytkwrap.common.mixins import (
    PyTkWrapAttributes,
    PyTkWrapMixin,
    make_pytkwrap_config,
)
from pytkwrap.exceptions import WrongTypeError

_TOOLKIT_NAMES = {"Gdk", "GdkPixbuf", "Gio", "GLib", "GObject", "Gtk", "Pango"}


def no_value_error_handler(message):
    """Error handler for do_get_value() errors."""
    assert (
        message == "PyTkWrapMixin.do_get_value(): No value set or no method to "
        "retrieve value."
    )


def none_property_error_handler(message):
    """Error handler for do_set_property() errors."""
    assert (
        message == "PyTkWrapMixin.do_set_properties(): Properties are None or a "
        "non-iterable object: 'None'."
    )


def non_iterable_property_error_handler(message):
    """Error handler for do_set_property() errors."""
    assert (
        message == "PyTkWrapMixin.do_set_properties(): Properties are not valid "
        "key-value pairs: 'Non-iterable property'."
    )


def unknown_attribute_error_handler(message):
    """Error handler for do_get_attribute() errors."""
    assert (
        message == "PyTkWrapMixin.do_get_attribute(): Unknown attribute "
        "'unk_attribute'."
    )


def unknown_property_error_handler(message):
    """Error handler for do_get_property() errors."""
    assert (
        message == "PyTkWrapMixin.do_get_property(): Unknown property 'unk_property'."
    )


def wrong_type_error_handler(message):
    """Error handler for do_set_value() errors."""
    assert (
        message == "PyTkWrapMixin.do_set_value(): Wrong type for value 'None': "
        "<class 'NoneType'>."
    )


@pytest.mark.order(0)
class TestPyTkWrapMixin:
    """Test class for the PyTkWrapMixin class."""

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-001")
    @pytest.mark.requirement("PTW-COM-X-002")
    @pytest.mark.requirement("PTW-COM-X-003")
    @pytest.mark.requirement("PTW-COM-X-004")
    @pytest.mark.requirement("PTW-COM-X-006")
    def test_init(self):
        """Should create an instance of the PyTkWrapMixin class with attributes set to
        default values."""
        dut = PyTkWrapMixin()

        assert dut._DEFAULT_HEIGHT == -1
        assert (
            dut._DEFAULT_TOOLTIP
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut._DEFAULT_WIDTH == -1
        assert dut.dic_attributes == {
            "axis": None,
            "canvas": None,
            "data_type": None,
            "default_value": None,
            "edit_signal": None,
            "figure": None,
            "font_description": None,
            "format": None,
            "index": None,
            "listen_topic": None,
            "n_columns": None,
            "n_rows": None,
            "send_topic": None,
            "x_pos": None,
            "y_pos": None,
        }
        assert dut.dic_error_message == {
            "no_value": "{}: No value set or no method to retrieve value.",
            "unk_attribute": "{}: Unknown attribute '{}'.",
            "unk_function": "{}: Unknown function '{}'.",
            "unk_property": "{}: Unknown property '{}'.",
            "unk_signal": "{}: Unknown signal '{}'.",
            "wrong_type": "{}: Wrong type for value '{}': {}.",
        }
        assert dut.dic_handler_id == {}
        assert dut.dic_properties == {}

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-013")
    def test_dic_attributes_not_shared(self):
        """Should not share dic_attributes between instances."""
        dut1 = PyTkWrapMixin()
        dut2 = PyTkWrapMixin()

        assert not dut1.dic_attributes is dut2.dic_attributes

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = PyTkWrapMixin()

        assert dut.do_get_attribute("index") is None
        assert dut.do_get_attribute("x_pos") is None
        assert dut.do_get_attribute("y_pos") is None

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_get_attribute_unknown(self):
        """Should raise a UnkAttributeError when passed an unknown attribute name."""
        dut = PyTkWrapMixin()
        pub.subscribe(unknown_attribute_error_handler, "do_log_error")

        with pytest.raises(UnkAttributeError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-015")
    def test_do_set_attributes(self):
        """Should set attributes to the values in the PyTkWrapAttributes passed in."""
        dut = PyTkWrapMixin()
        dut.do_set_attributes(PyTkWrapAttributes(index=3, x_pos=5, y_pos=10))

        assert dut.dic_attributes["index"] == 3
        assert dut.dic_attributes["x_pos"] == 5
        assert dut.dic_attributes["y_pos"] == 10

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-015")
    def test_do_set_attributes_partial(self):
        """Should preserve any attribute values not present in the PyTkWrapAttributes
        passed in."""
        dut = PyTkWrapMixin()
        dut.do_set_attributes(PyTkWrapAttributes(y_pos=15))

        assert dut.dic_attributes["index"] is None
        assert dut.dic_attributes["x_pos"] is None
        assert dut.dic_attributes["y_pos"] == 15

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-023")
    def test_class_attributes_not_mutated(self):
        """_WIDGET_ATTRIBUTES should not be mutated by do_set_attributes()."""
        _original = dict(PyTkWrapMixin._PYTKWRAP_ATTRIBUTES)

        dut = PyTkWrapMixin()
        dut.do_set_attributes(PyTkWrapAttributes(index=99))

        assert PyTkWrapMixin._PYTKWRAP_ATTRIBUTES == _original

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-025")
    def test_dic_attributes_is_sole_store(self):
        """PyTkWrapMixin should not store attribute values outside dic_attributes."""
        dut = PyTkWrapMixin()

        _instance_attrs = set(vars(dut).keys())
        _expected = {
            "dic_attributes",
            "dic_error_message",
            "dic_handler_id",
            "dic_properties",
        }

        assert _instance_attrs == _expected

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-002")
    def test_dic_properties_not_shared(self):
        """Should not share dic_properties between instances."""
        dut1 = PyTkWrapMixin()
        dut2 = PyTkWrapMixin()

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

        _imports = set()

        for _node in ast.walk(_tree):
            if isinstance(_node, ast.Import):
                for _alias in _node.names:
                    _imports.add(_alias.name.split(".")[0])
            elif isinstance(_node, ast.ImportFrom):
                if _node.module:
                    _imports.add(_node.module.split(".")[0])

        assert not _TOOLKIT_NAMES & _imports, (
            f"Toolkit-specific imports found in common layer: "
            f"{_TOOLKIT_NAMES & _imports}"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-008")
    def test_do_get_property_unknown(self):
        """Should raise an UnkPropertyError."""
        dut = PyTkWrapMixin()
        pub.subscribe(unknown_property_error_handler, "do_log_error")

        with pytest.raises(UnkPropertyError):
            dut.do_get_property("unk_property")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_properties(self):
        """Should set dic_properties to new values when passed a dict."""
        dut = PyTkWrapMixin()
        dut.do_set_properties({"new_prop": 14})

        assert dut.dic_properties["new_prop"] == 14

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_properties_list_list(self):
        """Should set dic_properties to new values when passed a list of lists."""
        dut = PyTkWrapMixin()
        dut.do_set_properties([["new_prop", 14], ["new_prop_2", "Twenty-two"]])

        assert dut.dic_properties["new_prop"] == 14
        assert dut.dic_properties["new_prop_2"] == "Twenty-two"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_properties_list_tuple(self):
        """Should set dic_properties to new values when passed a list of tuples."""
        dut = PyTkWrapMixin()
        dut.do_set_properties([("new_prop", 14), ("new_prop_2", "Twenty-two")])

        assert dut.dic_properties["new_prop"] == 14
        assert dut.dic_properties["new_prop_2"] == "Twenty-two"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-010")
    def test_do_set_properties_type_error(self):
        """Should raise a PytkwrapError and send a do_log_error message when passed
        None."""
        dut = PyTkWrapMixin()
        pub.subscribe(none_property_error_handler, "do_log_error")

        with pytest.raises(PytkwrapError):
            # noinspection PyTypeChecker
            dut.do_set_properties(None)

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-010")
    def test_do_set_properties_value_error(self):
        """Should raise a PytkwrapError and send a do_log_error message when passed non-
        iterable properties."""
        dut = PyTkWrapMixin()
        pub.subscribe(non_iterable_property_error_handler, "do_log_error")

        with pytest.raises(PytkwrapError):
            # noinspection PyTypeChecker
            dut.do_set_properties("Non-iterable property")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-024")
    def test_dic_properties_is_sole_store(self):
        """PyTkWrapMixin should not store property values outside dic_properties."""
        dut = PyTkWrapMixin()

        _instance_attrs = set(vars(dut).keys())
        _expected = {
            "dic_attributes",
            "dic_properties",
            "dic_error_message",
            "dic_handler_id",
        }

        assert _instance_attrs == _expected

    @pytest.mark.unit
    def test_do_get_value_missing(self):
        """Should raise a NoValueError and send a do_log_error message when called."""
        dut = PyTkWrapMixin()
        pub.subscribe(no_value_error_handler, "do_log_error")

        with pytest.raises(NoValueError):
            dut.do_get_value()

    @pytest.mark.unit
    def test_do_set_value_wrong_type(self):
        """Should raise a WrongTypeError and send a do_log_error message when called."""
        dut = PyTkWrapMixin()
        pub.subscribe(wrong_type_error_handler, "do_log_error")

        with pytest.raises(WrongTypeError):
            dut.do_set_value(None)


@pytest.mark.unit
@pytest.mark.order(1)
def test_create_widget_config():
    """Should create a PyTkWrapConfig."""
    dut = make_pytkwrap_config(PyTkWrapMixin(), PyTkWrapAttributes(), {})

    assert dut["attributes"] == {}
    assert dut["properties"] == {}
    assert isinstance(dut["widget"], PyTkWrapMixin)


@pytest.mark.unit
@pytest.mark.order(1)
def test_create_widget_config_with_attributes():
    """Should create a PyTkWrapConfig with attributes amd properties."""
    dut = make_pytkwrap_config(
        PyTkWrapMixin(),
        PyTkWrapAttributes(
            x_pos=10,
            y_pos=10,
        ),
        {},
    )

    assert isinstance(dut["widget"], PyTkWrapMixin)
    assert dut["attributes"]["x_pos"] == 10
    assert dut["attributes"]["y_pos"] == 10
    assert dut["properties"] == {}
