"""The pytkwrap GTK3TreeModel module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetAttributes


class GTK3TreeModelMixin(GTK3GObjectMixin):
    """Mixin class for GTK3TreeModel.

    Attributes
    ----------
    _GTK3_TREEMODEL_ATTRIBUTES : GTK3WidgetAttributes
        Attributes unique to the GTK3TreeModel.
    """

    _GTK3_TREEMODEL_ATTRIBUTES = GTK3WidgetAttributes(
        column_types=None,
        n_columns=0,
        n_rows=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3TreeModel mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_TREEMODEL_ATTRIBUTES)

        self.type: str = "GTK3TreeModel"

    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested GTK3TreeModel attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool | date | float | int | str | None
            The value of the requested attribute.
        """
        if attribute in self.dic_attributes:
            return self.dic_attributes.get(attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: Mapping[str, object]) -> None:
        """Set the GTK3TreeModel attributes.

        Parameters
        ----------
        attributes : GTK3WidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        super().do_set_attributes(attributes)

        for _attr in self.dic_attributes:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

        if self.dic_attributes["column_types"] is not None:
            self.set_column_types(self.dic_attributes["column_types"])

        # Add n_rows empty rows to the GTK3ListStore.
        if self.dic_attributes["n_rows"] > 0:
            _row = 1
            while _row < self.dic_attributes["n_rows"]:
                self.append(None)
                _row += 1
        # Or clear all existing rows.
        elif self.dic_attributes["n_rows"] is None:
            self.clear()

    def do_insert_row(
        self,
        values: list[object],
        position: int | None = None,
        columns: list[int] | None = None,
        parent: Gtk.TreeIter | None = None,
        sibling: Gtk.TreeIter | None = None,
        after: bool | None = None,
    ) -> Gtk.TreeIter | None:
        """Insert a new row, optionally with values, into the GTK3ListStore.

        Parameters
        ----------
        values : list[object]
            The values to apply to the newly inserted row.
        position : int | None, optional
            The position to insert the new row.  Pass 0 to prepend the row, pass -1
            to append the row.
        columns : list[int] | None, optional
            The list of column numbers to insert the values.
        parent : Gtk.TreeIter | None, optional
            The Gtk.TreeIter that will be the parent of the newly inserted row.
        sibling : Gtk.TreeIter | None, optional
            The Gtk.TreeIter to insert the new row before or after.
        after : bool | None, optional
            Whether to insert the new row after the sibling or before it.

        Returns
        -------
        Gtk.TreeIter | None
            The Gtk.TreeIter of the newly inserted row.
        """
        if self.type == "GTK3ListStore":
            return self._insert_liststore_row(values, position, columns, sibling, after)
        return self._insert_treestore_row(
            values, position, columns, parent, sibling, after
        )

    def do_move_row(
        self,
        row: Gtk.TreeIter,
        position: Gtk.TreeIter | None,
        swap: bool = False,
        after: bool = True,
    ) -> None:
        """Move a row in the GTK3ListStore.

        Parameters
        ----------
        row : Gtk.TreeIter
            The Gtk.TreeIter representing to the row to move.
        position : Gtk.TreeIter | None
            The Gtk.TreeIter representing the row to move the iter before or after.
        swap : bool
            Indicates whether to simply swap the iter and position.
        after : bool
            Indicates whether to move the row after (default) or before the position
            passed.
        """
        if swap:
            return self.swap(row, position)

        if after:
            return self.move_after(row, position)
        return self.move_before(row, position)

    def _insert_liststore_row(
        self,
        values,
        position,
        columns,
        sibling,
        after,
    ) -> Gtk.TreeIter | None:
        """Insert a new row into a GTK3ListStore.

        Parameters
        ----------
        values : list[object]
            The values to apply to the newly inserted row.
        position : int | None, optional
            The position to insert the new row.  Pass 0 to prepend the row, pass -1
            to append the row.
        columns : list[int] | None, optional
            The list of column numbers to insert the values.
        sibling : Gtk.TreeIter | None, optional
            The Gtk.TreeIter to insert the new row before or after.
        after : bool | None, optional
            Whether to insert the new row after the sibling or before it.

        Returns
        -------
        Gtk.TreeIter
            The Gtk.TreeIter of the newly inserted row.
        """
        if columns:
            return self.insert_with_values(position, columns, values)

        if position == 0:
            return self.prepend(values)

        if position == -1:
            return self.append(values)

        if after is None:
            return self.insert(position, values)

        if after:
            return self.insert_after(sibling, values)
        return self.insert_before(sibling, values)

    def _insert_treestore_row(
        self,
        values,
        position,
        columns,
        parent,
        sibling,
        after,
    ) -> Gtk.TreeIter | None:
        """Insert a new row into a GTK3TreeStore.

        Parameters
        ----------
        values : list[object]
            The values to apply to the newly inserted row.
        position : int | None, optional
            The position to insert the new row.  Pass 0 to prepend the row, pass -1
            to append the row.
        columns : list[int] | None, optional
            The list of column numbers to insert the values.
        parent : Gtk.TreeIter | None, optional
            The Gtk.TreeIter that will be the parent of the newly inserted row.
        sibling : Gtk.TreeIter | None, optional
            The Gtk.TreeIter to insert the new row before or after.
        after : bool | None, optional
            Whether to insert the new row after the sibling or before it.

        Returns
        -------
        Gtk.TreeIter
            The Gtk.TreeIter of the newly inserted row.
        """
        if columns:
            return self.insert_with_values(parent, position, columns, values)

        if position == 0:
            return self.prepend(parent, values)

        if position == -1:
            return self.append(parent, values)

        if after is None:
            return self.insert(parent, position, values)

        if after:
            return self.insert_after(parent, sibling, values)
        return self.insert_before(parent, sibling, values)
