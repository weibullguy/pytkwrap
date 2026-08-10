# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.bin import GTK3BinMixin as GTK3BinMixin

class GTK3SearchBarMixin(GTK3BinMixin):
    _GTK3_SEARCHBAR_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3SearchBar(Gtk.SearchBar, GTK3SearchBarMixin):
    def __init__(self) -> None: ...
