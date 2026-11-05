# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget
from pytkwrap.gtk3.widget import GTK3WidgetMixin as GTK3WidgetMixin
from pytkwrap.gtk3.widget import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ActionBarMixin(GTK3WidgetMixin):
    _GTK3_ACTIONBAR_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_add_child(self, child: GTK3Widget, start: bool = True) -> None: ...

class GTK3ActionBar(Gtk.ActionBar, GTK3ActionBarMixin):
    def __init__(self) -> None: ...
