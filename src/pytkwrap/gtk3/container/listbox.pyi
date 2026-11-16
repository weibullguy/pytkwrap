# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment as GTK3Adjustment
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _ListBoxHost as _ListBoxHost

class GTK3ListBoxMixin(GTK3ContainerMixin):
    _GTK3_LISTBOX_PROPERTIES: Incomplete
    _GTK3_LISTBOX_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    def do_add_child(self, child: Gtk.Widget, position: int | None = None) -> None: ...
    def do_get_row(
        self, index: int | None = None, y: int | None = None
    ) -> Gtk.ListBoxRow | None: ...
    def do_get_selected(self) -> list[Gtk.ListBoxRow]: ...
    def do_select_row(self, row: Gtk.ListBoxRow | None) -> None: ...
    def do_unselect_row(self, row: Gtk.ListBoxRow | None) -> None: ...

class GTK3ListBox(Gtk.ListBox, GTK3ListBoxMixin):
    def __init__(self, adjustment: GTK3Adjustment | None = None) -> None: ...
