# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.window.scrolledwindow import GTK3ScrolledWindow as GTK3ScrolledWindow

class GTK3PlacesSidebar(Gtk.PlacesSidebar, GTK3ScrolledWindow):
    _GTK3_PLACESSIDEBAR_PROPERTIES: Incomplete
    _GTK3_PLACESSIDEBAR_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None: ...
