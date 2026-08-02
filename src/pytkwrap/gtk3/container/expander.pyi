# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.bin import GTK3BinMixin as GTK3BinMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ExpanderMixin(GTK3BinMixin):
    _GTK_EXPANDER_PROPERTIES: Incomplete
    _GTK3_EXPANDER_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3Expander(Gtk.Expander, GTK3ExpanderMixin):
    def __init__(self) -> None: ...
