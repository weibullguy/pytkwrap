# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3WidgetMixin as GTK3WidgetMixin

class GTK3ProgressBarMixin(GTK3WidgetMixin):
    _GTK3_PROGRESSBAR_ATTRIBUTES: Incomplete
    _GTK3_PROGRESSBAR_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float | int | str | None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None: ...

class GTK3ProgressBar(Gtk.ProgressBar, GTK3ProgressBarMixin):
    def __init__(self) -> None: ...
    @GObject.Signal
    def changed(self) -> None: ...
