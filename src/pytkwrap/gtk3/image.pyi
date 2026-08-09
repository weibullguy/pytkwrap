# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin as GTK3WidgetMixin

class GTK3ImageMixin(GTK3WidgetMixin):
    _GTK3_IMAGE_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3Image(Gtk.Image, GTK3ImageMixin):
    size: Incomplete
    def __init__(
        self, icon_name: str | None = None, pixbuf: GdkPixbuf = None, size: int = 4
    ) -> None: ...
