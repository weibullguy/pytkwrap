# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolitem import GTK3ToolItem as GTK3ToolItem

class GTK3ToolButton(Gtk.ToolButton, GTK3ToolItem):
    _GTK3_TOOLBUTTON_PROPERTIES: Incomplete
    _GTK3_TOOLBUTTON_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
