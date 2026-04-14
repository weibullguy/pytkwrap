from _typeshed import Incomplete
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3BaseWidget as GTK3BaseWidget, GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ScrolledWindow(Gtk.ScrolledWindow, GTK3BaseWidget):
    _GTK3_SCROLLEDWINDOW_PROPERTIES: Incomplete
    _GTK3_SCROLLEDWINDOW_SIGNALS: Incomplete
    def __init__(self, child: Gtk.Widget | GTK3BaseWidget | None = None) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
