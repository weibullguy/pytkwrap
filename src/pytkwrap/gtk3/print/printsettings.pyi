# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GLib as GLib
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3PrintSettingsMixin(GTK3GObjectMixin):
    file_name: str | None
    group_name: str | None
    key_file: GLib.KeyFile | None
    def __init__(self) -> None: ...
    def do_save_page_setup(self) -> None: ...

class GTK3PrintSettings(Gtk.PrintSettings, GTK3PrintSettingsMixin):
    file_name: Incomplete
    group_name: Incomplete
    key_file: Incomplete
    def __init__(
        self, file_name: str | None = None, group_name: str | None = None
    ) -> None: ...
