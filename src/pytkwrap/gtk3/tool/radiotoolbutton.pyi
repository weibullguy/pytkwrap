# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.tool.toggletoolbutton import (
    GTK3ToggleToolButton as GTK3ToggleToolButton,
)

class GTK3RadioToolButton(Gtk.RadioToolButton, GTK3ToggleToolButton):
    _GTK3_RADIOTOOLBUTTON_PROPERTIES: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
