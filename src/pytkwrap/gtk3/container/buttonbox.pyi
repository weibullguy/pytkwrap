# Standard Library Imports
from collections.abc import Callable as Callable
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.button.button import GTK3Button as GTK3Button
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ButtonBoxMixin(GTK3BoxMixin):
    _GTK3_BUTTONBOX_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3ButtonBox(Gtk.ButtonBox, GTK3ButtonBoxMixin):
    def __init__(self, orientation: Gtk.Orientation = ...) -> None: ...

def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    height: int = -1,
    layout: Gtk.ButtonBoxStyle = ...,
    orientation: str = "horizontal",
    width: int = -1,
) -> GTK3ButtonBox: ...
