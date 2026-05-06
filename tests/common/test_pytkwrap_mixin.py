"""Test module for the PyTkWrapMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap import UnkAttributeError
from pytkwrap.common.mixins import (
    PyTkWrapAttributes,
    PyTkWrapMixin,
    make_pytkwrap_config,
)


@pytest.mark.order(0)
class TestPyTkWrapMixin:
    """Test class for the PyTkWrapMixin class."""

    @staticmethod
    def unknown_attribute_error_handler(message):
        """Error handler for do_get_attribute() errors."""
        assert (
            message == "PyTkWrapMixin.do_get_attribute(): Unknown attribute "
            "'unk_attribute'."
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-011")
    @pytest.mark.requirement("PTW-COM-X-012")
    @pytest.mark.requirement("PTW-COM-X-013")
    @pytest.mark.requirement("PTW-COM-X-007")
    @pytest.mark.requirement("PTW-COM-X-020")
    def test_init(self):
        """Should create an instance of the PyTkWrapMixin class with attributes set to
        default values."""
        dut = PyTkWrapMixin()

        assert dut._PYTKWRAP_ATTRIBUTES == {
            "index": -1,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_attributes == {
            "index": -1,
            "x_pos": 0,
            "y_pos": 0,
        }

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-013")
    def test_dic_attributes_not_shared(self):
        """Should not share dic_attributes between instances."""
        dut1 = PyTkWrapMixin()
        dut2 = PyTkWrapMixin()

        assert not dut1.dic_attributes is dut2.dic_attributes

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-011")
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
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = PyTkWrapMixin()

        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_get_attribute_unknown(self):
        """Should raise a UnkAttributeError when passed an unknown attribute name."""
        dut = PyTkWrapMixin()
        pub.subscribe(self.unknown_attribute_error_handler, "do_log_error")

        with pytest.raises(UnkAttributeError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-015")
    def test_do_set_attributes_default(self):
        """Should set attributes to their default value when passed an empty
        PyTkWrapAttributes."""
        dut = PyTkWrapMixin()
        dut.do_set_attributes(PyTkWrapAttributes())

        assert dut.dic_attributes["index"] == -1
        assert dut.dic_attributes["x_pos"] == 0
        assert dut.dic_attributes["y_pos"] == 0

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

        assert dut.dic_attributes["index"] == -1
        assert dut.dic_attributes["x_pos"] == 0
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
        _expected = {"dic_attributes", "dic_error_message"}

        assert _instance_attrs == _expected


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
