# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.button.togglebutton import (
    GTK3ToggleButtonMixin as GTK3ToggleButtonMixin,
)

class GTK3CheckButtonMixin(GTK3ToggleButtonMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int

class GTK3CheckButton(Gtk.CheckButton, GTK3CheckButtonMixin):
    def __init__(self, label: str = "...") -> None: ...
