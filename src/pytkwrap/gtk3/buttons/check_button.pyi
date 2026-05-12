# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.toggle_button import GTK3ToggleButton as GTK3ToggleButton

class GTK3CheckButton(Gtk.CheckButton, GTK3ToggleButton):
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, label: str = "...") -> None: ...
