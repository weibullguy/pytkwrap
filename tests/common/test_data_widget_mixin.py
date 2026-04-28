"""Test class for the DataWidgetMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.common.mixins import DataWidgetAttributes, DataWidgetMixin
from pytkwrap.utilities import FontDescription


@pytest.mark.order(2)
class TestDataWidgetMixin:
    """Test class for the DataWidgetMixin class."""

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-010")
    @pytest.mark.requirement("PTW-COM-X-011")
    @pytest.mark.requirement("PTW-COM-X-012")
    @pytest.mark.requirement("PTW-COM-X-015")
    @pytest.mark.requirement("PTW-COM-X-015.001")
    @pytest.mark.requirement("PTW-COM-X-020")
    def test_init(self):
        """Should create an instance of the DataWidgetMixin class."""
        dut = DataWidgetMixin()

        assert dut._DEFAULT_EDIT_SIGNAL == ""
        assert dut._DEFAULT_VALUE is None
        assert dut._DATA_WIDGET_ATTRIBUTES == {
            "data_type": None,
            "default_value": None,
            "edit_signal": "",
            "font_description": None,
            "format": "{}",
            "index": -1,
            "listen_topic": "listen_topic",
            "send_topic": "send_topic",
        }
        assert dut.dic_attributes == {
            "data_type": None,
            "default_value": None,
            "edit_signal": "",
            "font_description": None,
            "format": "{}",
            "index": -1,
            "listen_topic": "listen_topic",
            "n_columns": 0,
            "n_rows": 0,
            "send_topic": "send_topic",
            "x_pos": 0,
            "y_pos": 0,
        }

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-021")
    def test_init_calls_super(self):
        """Should initialize WidgetMixin attributes via super().__init__()."""
        dut = DataWidgetMixin()

        # These come from WidgetMixin via super().__init__()
        assert "n_columns" in dut.dic_attributes
        assert "n_rows" in dut.dic_attributes
        assert "x_pos" in dut.dic_attributes
        assert "y_pos" in dut.dic_attributes
        # These come from BaseMixin via super().__init__()
        assert dut.dic_error_message is not None

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-013")
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = DataWidgetMixin()

        assert dut.do_get_attribute("data_type") is None
        assert dut.do_get_attribute("default_value") is None
        assert dut.do_get_attribute("edit_signal") == ""
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("send_topic") == "send_topic"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-013")
    @pytest.mark.requirement("PTW-COM-X-022")
    def test_do_get_attribute_delegates(self):
        """Should return the super() class value of the passed attribute name."""
        dut = DataWidgetMixin()

        assert dut.do_get_attribute("n_columns") == 0
        assert dut.do_get_attribute("n_rows") == 0
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-013")
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed an unknown attribute."""
        dut = DataWidgetMixin()

        with pytest.raises(KeyError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_set_attributes(self):
        """Should set attributes to the values in the DataWidgetAttributes passed in."""
        dut = DataWidgetMixin()
        dut.do_set_attributes(
            DataWidgetAttributes(
                data_type=str,
                default_value="Default Text",
                edit_signal="test_signal",
                index=10,
            )
        )

        assert dut.do_get_attribute("data_type") == str
        assert dut.do_get_attribute("default_value") == "Default Text"
        assert dut.do_get_attribute("edit_signal") == "test_signal"
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == 10
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("send_topic") == "send_topic"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_set_attributes_type_coercion(self):
        """Should coerce passed in values to the correct type for the attribute."""
        dut = DataWidgetMixin()
        dut.do_set_attributes(
            DataWidgetAttributes(
                default_value=1,
                edit_signal=46,
                font_description=12.32,
                format=True,
                index="5",
                listen_topic=False,
                send_topic=88.68,
            )
        )

        assert dut.do_get_attribute("default_value") == 1  # Not coerced.
        assert dut.do_get_attribute("edit_signal") == "46"
        assert isinstance(dut.do_get_attribute("font_description"), FontDescription)
        assert dut.do_get_attribute("format") == "True"
        assert dut.do_get_attribute("index") == 5
        assert dut.do_get_attribute("listen_topic") == "False"
        assert dut.do_get_attribute("send_topic") == "88.68"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_set_attributes_partial(self):
        """Should preserve any attribute values not present in the DataWidgetAttributes
        passed in."""
        dut = DataWidgetMixin()
        dut.do_set_attributes(
            DataWidgetAttributes(
                edit_signal="new_signal",
                listen_topic="new_topic",
            )
        )

        assert dut.dic_attributes["data_type"] is None
        assert dut.dic_attributes["default_value"] is None
        assert dut.dic_attributes["edit_signal"] == "new_signal"
        assert dut.dic_attributes["font_description"] is None
        assert dut.dic_attributes["format"] == "{}"
        assert dut.dic_attributes["index"] == -1
        assert dut.dic_attributes["listen_topic"] == "new_topic"
        assert dut.dic_attributes["send_topic"] == "send_topic"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-014")
    def test_do_set_attributes_calls_super(self):
        """Should call super().do_set_attributes()."""
        dut = DataWidgetMixin()
        dut.do_set_attributes(
            DataWidgetAttributes(
                edit_signal="new_signal",
                listen_topic="new_topic",
                n_columns=2,
                n_rows=2,
                x_pos=10,
                y_pos=22,
            )
        )

        assert dut.dic_attributes["data_type"] is None
        assert dut.dic_attributes["default_value"] is None
        assert dut.dic_attributes["edit_signal"] == "new_signal"
        assert dut.dic_attributes["font_description"] is None
        assert dut.dic_attributes["format"] == "{}"
        assert dut.dic_attributes["index"] == -1
        assert dut.dic_attributes["listen_topic"] == "new_topic"
        assert dut.dic_attributes["n_columns"] == 2
        assert dut.dic_attributes["n_rows"] == 2
        assert dut.dic_attributes["send_topic"] == "send_topic"
        assert dut.dic_attributes["x_pos"] == 10
        assert dut.dic_attributes["y_pos"] == 22

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-023")
    def test_class_attributes_not_mutated(self):
        """_DATA_WIDGET_ATTRIBUTES should not be mutated by do_set_attributes()."""
        _original = dict(DataWidgetMixin._DATA_WIDGET_ATTRIBUTES)
        dut = DataWidgetMixin()
        dut.do_set_attributes(DataWidgetAttributes(index=99))

        assert DataWidgetMixin._DATA_WIDGET_ATTRIBUTES == _original

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-024")
    def test_dic_attributes_is_sole_store(self):
        """DataWidgetMixin should not store attribute values outside dic_attributes."""
        dut = DataWidgetMixin()

        _instance_attrs = set(vars(dut).keys())
        _expected = {"dic_attributes", "dic_error_message"}

        assert _instance_attrs == _expected
