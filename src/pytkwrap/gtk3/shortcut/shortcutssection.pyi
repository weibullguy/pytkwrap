# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin as GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ShortcutsSectionMixin(GTK3BoxMixin):
    _GTK3_SHORTCUTSSECTION_PROPERTIES: Incomplete
    _GTK3_SHORTCUTSSECTION_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...

class GTK3ShortcutsSection(Gtk.ShortcutsSection, GTK3ShortcutsSectionMixin):
    def __init__(self) -> None: ...
