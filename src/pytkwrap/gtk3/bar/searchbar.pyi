# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin as GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3SearchBar(Gtk.SearchBar, GTK3Bin):
    _GTK3_SEARCHBAR_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
