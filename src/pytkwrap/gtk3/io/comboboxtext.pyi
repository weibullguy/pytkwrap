# Third Party Imports
from gi.overrides.GdkPixbuf import Pixbuf as Pixbuf

# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError as WrongTypeError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBoxMixin as GTK3ComboBoxMixin

class GTK3ComboBoxTextMixin(GTK3ComboBoxMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def do_load_combo(
        self,
        entries: list[
            str | list[str | int | Pixbuf | None] | tuple[str | int | Pixbuf | None]
        ],
    ) -> None: ...
    def do_get_value(self) -> str: ...

class GTK3ComboBoxText(Gtk.ComboBoxText, GTK3ComboBoxTextMixin):
    def __init__(
        self, has_entry: bool = False, model: Gtk.ListStore | None = None
    ) -> None: ...
