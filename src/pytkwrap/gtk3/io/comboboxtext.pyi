# Third Party Imports
from _typeshed import Incomplete
from gi.overrides.GdkPixbuf import Pixbuf as Pixbuf

# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError as WrongTypeError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBoxMixin as GTK3ComboBoxMixin

class GTK3ComboBoxTextMixin(GTK3ComboBoxMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def do_add_entry(
        self, entry: str, position: int, ident: str | None = None
    ) -> None: ...
    def do_clear_entry(self, index: int = -1) -> None: ...
    def do_load_combo(
        self,
        entries: list[
            str | list[str | int | Pixbuf | None] | tuple[str | int | Pixbuf | None]
        ],
    ) -> None: ...

class GTK3ComboBoxText(Gtk.ComboBoxText, GTK3ComboBoxTextMixin):
    n_items: Incomplete
    def __init__(
        self,
        has_entry: bool = False,
        model: Gtk.ListStore | None = None,
        id_column: int | None = None,
    ) -> None: ...
