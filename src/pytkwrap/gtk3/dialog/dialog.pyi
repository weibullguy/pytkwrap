# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3WindowMixin as GTK3WindowMixin

class GTK3DialogMixin(GTK3WindowMixin):
    _GTK3_DIALOG_PROPERTIES: Incomplete
    _GTK3_DIALOG_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GTK3Dialog(Gtk.Dialog, GTK3DialogMixin):
    def __init__(self, use_header_bar: bool = False) -> None: ...
