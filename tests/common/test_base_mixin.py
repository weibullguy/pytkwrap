"""Test module for the BaseMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.common.mixins import BaseMixin


@pytest.mark.order(0)
class TestBaseMixin:
    """Test class for the BaseMixin class."""

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-001")
    @pytest.mark.requirement("PTW-COM-X-002")
    @pytest.mark.requirement("PTW-COM-X-003")
    def test_init(self):
        """Should create an instance of the BaseMixin class with attributes set to
        default values."""
        dut = BaseMixin()

        assert dut.dic_attributes == {}
        assert dut.dic_error_message == {
            "unk_function": "{}: No such function {} exists.",
            "unk_signal": "{}: Unknown signal name '{}'.",
        }

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-002")
    def test_dic_attributes_not_shared(self):
        """Two instances of the BaseMixin should not share dic_attributes."""
        dut1 = BaseMixin()
        dut2 = BaseMixin()

        assert not dut1.dic_attributes is dut2.dic_attributes

        dut1.dic_attributes["n_columns"] = 3

        assert dut1.dic_attributes["n_columns"] == 3
        assert dut2.dic_attributes == {}

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-004")
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
    @pytest.mark.requirement("PTW-COM-X-024")
    def test_dic_attributes_is_sole_store(self):
        """BaseMixin should not store attribute values outside dic_attributes."""
        dut = BaseMixin()

        # Only dic_attributes and dic_error_message should be set as instance attributes
        _instance_attrs = set(vars(dut).keys())
        _expected = {"dic_attributes", "dic_error_message"}

        assert _instance_attrs == _expected
