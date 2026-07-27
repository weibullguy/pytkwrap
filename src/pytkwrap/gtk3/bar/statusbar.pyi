# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError as PytkwrapError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3Box as GTK3Box

class GTK3Statusbar(Gtk.Statusbar, GTK3Box):
    _GTK3_STATUSBAR_SIGNALS: Incomplete
    dic_context_id: dict[str, int]
    dic_message_id: dict[str, int]
    def __init__(self, contexts: list[str] | None = None) -> None: ...
    def do_add_message(self, context: str, message: str) -> None: ...
    def do_remove_message(
        self, context: str, message: str = "", remove_all: bool = False
    ) -> None: ...
