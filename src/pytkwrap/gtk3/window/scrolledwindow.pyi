# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment as GTK3Adjustment
from pytkwrap.gtk3.container.bin import GTK3Bin as GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ScrolledWindow(Gtk.ScrolledWindow, GTK3Bin):
    _GTK3_SCROLLEDWINDOW_PROPERTIES: Incomplete
    _GTK3_SCROLLEDWINDOW_SIGNALS: Incomplete
    def __init__(
        self,
        hadjustment: GTK3Adjustment | None = None,
        vadjustment: GTK3Adjustment | None = None,
    ) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
