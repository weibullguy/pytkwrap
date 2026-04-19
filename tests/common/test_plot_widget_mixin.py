# pylint: skip-file
# type: ignore
#
#       tests.common.test_plot_widget_mixin.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the PlotWidgetMixin class."""

# Third Party Imports
import pytest
from matplotlib.axes import Axes
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo
from matplotlib.figure import Figure

# pytkwrap Package Imports
from pytkwrap.common.mixins import PlotWidgetAttributes, PlotWidgetMixin


@pytest.mark.order(2)
class TestPlotWidgetMixin:
    """Test class for the PlotWidgetMixin class."""

    @pytest.mark.unit
    def test_init(self):
        """Should create an instance of the WidgetMixin class."""
        dut = PlotWidgetMixin()

        assert dut._PLOT_WIDGET_ATTRIBUTES == {
            "axis": None,
            "canvas": None,
            "figure": None,
        }
        assert dut.dic_attributes == {
            "axis": None,
            "canvas": None,
            "datatype": None,
            "default": None,
            "edit_signal": "",
            "field": "",
            "figure": None,
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
        assert dut.dic_attributes["axis"] is None
        assert dut.dic_attributes["canvas"] is None
        assert dut.dic_attributes["figure"] is None

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should return the value of the passed attribute name."""
        dut = PlotWidgetMixin()

        assert dut.do_get_attribute("axis") is None
        assert dut.do_get_attribute("canvas") is None
        assert dut.do_get_attribute("figure") is None
        assert dut.do_get_attribute("x_pos") == 0
        assert dut.do_get_attribute("y_pos") == 0

    @pytest.mark.unit
    def test_do_get_attribute_unknown(self):
        """Should raise a KeyError when passed an unknown attribute."""
        dut = PlotWidgetMixin()

        with pytest.raises(KeyError):
            dut.do_get_attribute("unk_attribute")

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Set default attribute values when passed an empty PlotWidgetAttributes."""
        dut = PlotWidgetMixin()
        dut.do_set_attributes(PlotWidgetAttributes())

        assert dut.dic_attributes["axis"] is None
        assert dut.dic_attributes["canvas"] is None
        assert dut.dic_attributes["figure"] is None
        assert dut.dic_attributes["x_pos"] == 0
        assert dut.dic_attributes["y_pos"] == 0

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values in the WidgetAttributes passed in."""
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
