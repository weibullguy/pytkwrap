"""The pytkwrap GTK3ComboBoxText module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# Third Party Imports

# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBox


class GTK3ComboBoxText(Gtk.ComboBoxText, GTK3ComboBox):
    """Wrapper for version 3.0 Gtk.ComboBoxText."""

    # Define private class attributes.
    _DEFAULT_HEIGHT: int = 30
    _DEFAULT_WIDTH: int = 200

    def __init__(
        self,
        has_entry: bool = False,
    ) -> None:
        """Initialize an instance of the GTK3ComboBoxText.

        Parameters
        ----------
        has_entry : bool
            Indicates whether GTK3ComboBoxText will have an entry.
        """
        Gtk.ComboBoxText.__init__(self)
        GTK3ComboBox.__init__(
            self,
            display_index=0,
            simple=True,
            n_items=1,
            column_types=[GObject.TYPE_STRING],
            has_entry=has_entry,
        )

    def do_load_combo(
        self,
        entries: list[str],
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

    def do_get_value(self) -> str:
        """Return the value currently being displayed in the GTK3ComboBoxText.

        Returns
        -------
        _value : str
        """
        return self.get_active_text()
