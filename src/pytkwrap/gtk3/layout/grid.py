"""The pytkwrap GTK3Grid module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping, Sequence

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3GridMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Grid.

    Attributes
    ----------
    _GTK3_GRID_ATTRIBUTES : dict
        Attributes specific to GTK3Grid and their default values.
    _GTK3_GRID_PROPERTIES : GTK3WidgetProperties
        Properties specific to GTK3Grid and their default values.

    Notes
    -----
    GTK3Grid passes no widgets to its callback function.
    """

    _GTK3_GRID_ATTRIBUTES = {"n_columns": 1, "n_rows": 1}
    _GTK3_GRID_PROPERTIES = GTK3WidgetProperties(
        baseline_row=0,
        column_homogeneous=False,
        column_spacing=0,
        row_homogeneous=False,
        row_spacing=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Grid mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_GRID_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_GRID_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Grid-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Grid.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_baseline_row(self.dic_properties["baseline_row"])
        self.set_column_homogeneous(self.dic_properties["column_homogeneous"])
        self.set_column_spacing(self.dic_properties["column_spacing"])
        self.set_row_homogeneous(self.dic_properties["row_homogeneous"])
        self.set_row_spacing(self.dic_properties["row_spacing"])

    def do_build_grid(
        self,
        columns: Sequence[int] | None = None,
        rows: Sequence[int] | None = None,
        siblings: Sequence[Gtk.Widget] | None = None,
        sides: Sequence[Sequence[Gtk.PositionType]] | None = None,
    ) -> None:
        """Build the GTK3Grid.

        Parameters
        ----------
        columns : Sequence[int] | None, optional
            A list or tuple of the positions to add a column to the GTK3Grid.
        rows : Sequence[int] | None, optional
            A list or tuple of the positions to add a row to the GTK3Grid.
        siblings : Sequence[Gtk.Widget] | None, optional
            The list or tuple of widgets already in the GTK3Grid that the new widgets
            will be placed next to.
        sides : Sequence[Gtk.PositionType] | None, optional
            The list or tuple of positions the new widgets will occupy next its sibling
            widget.  These would be Gtk.PositionType.LEFT, Gtk.PositionType.RIGHT,
            Gtk.PositionType.TOP, or Gtk.PositionType.BOTTOM.
        """
        if siblings is not None and sides is not None:
            return self._build_grid_with_siblings_and_sides(siblings, sides)

        return self._build_grid_with_column_row_count(columns, rows)

    def do_populate_grid(
        self,
        widgets: Sequence[Gtk.Widget],
        positions: Sequence[Sequence[int]],
        sizes: Sequence[Sequence[int]],
        siblings: Sequence[Gtk.Widget] | None = None,
        sides: Sequence[Gtk.PositionType] | None = None,
    ) -> None:
        """Populate the GTK3Grid with the given widgets.

        Parameters
        ----------
        widgets : Sequence[Gtk.Widget]
            The list or tuple of widgets to add to the GTK3Grid.
        positions : Sequence[Sequence[int]]
            A list or tuple of the [left, top] or (left, top) positions to add each
            widget to the GTK3Grid.
        sizes : Sequence[Sequence[int]]
            A list or tuple of the [width, height] or (width, height) for each widget
            where width is the number of columns the widget will span and the height is
            the number of rows the widget will span.  Passing an empty list will
            cause each widget to span one column and one row.
        siblings : Sequence[Gtk.Widget] | None, optional
            The list or tuple of widgets already in the GTK3Grid that the new widgets
            will be placed next to.
        sides : Sequence[Gtk.PositionType] | None, optional
            The list or tuple of positions the new widgets will occupy next its sibling
            widget.  These would be Gtk.PositionType.LEFT, Gtk.PositionType.RIGHT,
            Gtk.PositionType.TOP, or Gtk.PositionType.BOTTOM.
        """
        for _idx, _widget in enumerate(widgets):
            # By default, the widget will span one column and one row.
            try:
                _width = sizes[_idx][0]
                _height = sizes[_idx][1]
            except IndexError:
                _width = 1
                _height = 1

            if siblings is not None and sides is not None:
                self.attach_next_to(
                    _widget,
                    siblings[_idx],
                    sides[_idx],
                    _width,
                    _height,
                )
            else:
                self.attach(
                    _widget,
                    positions[_idx][0],
                    positions[_idx][1],
                    _width,
                    _height,
                )

    def _build_grid_with_column_row_count(
        self,
        columns: Sequence[int] | None,
        rows: Sequence[int] | None,
    ) -> None:
        """Build the GTK3Grid with the given number of columns and rows.

        Parameters
        ----------
        columns : Sequence[int] | None, optional
            A list or tuple of the positions to add a column to the GTK3Grid.
        rows : Sequence[int] | None, optional
            A list or tuple of the positions to add a row to the GTK3Grid.
        """
        if columns is not None:
            for _column in columns:
                self.insert_column(_column)
                self.dic_attributes["n_columns"] += 1

        if rows is not None:
            for _row in rows:
                self.insert_row(_row)
                self.dic_attributes["n_rows"] += 1

    def _build_grid_with_siblings_and_sides(
        self,
        siblings: Sequence[Gtk.Widget],
        sides: Sequence[Sequence[Gtk.PositionType]],
    ) -> None:
        """Build the GTK3Grid with the given siblings and sides.

        Parameters
        ----------
        siblings : Sequence[Gtk.Widget]
            The list or tuple of widgets already in the GTK3Grid that the new widgets
            will be placed next to.
        sides : Sequence[Sequence[Gtk.PositionType]]
            The list or tuple of positions the new columns or rows will occupy next its
            sibling widget.  These would be Gtk.PositionType.LEFT,
            Gtk.PositionType.RIGHT, Gtk.PositionType.TOP, or Gtk.PositionType.BOTTOM.
        """
        for _idx, _sibling in enumerate(siblings):
            for _side in sides[_idx]:
                self.insert_next_to(_sibling, _side)

                if _side in {Gtk.PositionType.TOP, Gtk.PositionType.BOTTOM}:
                    self.dic_attributes["n_rows"] += 1
                else:
                    self.dic_attributes["n_columns"] += 1


class GTK3Grid(Gtk.Grid, GTK3GridMixin):
    """Wrapper for version 3.0 Gtk.Grid."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Grid."""
        Gtk.Grid.__init__(self)
        GTK3GridMixin.__init__(self)
