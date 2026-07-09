# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.entry import GTK3Entry as GTK3Entry
from pytkwrap.utilities import FontDescription as FontDescription

class GTK3SearchEntry(Gtk.SearchEntry, GTK3Entry):
    _GTK3_SEARCHENTRY_SIGNALS: list[str]
    def __init__(self, font: FontDescription | None = None) -> None: ...
