# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.popover import GTK3PopoverMixin as GTK3PopoverMixin

class GTK3PopoverMenuMixin(GTK3PopoverMixin):
    _GTK3_POPOVERMENU_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3PopoverMenu(Gtk.PopoverMenu, GTK3PopoverMenuMixin):
    def __init__(self) -> None: ...
