# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.entry import GTK3EntryMixin as GTK3EntryMixin
from pytkwrap.utilities import FontDescription as FontDescription

class GTK3SearchEntryMixin(GTK3EntryMixin):
    _GTK3_SEARCHENTRY_SIGNALS: list[str]
    def __init__(self, **kwargs) -> None: ...

class GTK3SearchEntry(Gtk.SearchEntry, GTK3SearchEntryMixin):
    def __init__(self) -> None: ...
