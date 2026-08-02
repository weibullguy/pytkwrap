# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin as GTK3DialogMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3AboutDialogMixin(GTK3DialogMixin):
    _GTK3_ABOUTDIALOG_PROPERTIES: Incomplete
    _GTK3_ABOUTDIALOG_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3AboutDialog(Gtk.AboutDialog, GTK3AboutDialogMixin):
    def __init__(self) -> None: ...
