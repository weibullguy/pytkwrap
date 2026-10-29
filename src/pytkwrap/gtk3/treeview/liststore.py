"""The pytkwrap GTK3ListStore module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.treeview.treemodel import GTK3TreeModelMixin


class GTK3ListStore(Gtk.ListStore, GTK3TreeModelMixin):
    """Wrapper for version 3.0 Gtk.ListStore."""

    def __init__(
        self,
        column_types: list[GObject.GType] | None,
        n_columns: int,
        n_rows: int | None,
    ) -> None:
        """Initialize an instance of the GTK3ListStore.

        Parameters
        ----------
        column_types : list[GObject.GType] | None, optional
            The type of data for each column in the GTK3ListStore.
        n_columns : int, optional
            The number of columns in the GTK3ListStore.
        n_rows : int | None, optional
            The initial number of rows in the GTK3ListStore.  Pass None to clear the
            GTK3ListStore.
        """
        if column_types is None:
            Gtk.ListStore.__init__(self)
        else:
            Gtk.ListStore.__init__(self, *column_types)
        GTK3TreeModelMixin.__init__(self)

        self.type = "GTK3ListStore"

        self.dic_attributes["column_types"] = column_types
        if n_columns <= 0 and column_types is not None:
            n_columns = len(column_types)

        self.dic_attributes["n_columns"] = n_columns
        self.dic_attributes["n_rows"] = n_rows

        self.do_set_attributes(self.dic_attributes)
