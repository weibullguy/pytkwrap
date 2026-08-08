# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3._libs import Pango as Pango
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import (
    GTK3CellRendererMixin as GTK3CellRendererMixin,
)

class GTK3CellRendererTextMixin(GTK3CellRendererMixin):
    _GTK3_CELLRENDERERTEXT_PROPERTIES: Incomplete
    _GTK3_CELLRENDERERTEXT_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3CellRendererText(Gtk.CellRendererText, GTK3CellRendererTextMixin):
    def __init__(self) -> None: ...
