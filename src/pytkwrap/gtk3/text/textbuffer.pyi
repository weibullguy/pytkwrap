# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3TextBufferMixin(GTK3GObjectMixin):
    _GTK3_TEXTBUFFER_PROPERTIES: Incomplete
    _GTK3_TEXTBUFFER_SIGNALS: Incomplete
    dic_properties: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    @property
    def modified(self) -> bool: ...
    @property
    def n_chars(self) -> int: ...
    @property
    def n_lines(self) -> int: ...
    @property
    def text_selected(self) -> bool: ...

class GTK3TextBuffer(Gtk.TextBuffer, GTK3TextBufferMixin):
    def __init__(self, tag_table: Gtk.TextTagTable | None = None) -> None: ...
