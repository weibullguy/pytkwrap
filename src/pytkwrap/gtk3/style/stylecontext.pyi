# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.style import GTK3CssProvider as GTK3CssProvider

class GTK3StyleContextMixin(GTK3GObjectMixin):
    _GTK3_STYLECONTEXT_PROPERTIES: Incomplete
    _GTK3_STYLECONTEXT_SIGNALS: Incomplete
    dic_properties: Incomplete
    dic_providers: dict[GTK3CssProvider, int]
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_add_style_provider(
        self, provider: GTK3CssProvider, priority: int, screen: Gdk.Screen | None = None
    ) -> None: ...
    def do_get_stateful_property(
        self, property_name: str, state: Gtk.StateFlags
    ) -> Gtk.Border | Gdk.RGBA | None: ...
    def do_remove_style_provider(self, provider: GTK3CssProvider) -> None: ...

class GTK3StyleContext(Gtk.StyleContext, GTK3StyleContextMixin):
    def __init__(self) -> None: ...
