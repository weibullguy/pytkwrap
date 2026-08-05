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
    """Mixin for GTK3ComboBoxText."""

    # Define private class attributes.
    _DEFAULT_HEIGHT: int = 30
    _DEFAULT_WIDTH: int = 200

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

    def do_get_value(self) -> str:
        """Return the value currently being displayed in the GTK3ComboBoxText.

        Returns
        -------
        _value : str
        """
        return self.get_active_text()


class GTK3ComboBoxText(Gtk.ComboBoxText, GTK3ComboBoxTextMixin):
    """Wrapper for version 3.0 Gtk.ComboBoxText."""

    def __init__(
        self,
        has_entry: bool = False,
        model: Gtk.ListStore | None = None,
    ) -> None:
        """Initialize an instance of the GTK3ComboBoxText.

        Parameters
        ----------
        has_entry : bool
            Indicates whether GTK3ComboBoxText will have an entry.
        """
        Gtk.ComboBoxText.__init__(self, has_entry=has_entry, model=model)
        GTK3ComboBoxTextMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties["has_entry"] = has_entry
        self.dic_properties["model"] = model
