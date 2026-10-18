# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3CssProviderMixin(GTK3GObjectMixin):
    _GTK3_CSSPROVIDER_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_load_styling(
        self,
        data: str | None = None,
        file: Gio.File | None = None,
        path: str | None = None,
        resource: str | None = None,
    ) -> bool | None: ...

class GTK3CssProvider(Gtk.CssProvider, GTK3CssProviderMixin):
    def __init__(self) -> None: ...
