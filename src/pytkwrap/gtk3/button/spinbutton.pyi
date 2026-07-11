# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.io.entry import GTK3Entry as GTK3Entry
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3SpinButton(Gtk.SpinButton, GTK3Entry):
    _GTK3_SPINBUTTON_ATTRIBUTES: Incomplete
    _GTK3_SPINBUTTON_PROPERTIES: Incomplete
    _GTK3_SPINBUTTON_SIGNALS: list[str]
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None: ...
