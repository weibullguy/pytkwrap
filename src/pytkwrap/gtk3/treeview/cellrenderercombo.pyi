# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderertext import (
    GTK3CellRendererTextMixin as GTK3CellRendererTextMixin,
)

class GTK3CellRendererComboMixin(GTK3CellRendererTextMixin):
    _GTK3_CELLRENDERERCOMBO_PROPERTIES: Incomplete
    _GTK3_CELLRENDERERCOMBO_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3CellRendererCombo(Gtk.CellRendererCombo, GTK3CellRendererComboMixin):
    def __init__(self) -> None: ...
