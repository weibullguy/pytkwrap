"""The pytkwrap GTK3TreeStore module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.treeview.treemodel import GTK3TreeModelMixin


class GTK3TreeStore(Gtk.TreeStore, GTK3TreeModelMixin):
    """Wrapper for version 3.0 Gtk.TreeStore."""

    def __init__(
        self,
        column_types: list[GObject.GType] | None,
        n_columns: int,
        n_rows: int,
    ) -> None:
        """Initialize an instance of the GTK3TreeStore.

        Parameters
        ----------
        column_types : list
            The type of data for each column in the GTK3TreeStore.
        n_columns : int
            The number of columns in the GTK3TreeStore.
        n_rows : int
            The initial number of rows in the GTK3TreeStore.
        """
        if column_types is None:
            Gtk.TreeStore.__init__(self)
        else:
            Gtk.TreeStore.__init__(self, *column_types)
        GTK3TreeModelMixin.__init__(self)

        self.type = "GTK3TreeStore"

        self.dic_attributes["column_types"] = column_types
        if n_columns <= 0 and column_types is not None:
            n_columns = len(column_types)

        self.dic_attributes["n_columns"] = n_columns
        self.dic_attributes["n_rows"] = n_rows

        self.do_set_attributes(self.dic_attributes)
