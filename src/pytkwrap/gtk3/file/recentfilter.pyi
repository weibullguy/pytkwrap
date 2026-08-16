# Standard Library Imports
from collections.abc import Callable

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3RecentFilter(Gtk.RecentFilter, GTK3GObjectMixin):
    def __init__(self) -> None: ...
    def do_set_filter(
        self,
        *data: object | None,
        mime_types: list[str] | None = None,
        age: int | None = None,
        applications: str | None = None,
        patterns: list[str] | None = None,
        needed: Gtk.FileFilterFlags | None = None,
        func: Callable | None = None,
    ): ...
