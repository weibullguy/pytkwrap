# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin as GTK3DialogMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3MessageDialogMixin(GTK3DialogMixin):
    _GTK3_MESSAGEDIALOG_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3MessageDialog(Gtk.MessageDialog, GTK3MessageDialogMixin):
    def __init__(
        self, buttons: Gtk.ButtonsType = ..., message_type: Gtk.MessageType = ...
    ) -> None: ...
