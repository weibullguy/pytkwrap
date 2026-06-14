# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin as GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3Window(Gtk.Window, GTK3Bin):
    _GTK3_WINDOW_PROPERTIES: Incomplete
    _GTK3_WINDOW_SIGNALS: Incomplete
    def __init__(self, wtype: Gtk.WindowType = ...) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
