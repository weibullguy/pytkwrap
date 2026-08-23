"""The pytkwrap GTK3ComboBoxText module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
from gi.overrides.GdkPixbuf import Pixbuf  # type: ignore[import-untyped]

# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBoxMixin


class GTK3ComboBoxTextMixin(GTK3ComboBoxMixin):
    """Mixin for GTK3ComboBoxText.

    Notes
    -----
    GTK3ComboBoxText passes no widgets to its callback function.
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT: int = 30
    _DEFAULT_WIDTH: int = 200

    def do_add_entry(self, entry: str, position: int, ident: str | None = None) -> None:
        """Add an entry to the GTK3ComboBoxText at index.

        Parameters
        ----------
        entry : str
            The entry to add to the GTK3ComboBoxText.
        position : int
            The position in the existing list to add the entry.  If the position is
            negative, then the entry is appended to the end of the list.
        ident : str | None
            The ID of the new entry to place in the ID column.
        """
        if isinstance(ident, str):
            self.insert(position, ident, entry)
        else:
            self.insert_text(position, entry)

    def do_clear_entry(self, index: int = -1) -> None:
        """Clear the GTK3ComboBoxText entry at the specified index.

        Parameters
        ----------
        index : int
            The index of the item to clear.  Set to -1 to clear all items,
            the default behavior.
        """
        if index == -1:
            self.remove_all()
        self.remove(index)

    def do_load_combo(
        self,
        entries: list[
            str | list[str | int | Pixbuf | None] | tuple[str | int | Pixbuf | None],
        ],
    ) -> None:
        """Load the GTK3ComboBoxText.

        Parameters
        ----------
        entries : list
            The information to load into the GTK3ComboBoxText.

        Raises
        ------
        WrongTypeError
            If passed anything other than a list of strings.
        """
        if not all(isinstance(_entry, str) for _entry in entries):
            raise WrongTypeError("All entries for a GTK3ComboBoxText must be strings.")

        self.remove_all()
        self.insert_text(-1, "")

        _hid = self.dic_handler_id[self.dic_attributes["edit_signal"]]
        if _hid != -1:
            with self.handler_block(_hid):
                for _entry in entries:
                    self.insert_text(-1, _entry)


class GTK3ComboBoxText(Gtk.ComboBoxText, GTK3ComboBoxTextMixin):
    """Wrapper for version 3.0 Gtk.ComboBoxText."""

    def __init__(
        self,
        has_entry: bool = False,
        model: Gtk.ListStore | None = None,
        id_column: int | None = None,
    ) -> None:
        """Initialize an instance of the GTK3ComboBoxText.

        Parameters
        ----------
        has_entry : bool
            Indicates whether GTK3ComboBoxText will have an entry.
        model : Gtk.ListStore | None
            The model to use for the GTK3ComboBoxText.
        id_column : int | None
            The column in the model that will contain the string ID.
        """
        Gtk.ComboBoxText.__init__(
            self,
            has_entry=has_entry,
            model=model,
        )
        GTK3ComboBoxTextMixin.__init__(self)

        self.dic_properties["has_entry"] = has_entry
        self.dic_properties["model"] = model

        if model is not None:
            self.n_items = model.get_n_columns()

        if id_column is not None:
            self.dic_properties["id_column"] = id_column
            self.set_id_column(id_column)
