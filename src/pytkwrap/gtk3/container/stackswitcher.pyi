# Standard Library Imports
from collections.abc import Mapping, Sequence

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _StackSwitcherHost as _StackSwitcherHost

class GTK3StackSwitcherMixin(GTK3BoxMixin):
    _GTK3_STACKSWITCHER_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...

class GTK3StackSwitcher(Gtk.StackSwitcher, GTK3StackSwitcherMixin):
    def __init__(self) -> None: ...
