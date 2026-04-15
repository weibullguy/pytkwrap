#
#       pytkwrap.gtk3.plotview.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 PlotView module."""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.common import PlotWidgetAttributes, PlotWidgetMixin
from pytkwrap.gtk3._libs import Gdk, Gtk, _
from pytkwrap.gtk3.widget import GTK3BaseWidget


try:
    # Third Party Imports
    from matplotlib.backend_bases import MouseEvent
    from matplotlib.backends.backend_gtk3cairo import (
        FigureCanvasGTK3Cairo as FigureCanvas,
    )
    from matplotlib.figure import Figure
    from matplotlib.lines import Line2D
except RuntimeError:
    # This is necessary to have the tests pass on headless servers.
    pass


class GTK3PlotView(Gtk.HBox, GTK3BaseWidget, PlotWidgetMixin):
    """The GTK3PlotView class."""

    _GTK3_PLOTVIEW_ATTRIBUTES = PlotWidgetAttributes(
        axis=None,
        canvas=None,
        figure=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3PlotView widget."""
        Gtk.HBox.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        GTK3BaseWidget.__init__(self)
        PlotWidgetMixin.__init__(self)

        # Initialize private instance attributes.
        self._max_values: list[float] = []
        self._min_values: list[float] = [0.0]

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_PLOTVIEW_ATTRIBUTES)

        self.figure: Figure = Figure()
        self.canvas: FigureCanvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)

        self.pack_start(self.canvas, True, True, 0)

    # ----- ----- PlotView specific methods. ----- ----- #
    def do_load_plot(
        self,
        x_values: list[float],
        y_values: list[float],
        marker: str = "o",
        plot_type: str = "scatter",
    ) -> None:
        """Load the GTK3PlotView.

        Pass the keyword plot_type to select.  Markers can be set using the marker
        keyword.  The default marker is 'g-' or a solid green line.  See matplotlib
        documentation for other options.

        Parameters
        ----------
        x_values : list
            The list of the x-values to plot.
        y_values : list
            The list of the y-values to plot or list of bin edges if plotting a
            histogram.
        marker : str
            The marker style for the plot.
        plot_type : str
            The type of plot to produce. Options are 'date', 'histogram', 'scatter'
            (default), and 'step'.
        """
        if not y_values:
            return

        if plot_type == "step":
            self._do_make_step_plot(x_values, y_values, marker)
        elif plot_type == "scatter":
            self._do_make_scatter_plot(x_values, y_values, marker)
        elif plot_type == "histogram":
            self._do_make_histogram(x_values, y_values, marker)
        elif plot_type == "date":
            self._do_make_date_plot(x_values, y_values, marker)
        else:
            return

        _min, _max = self._get_minimax_ordinates()

        self.axis.set_ybound(_min, 1.05 * _max)

        self.canvas.show()

    def do_add_line(
        self,
        x_values: list[float],
        y_values: list[float] | None = None,
        color: str = "k",
        marker: str = "^",
    ) -> None:
        """Add a line to the GTK3PlotView.

        Parameters
        ----------
        x_values: list
            The list of the x-values to plot.
        y_values : list
            The list of the y-values to plot or list of bin edges if plotting a
            histogram.
        color : str
            The color of the line to add to the plot. Black is the default.  See
            matplotlib documentation for options.
        marker : str
            The marker to use on the plot. Default is '^' or an upward pointing
            triangle. See matplotlib documentation for other options.
        """
        _line = Line2D(
            x_values,
            y_values,
            lw=0.0,
            color=color,
            marker=marker,
            markersize=10,
        )
        self.axis.add_line(_line)

    def do_close_plot(
        self, __window: Gtk.Window, __event: Gdk.Event, parent: Gtk.Widget
    ) -> None:
        """Return the plot to the parent widget it is part of.

        Parameters
        ----------
        __window : Gtk.Window
            The Gtk.Window that is being destroyed.
        __event : Gdk.Event
            The Gdk.Event that called this method.
        parent : Gtk.Widget
            The original parent Gtk.Widget for the plot.
        """
        self.canvas.reparent(parent)

    def do_expand_plot(self, event: MouseEvent) -> None:
        """Display a GTK3PlotView in its own window.

        Parameters
        ----------
        event : matplotlib.backend_bases.MouseEvent
            The matplotlib.backend_bases.MouseEvent that called this method.
        """
        self.canvas = event.canvas
        _parent = self.canvas.get_parent()

        if event.button == MouseEvent.RIGHT:  # pylint: disable=no-member
            _window = Gtk.Window()
            _window.set_skip_pager_hint(True)
            _window.set_skip_taskbar_hint(True)
            _window.set_default_size(800, 400)
            _window.set_border_width(5)
            _window.set_position(Gtk.WindowPosition.NONE)
            _window.set_title(_(" Plot"))

            _window.connect("delete_event", self.do_close_plot, _parent)

            self.canvas.reparent(_window)

            _window.show_all()

    def _do_make_date_plot(
        self,
        x_values: list[float],
        y_values: list[float],
        marker: str = "g-",
    ) -> None:
        """Make a date plot.

        Parameters
        ----------
        x_values : list
            The list of x-values (dates) for the plot.
        y_values : list
            The list of y-values for the plot.
        marker : str
            The type and color of marker to use for the plot. Default is 'g-' or a
            solid green line.
        """
        self.axis.xaxis_date()
        self.axis.plot(x_values, y_values, marker, linewidth=2)
        self._min_values.append(min(y_values))
        self._max_values.append(max(y_values))

    def _do_make_histogram(
        self,
        x_values: list[float],
        y_values: list[float],
        marker: str = "g",
    ) -> None:
        """Make a histogram.

        Parameters
        ----------
        x_values: list
            The list of x-values for the plot.
        y_values: list
            The list of bin edges for the plot.
        marker : str
            Type and color of marker to use for the plot. Default is 'g' or solid green.
        """
        self.axis.grid(False, which="both")
        _values, _edges, __ = self.axis.hist(x_values, bins=y_values, color=marker)
        self._min_values.append(min(_values))
        self._max_values.append(max(_values) + 1)

    def _do_make_scatter_plot(
        self,
        x_values: list[float],
        y_values: list[float],
        marker: str = "go",
    ) -> None:
        """Make a scatter plot.

        Parameters
        ----------
        x_values: list
            The list of x-values for the plot.
        y_values: list
            The list of y-values for the plot.
        marker : str
            Type and color of marker to use for the plot. Default is 'go' or open green
             circles.
        """
        _paths = self.axis.scatter(x_values, y_values, marker=marker, linewidth=2)
        self._min_values.append(min(y_values))
        self._max_values.append(max(y_values))

    def _do_make_step_plot(
        self,
        x_values: list[float],
        y_values: list[float],
        marker: str = "g-",
    ) -> None:
        """Make a step plot.

        Parameters
        ----------
        x_values : list
            The list of x-values for the plot.
        y_values : list
            The list of y-values for the plot.
        marker : str
            Type and color of marker to use for the plot. Default is 'g-' or a solid
            green line.
        """
        (_line,) = self.axis.step(x_values, y_values, marker, where="mid")
        _line.set_ydata(y_values)
        self._min_values.append(min(y_values))
        self._max_values.append(max(y_values))

    def _get_minimax_ordinates(self) -> tuple[float, float]:
        """Get minimum and maximum y-values to set the axis bounds.

        If the maximum value is infinity, use the next largest value and so forth.

        Returns
        -------
        _min, _max : tuple
            The minimum and maximum ordinate values.
        """
        _min: float = min(self._min_values)
        _max: float = max(1.0, self._max_values[0])
        for i in range(1, len(self._max_values)):
            if _max < self._max_values[i] != float("inf"):
                _max = self._max_values[i]

        return _min, _max
