# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete
from pubsub import pub as pub

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin as GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes as GTK3WidgetAttributes
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.gtk3.text import GTK3TextBuffer as GTK3TextBuffer

class GTK3TextViewMixin(GTK3ContainerMixin):
    _GTK3_TEXTVIEW_ATTRIBUTES: Incomplete
    _GTK3_TEXTVIEW_PROPERTIES: Incomplete
    _GTK3_TEXTVIEW_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: Mapping[str, object]) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> str: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...

class GTK3TextView(Gtk.TextView, GTK3TextViewMixin):
    def __init__(self, buffer: GTK3TextBuffer | None = None) -> None: ...
