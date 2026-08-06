# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin as GTK3WidgetMixin

class GTK3GLAreaMixin(GTK3WidgetMixin):
    _GTK3_GLAREA_PROPERTIES: Incomplete
    _GTK3_GLAREA_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3GLArea(Gtk.GLArea, GTK3GLAreaMixin):
    def __init__(self) -> None: ...
