# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import (
    GTK3CellRendererMixin as GTK3CellRendererMixin,
)

class GTK3CellRendererToggleMixin(GTK3CellRendererMixin):
    _GTK3_CELLRENDERERTOGGLE_PROPERTIES: Incomplete
    _GTK3_CELLRENDERERTOGGLE_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3CellRendererToggle(Gtk.CellRendererToggle, GTK3CellRendererToggleMixin):
    def __init__(self) -> None: ...
