# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.button.checkbutton import (
    GTK3CheckButtonMixin as GTK3CheckButtonMixin,
)
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3RadioButtonMixin(GTK3CheckButtonMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_RADIO_BUTTON_PROPERTIES: Incomplete
    _GTK3_RADIO_BUTTON_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3RadioButton(Gtk.RadioButton, GTK3RadioButtonMixin):
    def __init__(self, label: str = "...", group=None) -> None: ...
