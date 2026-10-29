"""The pytkwrap GTK3ListStore module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetAttributes


class GTK3ListStoreMixin(GTK3GObjectMixin):
    """Mixin class for GTK3ListStore.

    Attributes
    ----------
    _GTK3_LISTSTORE_ATTRIBUTES : GTK3WidgetAttributes
        Attributes unique to GTK3ListStore.
    """

    _GTK3_LISTSTORE_ATTRIBUTES = GTK3WidgetAttributes(
        column_types=None,
        n_columns=0,
        n_rows=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ListStore."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_LISTSTORE_ATTRIBUTES)

    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested PyTkWrapMixin attribute.

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
        """Set the GTK3ListStore attributes.

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
        sibling: Gtk.TreeIter | None = None,
        after: bool | None = None,
    ) -> Gtk.TreeIter:
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
            return self.insert_with_valuesv(position, columns, values)

        if position == 0:
            return self.prepend(values)

        if position == -1:
            return self.append(values)

        if after is None:
            return self.insert(position, values)

        if after:
            return self.insert_after(sibling, values)
        return self.insert_before(sibling, values)

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


class GTK3ListStore(Gtk.ListStore, GTK3ListStoreMixin):
    """Wrapper for version 3.0 Gtk.ListStore."""

    def __init__(
        self,
        column_types: list[GObject.GType],
        n_columns: int,
        n_rows: int | None,
    ) -> None:
        """Initialize an instance of the GTK3ListStore.

        Parameters
        ----------
        column_types : list[GObject.GType], optional
            The type of data for each column in the GTK3ListStore.
        n_columns : int, optional
            The number of columns in the GTK3ListStore.
        n_rows : int | None, optional
            The initial number of rows in the GTK3ListStore.  Pass None to clear the
            GTK3ListStore.
        """
        Gtk.ListStore.__init__(self)
        GTK3ListStoreMixin.__init__(self)

        self.dic_attributes["column_types"] = column_types
        if n_columns <= 0 and column_types is not None:
            n_columns = len(column_types)

        self.dic_attributes["n_columns"] = n_columns
        self.dic_attributes["n_rows"] = n_rows

        self.do_set_attributes(self.dic_attributes)
