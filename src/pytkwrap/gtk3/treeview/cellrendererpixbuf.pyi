# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import (
    GTK3CellRendererMixin as GTK3CellRendererMixin,
)

class GTK3CellRendererPixbufMixin(GTK3CellRendererMixin):
    _GTK3_CELLRENDERERPIXBUF_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3CellRendererPixbuf(Gtk.CellRendererPixbuf, GTK3CellRendererPixbufMixin):
    def __init__(self) -> None: ...
