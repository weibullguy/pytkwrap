# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.menu.menu import GTK3MenuMixin as GTK3MenuMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3RecentChooserMenuMixin(GTK3MenuMixin):
    _GTK3_RECENTCHOOSERMENU_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3RecentChooserMenu(Gtk.RecentChooserMenu, GTK3RecentChooserMenuMixin):
    def __init__(self) -> None: ...
