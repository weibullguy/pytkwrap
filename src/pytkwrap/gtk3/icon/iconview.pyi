# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3IconViewMixin(GTK3ContainerMixin):
    _GTK3_ICONVIEW_PROPERTIES: Incomplete
    _GTK3_ICONVIEW_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3IconView(Gtk.IconView, GTK3IconViewMixin):
    def __init__(self, model: Gtk.TreeModel) -> None: ...
