# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _ExpanderHost as _ExpanderHost

class GTK3ExpanderMixin(GTK3ContainerMixin):
    _GTK_EXPANDER_PROPERTIES: Incomplete
    _GTK3_EXPANDER_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...

class GTK3Expander(Gtk.Expander, GTK3ExpanderMixin):
    def __init__(self, label: str | None = None) -> None: ...
