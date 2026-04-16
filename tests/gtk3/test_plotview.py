# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_plotview.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3PlotView module algorithms and models."""

# Third Party Imports
import matplotlib
import pytest
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo
from matplotlib.figure import Figure

# pytkwrap Package Imports
from pytkwrap.gtk3.plotview import GTK3PlotView

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests


class TestPlotView(BaseGTK3DataWidgetTests):
    """Test class for the GTK3PlotView."""

    widget_class = GTK3PlotView
    expected_default_height = -1
    expected_default_value = None
    expected_default_width = -1

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3PlotView object."""
        super().test_init()

        dut = self.make_dut()

        # PlotView-specific attributes should be registered.
        for _attribute in GTK3PlotView._GTK3_PLOTVIEW_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        assert isinstance(dut, GTK3PlotView)
        assert isinstance(dut.figure, Figure)
        assert isinstance(dut.canvas, FigureCanvasGTK3Cairo)
        assert dut._max_values == []
        assert dut._min_values == [0.0]

    @pytest.mark.unit
    def test_do_make_date_plot(self):
        """Should create a date plot when passed a plot_type of date."""
        dut = self.make_dut()

        _x_values = [
            matplotlib.dates.datestr2num("20190701"),
            matplotlib.dates.datestr2num("20190715"),
            matplotlib.dates.datestr2num("20190801"),
            matplotlib.dates.datestr2num("20190815"),
        ]
        _y_values = [100.0, 90.0, 75.0, 50.0]

        assert dut.do_load_plot(_x_values, _y_values, plot_type="date") is None
        assert dut._min_values == [0.0, 50.0]
        assert dut._max_values == [100.0]

    @pytest.mark.unit
    def test_do_make_histogram(self):
        """Should create a histogram when passed a plot_type of histogram."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9, 1.3, 3.2, 3.4, 2.6]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        assert (
            dut.do_load_plot(_x_values, _y_values, plot_type="histogram", marker="r")
            is None
        )
        assert dut._min_values == [0.0, 2.0]
        assert dut._max_values == [4.0]

    @pytest.mark.unit
    def test_do_make_scatter_plot(self):
        """Should create a scatter plot when passed a plot_type of scatter."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        assert (
            dut.do_load_plot(_x_values, _y_values, plot_type="scatter", marker=".")
            is None
        )
        assert dut._min_values == [0.0, 1.0]
        assert dut._max_values == [4.0]

    @pytest.mark.unit
    def test_do_make_step_plot(self):
        """Should create a step plot when passed a plot_type of step."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        assert dut.do_load_plot(_x_values, _y_values, plot_type="step") is None
        assert dut._min_values == [0.0, 1.0]
        assert dut._max_values == [4.0]

    @pytest.mark.unit
    def test_do_make_default_plot(self):
        """Should create a scatter plot when not passed a plot_type."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        assert dut.do_load_plot(_x_values, _y_values) is None
        assert dut._min_values == [0.0, 1.0]
        assert dut._max_values == [4.0]

    @pytest.mark.unit
    def test_do_make_plot_no_y_data(self):
        """Should not create a plot when passed an empty y-value list."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9]
        _y_values = []

        assert dut.do_load_plot(_x_values, _y_values) is None
        assert dut._min_values == [0.0]
        assert dut._max_values == []

    @pytest.mark.unit
    def test_do_make_plot_unknown_type(self):
        """Should NOT create a plot when passed an unknown plot_type."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        assert dut.do_load_plot(_x_values, _y_values, plot_type="crackhead") is None
        assert dut._min_values == [0.0]
        assert dut._max_values == []

    @pytest.mark.unit
    def test_do_add_line_to_scatter_plot(self):
        """Should add a line to a scatter plot."""
        dut = self.make_dut()

        _x_values = [1.4, 1.2, 2.8, 4.9]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        dut.do_load_plot(_x_values, _y_values, plot_type="scatter", marker="v")

        _x_values = [2.3, 3.2, 4.8, 5.9]
        _y_values = [1.0, 2.0, 3.0, 4.0]

        assert dut.do_add_line(_x_values, _y_values) is None

    @pytest.mark.unit
    def test_get_minimax_ordinates(self):
        """Should return a tuple (min_value, max_value)."""
        dut = self.make_dut()

        dut._min_values = [0.0, 1.0]
        dut._max_values = [1.4, 4.0]
        _min, _max = dut._get_minimax_ordinates()

        assert _min == 0.0
        assert _max == 4.0

    @pytest.mark.unit
    def test_get_minimax_ordinates_inf_y(self):
        """Should return a tuple (min_value, max_value)."""
        dut = self.make_dut()

        dut._min_values = [0.0, 1.0, 3.2]
        dut._max_values = [1.4, 4.0, float("inf")]
        _min, _max = dut._get_minimax_ordinates()

        assert _min == 0.0
        assert _max == 4.0
