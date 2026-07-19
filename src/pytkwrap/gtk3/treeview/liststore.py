"""The pytkwrap GTK3ListStore module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetAttributes


class GTK3ListStore(Gtk.ListStore, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.ListStore."""

    _GTK3_LISTSTORE_ATTRIBUTES = GTK3WidgetAttributes(
        column_types=None,
        n_columns=0,
        n_rows=0,
    )

    def __init__(self, column_types: list, n_columns: int, n_rows: int) -> None:
        """Initialize an instance of the GTK3ListStore.

        Parameters
        ----------
        column_types : list
            The type of data for each column in the GTK3ListStore.
        n_columns : int
            The number of columns in the GTK3ListStore.
        n_rows : int
            The initial number of rows in the GTK3ListStore.
        """
        Gtk.ListStore.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_attributes.update(self._GTK3_LISTSTORE_ATTRIBUTES)
        self.dic_attributes["column_types"] = column_types

        if n_columns <= 0 and column_types is not None:
            n_columns = len(column_types)

        self.dic_attributes["n_columns"] = n_columns
        self.dic_attributes["n_rows"] = n_rows

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
