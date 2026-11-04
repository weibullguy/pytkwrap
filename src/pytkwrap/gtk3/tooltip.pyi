# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3TooltipMixin(GTK3GObjectMixin):
    def do_set_icon(
        self,
        icon: GdkPixbuf.Pixbuf | None,
        gicon: Gio.Icon | None,
        icon_name: str | None,
        icon_size: int,
    ) -> None: ...
    def do_set_tooltip(self, tooltip: str | None, markup: bool) -> None: ...

class GTK3Tooltip(Gtk.Tooltip, GTK3TooltipMixin):
    def __init__(self) -> None: ...

def do_construct_tooltip(
    tooltip: str | None,
    markup: bool,
    icon: GdkPixbuf.Pixbuf | None,
    gicon: Gio.Icon | None,
    icon_name: str | None,
    icon_size: int,
) -> GTK3Tooltip: ...
