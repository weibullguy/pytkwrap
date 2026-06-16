# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3Window as GTK3Window

class GTK3Assistant(Gtk.Assistant, GTK3Window):
    _GTK3_ASSISTANT_PROPERTIES: Incomplete
    _GTK3_ASSISTANT_SIGNALS: Incomplete
    def __init__(self, use_header_bar: bool = False) -> None: ...
