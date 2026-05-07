# Standard Library Imports
import abc
from abc import abstractmethod
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common import PyTkWrapMixin as PyTkWrapMixin
from pytkwrap.exceptions import UnkSignalError as UnkSignalError
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties
from pytkwrap.utilities import none_to_default as none_to_default

class GTK3Widget(Gtk.Widget, GTK3GObjectMixin, PyTkWrapMixin, metaclass=abc.ABCMeta):
    _GTK3_WIDGET_PROPERTIES: Incomplete
    _GTK3_WIDGET_SIGNALS: Incomplete
    dic_properties: Incomplete
    def __init__(self) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_properties(self, properties: dict | list[list | tuple]) -> None: ...
    @abstractmethod
    def do_get_value(self) -> bool | date | float | int | str | None: ...
    @abstractmethod
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...
    def do_update(
        self, package: dict[str, bool | date | float | int | str | None]
    ) -> None: ...
    def on_changed(self, /, __widget: GTK3Widget) -> None: ...
    def _get_signal_owner(self) -> GTK3Widget: ...
