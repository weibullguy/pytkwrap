# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin

class GTK3StatusbarMixin(GTK3BoxMixin):
    _GTK3_STATUSBAR_SIGNALS: Incomplete
    dic_context_id: dict[str, int]
    dic_message_id: dict[str, int]
    def __init__(self) -> None: ...
    def do_add_message(self, context: str, message: str) -> None: ...
    def do_remove_message(
        self, context: str, message: str = "", remove_all: bool = False
    ) -> None: ...

class GTK3Statusbar(Gtk.Statusbar, GTK3StatusbarMixin):
    def __init__(self, contexts: list[str] | None = None) -> None: ...
