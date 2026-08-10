# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete as Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject as GObject
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3WidgetMixin as GTK3WidgetMixin

class GTK3LevelBarMixin(GTK3WidgetMixin):
    _GTK3_LEVELBAR_ATTRIBUTES: Incomplete
    _GTK3_LEVELBAR_PROPERTIES: Incomplete
    _GTK3_LEVELBAR_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> float | int | str | None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...

class GTK3LevelBar(Gtk.LevelBar, GTK3LevelBarMixin):
    def __init__(self) -> None: ...
    @GObject.Signal
    def changed(self) -> None: ...
