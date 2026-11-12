# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

# pytkwrap Local Imports
from ._protocols import _ButtonHost as _ButtonHost

class GTK3ButtonMixin(GTK3ContainerMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_BUTTON_PROPERTIES: Incomplete
    _GTK3_BUTTON_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3Button(Gtk.Button, GTK3ButtonMixin):
    def __init__(self, label: str = "...") -> None: ...
