# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3FileChooserButtonMixin(GTK3BoxMixin):
    _GTK3_FILECHOOSERBUTTON_PROPERTIES: Incomplete
    _GTK3_FILECHOOSERBUTTON_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3FileChooserButtonMixin):
    def __init__(
        self,
        title: str = "Select a File",
        action: Gtk.FileChooserAction = ...,
        dialog: Gtk.Dialog | None = None,
    ) -> None: ...
