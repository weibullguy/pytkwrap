# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolbutton import GTK3ToolButtonMixin as GTK3ToolButtonMixin

class GTK3MenuToolButtonMixin(GTK3ToolButtonMixin):
    _GTK3_MENUTOOLBUTTON_PROPERTIES: Incomplete
    _GTK3_MENUTOOLBUTTON_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3MenuToolButton(Gtk.MenuToolButton, GTK3MenuToolButtonMixin):
    def __init__(
        self, icon_widget: Gtk.Widget | None = None, label: str | None = None
    ) -> None: ...
