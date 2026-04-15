#       pytkwrap.gtk3.matrixview.py is part of the  Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 MatrixView module."""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.buttons import GTK3CheckButton  # , GTK3SpinButton
from pytkwrap.gtk3.combo import GTK3ComboBox
from pytkwrap.gtk3.entry import GTK3Entry
from pytkwrap.gtk3.label import GTK3Label
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.textview import GTK3TextView
from pytkwrap.gtk3.widget import GTK3BaseDataWidget, GTK3WidgetProperties


class GTK3MatrixView(Gtk.Grid, GTK3BaseDataWidget):
    """The GTK3MatrixView class."""

    _GTK3_MATRIXVIEW_PROPERTIES = GTK3WidgetProperties(
        baseline_row=0,
        column_homogeneous=False,
        column_spacing=0,
        row_homogeneous=False,
        row_spacing=0,
    )
    _GTK3_MATRIXVIEW_SIGNALS = [
        "add",
        "check-resize",
        "remove",
        "set-focus-child",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MatrixView widget."""
        Gtk.Grid.__init__(self)
        GTK3BaseDataWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_MATRIXVIEW_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_MATRIXVIEW_SIGNALS
        })
        self.n_columns: int = 0
        self.n_rows: int = 0

        self.show()

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3MatrixView.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3MatrixView.
        """
        super().do_set_properties(properties)

        self.set_baseline_row(self.dic_properties["baseline_row"])
        self.set_column_homogeneous(self.dic_properties["column_homogeneous"])
        self.set_column_spacing(self.dic_properties["column_spacing"])
        self.set_row_homogeneous(self.dic_properties["row_homogeneous"])
        self.set_row_spacing(self.dic_properties["row_spacing"])

    # ----- ----- MatrixView specific methods ----- ----- #
    def do_add_column(self, position: int) -> None:
        """Add a column to the GTK3MatrixView at position.

        Parameters
        ----------
        position : int
            The position in the GTK3MatrixView to add the column.
        """
        self.insert_column(position)
        self.n_columns += 1

    def do_add_label(
        self,
        angle: float,
        heading: str,
        height: int,
        position: tuple[int, int],
        tooltip: str,
        width: int,
    ) -> None:
        """Add either a column or row label to the GTK3MatrixView.

        Parameters
        ----------
        angle : float
            The angle to rotate the label in degrees.
        heading : str
            The text to display as the heading for the new column/row.
        height : int
            The number of rows for the label to span.
        position : tuple
            The column number and row number to attach the left side and top side
            respectively of new widgets to.
        tooltip : str
            The tooltip for the new column's/row's header widget.
        width : int
            The number of columns for the label to span.
        """
        _label = GTK3Label(heading)
        _label.do_set_attributes(
            GTK3DataWidgetAttributes(
                font_weight="bold",
            )
        )
        _label.do_set_properties(
            GTK3WidgetProperties(
                angle=angle,
                can_focus=False,
                label=heading,
                tooltip_markup=tooltip,
                tooltip_text=tooltip,
                wrap=False,
            ),
        )
        _label.do_set_font_description()

        self.attach(
            _label,
            position[0],
            position[1],
            width,
            height,
        )

    def do_add_row(self, position: int) -> None:
        """Add a row to the GTK3MatrixView at position.

        Parameters
        ----------
        position : int
            The position in the GTK3MatrixView to add the row.
        """
        self.insert_row(position)
        self.n_rows += 1

    # TODO: Add the spinbutton to this method once their classes are written.
    def do_add_widget(
        self,
        widget: GTK3CheckButton | GTK3ComboBox | GTK3Entry | GTK3Label | GTK3TextView,
        left: int,
        top: int,
        height: int,
        width: int,
    ):
        """Add an interactive widget to the GTK3MatrixView.

        Interactive widgets can be one of:

        * GTK3Checkbutton
        * GTK3ComboBox
        * GTK3Entry
        * GTK3Label
        * GTK3SpinButton
        * GTK3TextView

        Parameters
        ----------
        height : int
            The number of rows the widget spans.
        left : int
            The column the left side of the widget should attach to.
        top : int
            The row the top of the widget should attach to.
        width : int
            The number of columns the widget spans.
        widget : GTK3CheckButton or GTK3ComboBox or GTK3Entry or GTK3Label or
        GTK3SpinButton or GTK3TextView
            The data widget to attach.
        """
        self.attach(widget, left, top, width, height)

    def do_build_matrix(
        self,
        column_names: list[tuple[str, str]],
        row_names: list[tuple[str, str]],
    ) -> None:
        """Build an M row x N column matrix.

        Parameters
        ----------
        column_names : list
            A list of tuples with the name and description of the items to use as the
            column headings and the tooltips.
        row_names : list
            A list of tuples with the name and description of the items to use as the
            row headings and the tooltips.
        """
        self.do_set_column_headings(column_names)
        self.do_set_row_headings(row_names)

    # TODO: Add the spinbutton to this method once their classes are written.
    def do_get_widget(
        self,
        column: int,
        row: int,
    ) -> GTK3CheckButton | GTK3ComboBox | GTK3Entry | GTK3Label | GTK3TextView | None:
        """Get the interactive widget at column/row.

        Parameters
        ----------
        column : int
            The index of the column in the GTK3MatrixView to retrieve the widget.
        row : int
            The index of the row in the GTK3MatrixView to retrieve the widget.

        Returns
        -------
        GTK3CheckButton or GTK3Combobox or GTK3Entry or GTK3Label or
        GTK3SpinButton or GTK3TextView or None
            The widget at the column/row intersection in the GTK3MatrixView or None.
        """
        return self.get_child_at(column, row)

    def do_remove_column(self, position: int) -> None:
        """Remove the GTK3MatrixView column at position.

        Parameters
        ----------
        position : int
            The column position to remove.
        """
        self.remove_column(position)
        self.n_columns -= 1

    def do_remove_row(self, position: int) -> None:
        """Remove the GTK3MatrixView row at position.

        Parameters
        ----------
        position : int
            The row position to remove.
        """
        self.remove_row(position)
        self.n_rows -= 1

    def do_set_column_headings(
        self,
        column_names: list[tuple[str, str]],
    ) -> None:
        """Load the GTK3MatrixView column headings for each column.

        A row of data in a matrix is a tuple with the first element being the column
        heading and the second element being the tooltip for that column heading.

        Parameters
        ----------
        column_names : list
            A list of tuples with the items to use as the column heading and the
            tooltip.
        """
        for _column_name in column_names:
            self.do_add_column(self.n_columns + 1)
            self.do_add_label(
                90.0,
                _column_name[0],
                1,
                (self.n_columns, 0),
                _column_name[1],
                1,
            )

    def do_set_row_headings(
        self,
        row_names: list[tuple[str, str]],
    ) -> None:
        """Load the GTK3MatrixView row headings for each row.

        A row of data in a matrix is a tuple with the first element being the row
        heading and the second element being the tooltip for that row heading.

        Parameters
        ----------
        row_names : list
            A list of tuples with the items to use as the row heading and the tooltip.
        """
        for _row_name in row_names:
            self.do_add_row(self.n_rows + 1)
            self.do_add_label(
                0.0,
                _row_name[0],
                1,
                (0, self.n_rows),
                _row_name[1],
                1,
            )


# Register the new widget types.
GObject.type_register(GTK3MatrixView)
