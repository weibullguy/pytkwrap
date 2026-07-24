# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3TextTagTable(Gtk.TextTagTable, GTK3GObjectMixin):
    _GTK3_TEXTTAGTABLE_SIGNALS: Incomplete
    def __init__(self) -> None: ...
