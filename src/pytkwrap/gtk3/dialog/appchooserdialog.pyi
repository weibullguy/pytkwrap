# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio as Gio
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog as GTK3Dialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3AppChooserDialog(Gtk.AppChooserDialog, GTK3Dialog):
    _GTK3_APPCHOOSERDIALOG_PROPERTIES: Incomplete
    def __init__(self, gfile: Gio.File = None) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
