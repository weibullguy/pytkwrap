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
            "font_allow_breaks": "",
            "font_bgalpha": "",
            "font_bgcolor": "",
            "font_family": "",
            "font_features": "",
            "font_fgalpha": "",
            "font_fgcolor": "",
            "font_gravity": "",
            "font_gravity_hint": "",
            "font_insert_hyphens": "",
            "font_lang": "",
            "font_letter_spacing": "",
            "font_overline": "",
            "font_overline_color": "",
            "font_rise": "",
            "font_scale": "",
            "font_size": "",
            "font_stretch": "",
            "font_strikethrough": "",
            "font_strikethrough_color": "",
            "font_style": "",
            "font_underline": "",
            "font_underline_color": "",
            "font_variant": "",
            "font_variations": "",
            "font_weight": "",
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
            "font_allow_breaks": "",
            "font_bgalpha": "",
            "font_bgcolor": "",
            "font_family": "",
            "font_features": "",
            "font_fgalpha": "",
            "font_fgcolor": "",
            "font_gravity": "",
            "font_gravity_hint": "",
            "font_insert_hyphens": "",
            "font_lang": "",
            "font_letter_spacing": "",
            "font_overline": "",
            "font_overline_color": "",
            "font_rise": "",
            "font_scale": "",
            "font_size": "",
            "font_stretch": "",
            "font_strikethrough": "",
            "font_strikethrough_color": "",
            "font_style": "",
            "font_underline": "",
            "font_underline_color": "",
            "font_variant": "",
            "font_variations": "",
            "font_weight": "",
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
        assert dut.datatype is None
        assert dut.default is None
        assert dut.edit_signal == ""
        assert dut.field == ""
        assert dut.font_allow_breaks == ""
        assert dut.font_bgalpha == ""
        assert dut.font_bgcolor == ""
        assert dut.font_family == ""
        assert dut.font_features == ""
        assert dut.font_fgalpha == ""
        assert dut.font_fgcolor == ""
        assert dut.font_gravity == ""
        assert dut.font_gravity_hint == ""
        assert dut.font_insert_hyphens == ""
        assert dut.font_lang == ""
        assert dut.font_letter_spacing == ""
        assert dut.font_overline == ""
        assert dut.font_overline_color == ""
        assert dut.font_rise == ""
        assert dut.font_scale == ""
        assert dut.font_size == ""
        assert dut.font_stretch == ""
        assert dut.font_strikethrough == ""
        assert dut.font_strikethrough_color == ""
        assert dut.font_style == ""
        assert dut.font_underline == ""
        assert dut.font_underline_color == ""
        assert dut.font_variant == ""
        assert dut.font_variations == ""
        assert dut.font_weight == ""
        assert dut.format == "{}"
        assert dut.index == -1
        assert dut.listen_topic == "listen_topic"
        assert dut.parent_id == -1
        assert dut.record_id == -1
        assert dut.send_topic == "send_topic"

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = DataWidgetMixin()

        assert dut.do_get_attribute("datatype") is None
        assert dut.do_get_attribute("default") is None
        assert dut.do_get_attribute("edit_signal") == ""
        assert dut.do_get_attribute("field") == ""
        assert dut.do_get_attribute("font_allow_breaks") == ""
        assert dut.do_get_attribute("font_bgalpha") == ""
        assert dut.do_get_attribute("font_bgcolor") == ""
        assert dut.do_get_attribute("font_family") == ""
        assert dut.do_get_attribute("font_features") == ""
        assert dut.do_get_attribute("font_fgalpha") == ""
        assert dut.do_get_attribute("font_fgcolor") == ""
        assert dut.do_get_attribute("font_gravity") == ""
        assert dut.do_get_attribute("font_gravity_hint") == ""
        assert dut.do_get_attribute("font_insert_hyphens") == ""
        assert dut.do_get_attribute("font_lang") == ""
        assert dut.do_get_attribute("font_letter_spacing") == ""
        assert dut.do_get_attribute("font_overline") == ""
        assert dut.do_get_attribute("font_overline_color") == ""
        assert dut.do_get_attribute("font_rise") == ""
        assert dut.do_get_attribute("font_scale") == ""
        assert dut.do_get_attribute("font_size") == ""
        assert dut.do_get_attribute("font_stretch") == ""
        assert dut.do_get_attribute("font_strikethrough") == ""
        assert dut.do_get_attribute("font_strikethrough_color") == ""
        assert dut.do_get_attribute("font_style") == ""
        assert dut.do_get_attribute("font_underline") == ""
        assert dut.do_get_attribute("font_underline_color") == ""
        assert dut.do_get_attribute("font_variant") == ""
        assert dut.do_get_attribute("font_variations") == ""
        assert dut.do_get_attribute("font_weight") == ""
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
        DataWidgetAttributes.
        """
        dut = DataWidgetMixin()
        dut.do_set_attributes(DataWidgetAttributes())

        assert dut.datatype is None
        assert dut.default is None
        assert dut.edit_signal == ""
        assert dut.field == ""
        assert dut.font_allow_breaks == ""
        assert dut.font_bgalpha == ""
        assert dut.font_bgcolor == ""
        assert dut.font_family == ""
        assert dut.font_features == ""
        assert dut.font_fgalpha == ""
        assert dut.font_fgcolor == ""
        assert dut.font_gravity == ""
        assert dut.font_gravity_hint == ""
        assert dut.font_insert_hyphens == ""
        assert dut.font_lang == ""
        assert dut.font_letter_spacing == ""
        assert dut.font_overline == ""
        assert dut.font_overline_color == ""
        assert dut.font_rise == ""
        assert dut.font_scale == ""
        assert dut.font_size == ""
        assert dut.font_stretch == ""
        assert dut.font_strikethrough == ""
        assert dut.font_strikethrough_color == ""
        assert dut.font_style == ""
        assert dut.font_underline == ""
        assert dut.font_underline_color == ""
        assert dut.font_variant == ""
        assert dut.font_variations == ""
        assert dut.font_weight == ""
        assert dut.format == "{}"
        assert dut.index == -1
        assert dut.listen_topic == "listen_topic"
        assert dut.parent_id == -1
        assert dut.record_id == -1
        assert dut.send_topic == "send_topic"

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
                font_family="Arial",
                font_weight="Bold",
                index=10,
            )
        )

        assert dut.datatype == "str"
        assert dut.default == "Default Text"
        assert dut.edit_signal == "test_signal"
        assert dut.field == "test_field"
        assert dut.font_allow_breaks == ""
        assert dut.font_bgalpha == ""
        assert dut.font_bgcolor == ""
        assert dut.font_family == "Arial"
        assert dut.font_features == ""
        assert dut.font_fgalpha == ""
        assert dut.font_fgcolor == ""
        assert dut.font_gravity == ""
        assert dut.font_gravity_hint == ""
        assert dut.font_insert_hyphens == ""
        assert dut.font_lang == ""
        assert dut.font_letter_spacing == ""
        assert dut.font_overline == ""
        assert dut.font_overline_color == ""
        assert dut.font_rise == ""
        assert dut.font_scale == ""
        assert dut.font_size == ""
        assert dut.font_stretch == ""
        assert dut.font_strikethrough == ""
        assert dut.font_strikethrough_color == ""
        assert dut.font_style == ""
        assert dut.font_underline == ""
        assert dut.font_underline_color == ""
        assert dut.font_variant == ""
        assert dut.font_variations == ""
        assert dut.font_weight == "Bold"
        assert dut.format == "{}"
        assert dut.index == 10
        assert dut.listen_topic == "listen_topic"
        assert dut.parent_id == -1
        assert dut.record_id == -1
        assert dut.send_topic == "send_topic"
