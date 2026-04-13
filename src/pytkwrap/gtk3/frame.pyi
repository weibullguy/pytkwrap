from _typeshed import Incomplete
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3BaseWidget as GTK3BaseWidget, GTK3WidgetProperties as GTK3WidgetProperties

class GTK3Frame(Gtk.Frame, GTK3BaseWidget):
    _GTK3_FRAME_PROPERTIES: Incomplete
    _GTK3_FRAME_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
