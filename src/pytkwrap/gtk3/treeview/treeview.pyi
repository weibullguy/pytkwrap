# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3Container as GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3TreeView(Gtk.TreeView, GTK3Container):
    _GTK3_TREEVIEW_PROPERTIES: Incomplete
    _GTK3_TREEVIEW_SIGNALS: Incomplete
    def __init__(self, model: Gtk.TreeModel = None) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
