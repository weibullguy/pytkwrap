# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3WindowMixin as GTK3WindowMixin

class GTK3ApplicationWindowMixin(GTK3WindowMixin):
    _GTK3_APPLICATIONWINDOW_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3ApplicationWindow(Gtk.ApplicationWindow, GTK3ApplicationWindowMixin):
    def __init__(self) -> None: ...
