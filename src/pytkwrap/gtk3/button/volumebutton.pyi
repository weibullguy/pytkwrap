# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.button.scalebutton import (
    GTK3ScaleButtonMixin as GTK3ScaleButtonMixin,
)
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3VolumeButtonMixin(GTK3ScaleButtonMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_VOLUME_BUTTON_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3VolumeButton(Gtk.VolumeButton, GTK3VolumeButtonMixin):
    def __init__(self, size: int = 4) -> None: ...
