"""Test module for the WidgetMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import sys

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.common.mixins import WidgetAttributes, WidgetMixin, make_widget_config


@pytest.mark.order(1)
class TestWidgetMixin:
    """Test class for the WidgetMixin class."""

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-005")
    @pytest.mark.requirement("PTW-COM-X-006")
    @pytest.mark.requirement("PTW-COM-X-006.001")
    @pytest.mark.requirement("PTW-COM-X-007")
    @pytest.mark.requirement("PTW-COM-X-020")
    def test_init(self):
        """Should create an instance of the WidgetMixin class with attributes set to
        default values."""
        dut = WidgetMixin()

        assert dut._DEFAULT_HEIGHT == -1
        assert (
            dut._DEFAULT_TOOLTIP
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut._DEFAULT_WIDTH == -1
        assert dut._WIDGET_ATTRIBUTES == {
            "n_columns": 0,
            "n_rows": 0,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_attributes == {
            "n_columns": 0,
            "n_rows": 0,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_error_message == {
            "unk_function": "{}: No such function {} exists.",
            "unk_signal": "{}: Unknown signal name '{}'.",
        }

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
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = WidgetMixin()

        assert dut.do_get_attribute("n_columns") == 0
        assert dut.do_get_attribute("n_rows") == 0
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-008")
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed an unknown attribute."""
        dut = WidgetMixin()

        with pytest.raises(KeyError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_attributes_default(self):
        """Should set attributes to their default value when passed an empty
        WidgetAttributes."""
        dut = WidgetMixin()
        dut.do_set_attributes(WidgetAttributes())

        assert dut.dic_attributes["n_columns"] == 0
        assert dut.dic_attributes["n_rows"] == 0
        assert dut.dic_attributes["x_pos"] == 0
        assert dut.dic_attributes["y_pos"] == 0

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_attributes(self):
        """Should set attributes to the values in the WidgetAttributes passed in."""
        dut = WidgetMixin()
        dut.do_set_attributes(
            WidgetAttributes(n_columns=3, n_rows=5, x_pos=5, y_pos=10)
        )

        assert dut.dic_attributes["n_columns"] == 3
        assert dut.dic_attributes["n_rows"] == 5
        assert dut.dic_attributes["x_pos"] == 5
        assert dut.dic_attributes["y_pos"] == 10

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-009")
    def test_do_set_attributes_partial(self):
        """Should preserve any attribute values not present in the WidgetAttributes
        passed in."""
        dut = WidgetMixin()
        dut.do_set_attributes(WidgetAttributes(n_rows=51, y_pos=15))

        assert dut.dic_attributes["n_columns"] == 0
        assert dut.dic_attributes["n_rows"] == 51
        assert dut.dic_attributes["x_pos"] == 0
        assert dut.dic_attributes["y_pos"] == 15

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-023")
    def test_class_attributes_not_mutated(self):
        """_WIDGET_ATTRIBUTES should not be mutated by do_set_attributes()."""
        _original = dict(WidgetMixin._WIDGET_ATTRIBUTES)
        dut = WidgetMixin()
        dut.do_set_attributes(WidgetAttributes(n_columns=99))

        assert WidgetMixin._WIDGET_ATTRIBUTES == _original

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-024")
    def test_dic_attributes_is_sole_store(self):
        """WidgetMixin should not store attribute values outside dic_attributes."""
        dut = WidgetMixin()

        _instance_attrs = set(vars(dut).keys())
        _expected = {"dic_attributes", "dic_error_message"}

        assert _instance_attrs == _expected


@pytest.mark.unit
@pytest.mark.order(4)
def test_create_widget_config():
    """Should create a WidgetConfig."""
    dut = make_widget_config(WidgetMixin(), WidgetAttributes(), {})

    assert dut["attributes"] == {}
    assert dut["properties"] == {}
    assert isinstance(dut["widget"], WidgetMixin)


@pytest.mark.unit
@pytest.mark.order(4)
def test_create_widget_config_with_attributes():
    """Should create a WidgetConfig with attributes amd properties."""
    dut = make_widget_config(
        WidgetMixin(),
        WidgetAttributes(
            x_pos=10,
            y_pos=10,
        ),
        {},
    )

    assert isinstance(dut["widget"], WidgetMixin)
    assert dut["attributes"]["x_pos"] == 10
    assert dut["attributes"]["y_pos"] == 10
    assert dut["properties"] == {}
