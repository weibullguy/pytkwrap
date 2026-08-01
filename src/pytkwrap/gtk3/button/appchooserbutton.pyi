# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBoxMixin as GTK3ComboBoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3AppChooserButtonMixin(GTK3ComboBoxMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_APP_CHOOSER_BUTTON_PROPERTIES: Incomplete
    _GTK3_APP_CHOOSER_BUTTON_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3AppChooserButton(Gtk.AppChooserButton, GTK3AppChooserButtonMixin):
    def __init__(self) -> None: ...
