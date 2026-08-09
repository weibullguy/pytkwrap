# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.range import GTK3RangeMixin as GTK3RangeMixin

class GTK3ScaleMixin(GTK3RangeMixin):
    _GTK3_SCALE_PROPERTIES: Incomplete
    _GTK3_SCALE_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3Scale(Gtk.Scale, GTK3ScaleMixin):
    def __init__(
        self,
        orientation: Gtk.Orientation = ...,
        adjustment: Gtk.Adjustment | None = None,
    ) -> None: ...
