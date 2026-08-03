# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.dialog.nativedialog import (
    GTK3NativeDialogMixin as GTK3NativeDialogMixin,
)
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3FileChooserNativeMixin(GTK3NativeDialogMixin):
    _GTK3_FILECHOOSERNATIVE_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3FileChooserNative(Gtk.FileChooserNative, GTK3FileChooserNativeMixin):
    def __init__(
        self,
        title: str | None = None,
        action: Gtk.FileChooserAction = ...,
        accept_label: str | None = None,
        cancel_label: str | None = None,
    ) -> None: ...
