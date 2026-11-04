# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk as Gdk
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3ClipboardMixin(GTK3GObjectMixin):
    _GTK3_CLIPBOARD_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @property
    def display(self) -> Gdk.Display | None: ...
    @property
    def owner(self) -> GObject.GObject | None: ...
    @property
    def selection(self) -> Gdk.Atom: ...

class GTK3Clipboard(Gtk.Clipboard, GTK3ClipboardMixin):
    def __init__(self) -> None: ...
