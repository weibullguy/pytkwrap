"""Test class for the PlotWidgetMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from matplotlib.axes import Axes
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo
from matplotlib.figure import Figure

# pytkwrap Package Imports
from pytkwrap.common.mixins import PlotWidgetAttributes, PlotWidgetMixin


@pytest.mark.order(3)
class TestPlotWidgetMixin:
    """Test class for the PlotWidgetMixin class."""

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-016")
    @pytest.mark.requirement("PTW-COM-X-017")
    @pytest.mark.requirement("PTW-COM-X-020")
    def test_init(self):
        """Should create an instance of the PlotWidgetMixin class."""
        dut = PlotWidgetMixin()

        assert dut._PLOT_WIDGET_ATTRIBUTES == {
            "axis": None,
            "canvas": None,
            "figure": None,
        }
        assert dut.dic_attributes == {
            "axis": None,
            "canvas": None,
            "data_type": None,
            "default_value": None,
            "edit_signal": "",
            "figure": None,
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
        assert dut.dic_attributes["axis"] is None
        assert dut.dic_attributes["canvas"] is None
        assert dut.dic_attributes["figure"] is None

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-018")
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = PlotWidgetMixin()

        assert dut.do_get_attribute("axis") is None
        assert dut.do_get_attribute("canvas") is None
        assert dut.do_get_attribute("figure") is None

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-018")
    @pytest.mark.requirement("PTW-COM-X-022")
    def test_do_get_attribute_delegates(self):
        """Should return the super() class value of the passed attribute name."""
        dut = PlotWidgetMixin()

        # These come from DataWidgetMixin.
        assert dut.do_get_attribute("data_type") is None
        assert dut.do_get_attribute("default_value") is None
        assert dut.do_get_attribute("edit_signal") == ""
        assert dut.do_get_attribute("font_description") is None
        assert dut.do_get_attribute("format") == "{}"
        assert dut.do_get_attribute("index") == -1
        assert dut.do_get_attribute("listen_topic") == "listen_topic"
        assert dut.do_get_attribute("send_topic") == "send_topic"

        # These come from WidgetMixin.
        assert dut.do_get_attribute("n_columns") == 0
        assert dut.do_get_attribute("n_rows") == 0
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-018")
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed an unknown attribute."""
        dut = PlotWidgetMixin()

        with pytest.raises(KeyError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-019")
    def test_do_set_attributes(self):
        """Should set attributes to the values in the PlotWidgetAttributes passed in."""
        _figure = Figure()
        _canvas = FigureCanvasGTK3Cairo(_figure)
        _axis = _figure.add_subplot(111)

        dut = PlotWidgetMixin()
        dut.do_set_attributes(
            PlotWidgetAttributes(
                axis=_axis,
                canvas=_canvas,
                figure=_figure,
            )
        )

        assert isinstance(dut.dic_attributes["axis"], Axes)
        assert isinstance(dut.dic_attributes["canvas"], FigureCanvasGTK3Cairo)
        assert isinstance(dut.dic_attributes["figure"], Figure)

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-019")
    @pytest.mark.requirement("PTW-COM-X-021")
    def test_do_set_attributes_calls_super(self):
        """Should call super().do_set_attributes()."""
        _figure = Figure()
        _canvas = FigureCanvasGTK3Cairo(_figure)
        _axis = _figure.add_subplot(111)

        dut = PlotWidgetMixin()
        dut.do_set_attributes(
            PlotWidgetAttributes(
                axis=_axis,
                canvas=_canvas,
                figure=_figure,
                edit_signal="new_signal",
                listen_topic="new_topic",
                n_columns=2,
                n_rows=2,
                x_pos=10,
                y_pos=22,
            )
        )

        assert isinstance(dut.dic_attributes["axis"], Axes)
        assert isinstance(dut.dic_attributes["canvas"], FigureCanvasGTK3Cairo)
        assert isinstance(dut.dic_attributes["figure"], Figure)
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
        """_PLOT_WIDGET_ATTRIBUTES should not be mutated by do_set_attributes()."""
        _original = dict(PlotWidgetMixin._PLOT_WIDGET_ATTRIBUTES)
        dut = PlotWidgetMixin()
        dut.do_set_attributes(PlotWidgetAttributes(index=99))

        assert PlotWidgetMixin._PLOT_WIDGET_ATTRIBUTES == _original

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-024")
    def test_dic_attributes_is_sole_store(self):
        """PlotWidgetMixin should not store attribute values outside dic_attributes."""
        dut = PlotWidgetMixin()

        _instance_attrs = set(vars(dut).keys())
        _expected = {"dic_attributes", "dic_error_message"}

        assert _instance_attrs == _expected
