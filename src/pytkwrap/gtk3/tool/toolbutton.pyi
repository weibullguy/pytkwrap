# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolitem import GTK3ToolItemMixin as GTK3ToolItemMixin

class GTK3ToolButtonMixin(GTK3ToolItemMixin):
    _GTK3_TOOLBUTTON_PROPERTIES: Incomplete
    _GTK3_TOOLBUTTON_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3ToolButton(Gtk.ToolButton, GTK3ToolButtonMixin):
    def __init__(
        self, icon_widget: Gtk.Widget | None = None, label: str | None = None
    ) -> None: ...
