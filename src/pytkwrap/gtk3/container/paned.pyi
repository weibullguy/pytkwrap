# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3Container as GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3Paned(Gtk.Paned, GTK3Container):
    _GTK3_PANED_PROPERTIES: Incomplete
    _GTK3_PANED_SIGNALS: Incomplete
    orientation: Incomplete
    def __init__(self, orientation: Gtk.Orientation = ...) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
