# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.window.scrolledwindow import (
    GTK3ScrolledWindowMixin as GTK3ScrolledWindowMixin,
)

class GTK3PlacesSidebarMixin(GTK3ScrolledWindowMixin):
    _GTK3_PLACESSIDEBAR_PROPERTIES: Incomplete
    _GTK3_PLACESSIDEBAR_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3PlacesSidebar(Gtk.PlacesSidebar, GTK3PlacesSidebarMixin):
    def __init__(self) -> None: ...
