# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError as PytkwrapError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.io.label import GTK3Label as GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3NotebookMixin(GTK3ContainerMixin):
    _GTK3_NOTEBOOK_PROPERTIES: Incomplete
    _GTK3_NOTEBOOK_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_add_page(
        self, child: Gtk.Widget, tab_label: str | None = None, position: int = -1
    ) -> None: ...
    def do_remove_page(self, position: int) -> None: ...

class GTK3Notebook(Gtk.Notebook, GTK3NotebookMixin):
    def __init__(self) -> None: ...
