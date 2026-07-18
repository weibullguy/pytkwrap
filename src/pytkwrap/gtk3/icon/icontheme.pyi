# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin

class GTK3IconTheme(Gtk.IconTheme, GTK3GObjectMixin):
    _GTK3_ICONTHEME_SIGNALS: Incomplete
    def __init__(self) -> None: ...
