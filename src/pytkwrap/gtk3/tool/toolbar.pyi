# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolbutton import GTK3ToolButton as GTK3ToolButton
from pytkwrap.gtk3.tool.toolitem import GTK3ToolItem as GTK3ToolItem

class GTK3ToolbarMixin(GTK3ContainerMixin):
    _GTK3_TOOLBAR_PROPERTIES: Incomplete
    _GTK3_TOOLBAR_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_build_toolbar(
        self,
        children: (
            list[list[GTK3ToolButton | GTK3ToolItem | int]]
            | list[tuple[GTK3ToolButton | GTK3ToolItem, int]]
            | tuple[list[GTK3ToolButton | GTK3ToolItem | int]]
            | tuple[tuple[GTK3ToolButton | GTK3ToolItem, int]]
        ),
    ): ...
    @property
    def n_items(self) -> int: ...
    @property
    def relief_style(self) -> Gtk.ReliefStyle: ...

class GTK3Toolbar(Gtk.Toolbar, GTK3ToolbarMixin):
    def __init__(self) -> None: ...
