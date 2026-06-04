# Standard Library Imports
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.buttons.scale_button import GTK3ScaleButton as GTK3ScaleButton
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3VolumeButton(Gtk.VolumeButton, GTK3ScaleButton):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_VOLUME_BUTTON_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
