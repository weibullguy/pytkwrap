# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3RecentManagerMixin(GTK3GObjectMixin):
    _GTK3_RECENTMANAGER_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GTK3RecentManager(Gtk.RecentManager, GTK3RecentManagerMixin):
    def __init__(self) -> None: ...
    def do_add_recent(
        self, uri: str, recent_data: Gtk.RecentData | None = None
    ) -> bool: ...
    def do_remove_recent(self, uri: str, remove_all: bool = False) -> bool: ...
    @property
    def recent_items(self) -> list[Gtk.RecentData]: ...
