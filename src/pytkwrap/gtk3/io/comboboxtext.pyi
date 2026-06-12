# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError as WrongTypeError
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBox as GTK3ComboBox

class GTK3ComboBoxText(Gtk.ComboBoxText, GTK3ComboBox):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, has_entry: bool = False) -> None: ...
    def do_load_combo(self, entries: list[str]) -> None: ...
    def do_get_value(self) -> str: ...
