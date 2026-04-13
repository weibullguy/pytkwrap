from . import BaseWidget as BaseWidget, WidgetProperties as WidgetProperties
from _typeshed import Incomplete
from pytkwrap.gtk3._libs import Gtk as Gtk

class ScrolledWindow(Gtk.ScrolledWindow, BaseWidget):
    _SCROLLEDWINDOW_PROPERTIES: Incomplete
    _SCROLLEDWINDOW_SIGNALS: Incomplete
    def __init__(self, child: Gtk.Widget | BaseWidget | None = None) -> None: ...
    def do_set_properties(self, properties: WidgetProperties) -> None: ...
