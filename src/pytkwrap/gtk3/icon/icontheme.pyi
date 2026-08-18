# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3IconThemeMixin(GTK3GObjectMixin):
    _GTK3_ICONTHEME_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GTK3IconTheme(Gtk.IconTheme, GTK3IconThemeMixin):
    def __init__(self) -> None: ...
    def do_get_icon(
        self,
        icon_names: list[str],
        size: int,
        flags: Gtk.IconLookupFlags,
        scale: int = 0,
    ) -> Gtk.IconInfo: ...
    @staticmethod
    def do_get_icon_info(icon: Gtk.IconInfo) -> dict[str, bool | int | str | None]: ...
