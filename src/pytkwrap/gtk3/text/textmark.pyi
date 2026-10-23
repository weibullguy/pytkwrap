# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.text import GTK3TextBuffer as GTK3TextBuffer

class GTK3TextMarkMixin(GTK3GObjectMixin):
    _GTK3_TEXTMARK_PROPERTIES: Incomplete
    dic_properties: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @property
    def buffer(self) -> GTK3TextBuffer: ...
    @property
    def deleted(self) -> bool: ...
    @property
    def visible(self) -> bool: ...

class GTK3TextMark(Gtk.TextMark, GTK3TextMarkMixin):
    def __init__(self, name: str | None = None, left_gravity: bool = False) -> None: ...
