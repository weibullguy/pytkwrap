# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3Window as GTK3Window

class GTK3ShortcutsWindow(Gtk.ShortcutsWindow, GTK3Window):
    _GTK3_SHORTCUTSWINDOW_PROPERTIES: Incomplete
    _GTK3_SHORTCUTSWINDOW_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
