# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog as GTK3Dialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3MessageDialog(Gtk.MessageDialog, GTK3Dialog):
    _GTK3_MESSAGEDIALOG_PROPERTIES: Incomplete
    def __init__(
        self, buttons: Gtk.ButtonsType = ..., message_type: Gtk.MessageType = ...
    ) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
