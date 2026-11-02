# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget as GTK3Widget
from pytkwrap.gtk3.window.window import GTK3WindowMixin as GTK3WindowMixin

class GTK3AssistantMixin(GTK3WindowMixin):
    _GTK3_ASSISTANT_PROPERTIES: Incomplete
    _GTK3_ASSISTANT_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_add_page(self, page: GTK3Widget, position: int = -1) -> int: ...
    @property
    def n_pages(self) -> int: ...

class GTK3Assistant(Gtk.Assistant, GTK3AssistantMixin):
    def __init__(self, use_header_bar: bool = False) -> None: ...

def do_construct_assistant(
    pages: list[GTK3Widget],
    titles: list[str] | None = None,
    types: list[Gtk.AssistantPageType] | None = None,
    use_header_bar: bool = False,
) -> GTK3Assistant: ...
