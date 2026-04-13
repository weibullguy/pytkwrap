# pylint: skip-file
# type: ignore
#
#       tests.common.test_widget_mixin.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the WidgetMixin class."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.common.mixins import (
    WidgetAttributes,
    WidgetMixin,
    make_widget_config,
)


@pytest.mark.order(0)
class TestWidgetMixin:
    """Test class for the WidgetMixin class."""

    @pytest.mark.unit
    def test_init(self):
        """Should create an instance of the WidgetMixin class."""
        dut = WidgetMixin()

        assert dut._WIDGET_ATTRIBUTES == {
            "label_text": "",
            "n_columns": 0,
            "n_rows": 0,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_attributes == {
            "label_text": "",
            "n_columns": 0,
            "n_rows": 0,
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.dic_error_message == {
            "unk_function": "{}: No such function {} exists.",
            "unk_signal": "{}: Unknown signal name '{}'.",
        }
        assert dut.label_text == ""
        assert dut.n_columns == 0
        assert dut.n_rows == 0
        assert dut.x_pos == 0
        assert dut.y_pos == 0

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = WidgetMixin()

        assert dut.do_get_attribute("label_text") == ""
        assert dut.do_get_attribute("n_columns") == 0
        assert dut.do_get_attribute("n_rows") == 0
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed an unknown attribute."""
        dut = WidgetMixin()

        with pytest.raises(KeyError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set default attribute values when passed an empty WidgetAttributes."""
        dut = WidgetMixin()
        dut.do_set_attributes(WidgetAttributes())

        assert dut.label_text == ""
        assert dut.n_columns == 0
        assert dut.n_rows == 0
        assert dut.x_pos == 0
        assert dut.y_pos == 0

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values in the WidgetAttributes passed in."""
        dut = WidgetMixin()
        dut.do_set_attributes(
            WidgetAttributes(
                label_text="Test Label Text", n_columns=3, n_rows=5, x_pos=5, y_pos=10
            )
        )

        assert dut.label_text == "Test Label Text"
        assert dut.n_columns == 3
        assert dut.n_rows == 5
        assert dut.x_pos == 5
        assert dut.y_pos == 10


@pytest.mark.unit
@pytest.mark.order(0)
def test_create_widget_config():
    """Should create a WidgetConfig."""
    dut = make_widget_config(WidgetMixin, {}, {})

    assert dut["attributes"] == {}
    assert dut["properties"] == {}
    assert dut["widget"] == WidgetMixin


@pytest.mark.unit
@pytest.mark.order(0)
def test_create_widget_config_with_attributes():
    """Should create a WidgetConfig with attributes amd properties."""
    dut = make_widget_config(
        WidgetMixin,
        {
            "label_text": "Test Label Text",
            "parent_id": 0,
            "record_id": 1,
            "x_pos": 0,
            "y_pos": 0,
        },
        {},
    )

    assert dut["widget"] == WidgetMixin
    assert dut["attributes"]["label_text"] == "Test Label Text"
    assert dut["attributes"]["parent_id"] == 0
    assert dut["attributes"]["record_id"] == 1
    assert dut["attributes"]["x_pos"] == 0
    assert dut["attributes"]["y_pos"] == 0
    assert dut["properties"] == {}
