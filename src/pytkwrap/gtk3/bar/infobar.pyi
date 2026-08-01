# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3InfoBarMixin(GTK3BoxMixin):
    _GTK3_INFOBAR_PROPERTIES: Incomplete
    _GTK3_INFOBAR_SIGNALS: Incomplete
    def __init__(self) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3InfoBar(Gtk.InfoBar, GTK3InfoBarMixin):
    def __init__(self) -> None: ...
