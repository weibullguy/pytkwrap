# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin as GTK3DialogMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3AppChooserDialogMixin(GTK3DialogMixin):
    _GTK3_APPCHOOSERDIALOG_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3AppChooserDialog(Gtk.AppChooserDialog, GTK3AppChooserDialogMixin):
    def __init__(
        self, parent: Gtk.Window | None, flags: Gtk.DialogFlags, gfile: Gio.File = None
    ) -> None: ...
