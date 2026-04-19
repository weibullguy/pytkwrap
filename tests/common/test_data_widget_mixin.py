# pylint: skip-file
# type: ignore
#
#       tests.common.test_data_widget_mixin.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the DataWidgetMixin class."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.common.mixins import DataWidgetAttributes, DataWidgetMixin


@pytest.mark.order(1)
class TestDataWidgetMixin:
    """Test class for the DataWidgetMixin class."""

    @pytest.mark.unit
    def test_init(self):
        """Should create an instance of the DataWidgetMixin class."""
        dut = DataWidgetMixin()

        assert dut._DATA_WIDGET_ATTRIBUTES == {
            "datatype": None,
            "default": None,
            "edit_signal": "",
            "field": "",
            "font_description": None,
            "format": "{}",
            "index": -1,
            "listen_topic": "listen_topic",
            "parent_id": -1,
            "record_id": -1,
            "send_topic": "send_topic",
        }
        assert dut.dic_attributes == {
            "datatype": None,
            "default": None,
            "edit_signal": "",
            "field": "",
            "font_description": None,
            "format": "{}",
            "index": -1,
            "label_text": "",
            "listen_topic": "listen_topic",
            "n_columns": 0,
            "n_rows": 0,
            "parent_id": -1,
            "record_id": -1,
            "send_topic": "send_topic",
            "x_pos": 0,
            "y_pos": 0,
        }
        assert dut.do_get_attribute("datatype") is None
        assert dut.do_get_attribute("default") is None
        assert dut.do_get_attribute("edit_signal") == ""
        assert dut.do_get_attribute("field") == ""
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("parent_id") == -1
        assert dut.do_get_attribute("record_id") == -1
        assert dut.do_get_attribute("send_topic") == "send_topic"

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = DataWidgetMixin()

        assert dut.do_get_attribute("datatype") is None
        assert dut.do_get_attribute("default") is None
        assert dut.do_get_attribute("edit_signal") == ""
        assert dut.do_get_attribute("field") == ""
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("parent_id") == -1
        assert dut.do_get_attribute("record_id") == -1
        assert dut.do_get_attribute("send_topic") == "send_topic"

    @pytest.mark.unit
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed an unknown attribute."""
        dut = DataWidgetMixin()

        with pytest.raises(KeyError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set default attribute values when passed an empty
        DataWidgetAttributes."""
        dut = DataWidgetMixin()
        dut.do_set_attributes(DataWidgetAttributes())

        assert dut.do_get_attribute("datatype") is None
        assert dut.do_get_attribute("default") is None
        assert dut.do_get_attribute("edit_signal") == ""
        assert dut.do_get_attribute("field") == ""
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("parent_id") == -1
        assert dut.do_get_attribute("record_id") == -1
        assert dut.do_get_attribute("send_topic") == "send_topic"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values in the DataWidgetAttributes passed in."""
        dut = DataWidgetMixin()
        dut.do_set_attributes(
            DataWidgetAttributes(
                datatype="str",
                default="Default Text",
                edit_signal="test_signal",
                field="test_field",
                index=10,
            )
        )
        assert dut.do_get_attribute("datatype") == "str"
        assert dut.do_get_attribute("default") == "Default Text"
        assert dut.do_get_attribute("edit_signal") == "test_signal"
        assert dut.do_get_attribute("field") == "test_field"
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == 10
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("parent_id") == -1
        assert dut.do_get_attribute("record_id") == -1
        assert dut.do_get_attribute("send_topic") == "send_topic"
