# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes as PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment as GTK3Adjustment
from pytkwrap.gtk3.button.button import GTK3ButtonMixin as GTK3ButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3ScaleButtonMixin(GTK3ButtonMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    _GTK3_SCALEBUTTON_ATTRIBUTES: PyTkWrapAttributes
    _GTK3_SCALEBUTTON_PROPERTIES: Incomplete
    _GTK3_SCALEBUTTON_SIGNALS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None: ...
    def do_get_value(self) -> bool | date | float | int | object | str | None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...
    def do_configure(
        self,
        value: float,
        lower: float,
        upper: float,
        step_increment: float,
        page_increment: float,
        page_size: float,
    ) -> None: ...
    @property
    def lower(self) -> float: ...
    @property
    def minus_button(self) -> Gtk.Button: ...
    @property
    def page_increment(self) -> float: ...
    @property
    def page_size(self) -> float: ...
    @property
    def plus_button(self) -> Gtk.Button: ...
    @property
    def popup(self) -> Gtk.Widget: ...
    @property
    def step_increment(self) -> float: ...
    @property
    def upper(self) -> float: ...

class GTK3ScaleButton(Gtk.ScaleButton, GTK3ScaleButtonMixin):
    def __init__(
        self,
        size: int,
        min_value: float = 0.0,
        max_value: float = 100.0,
        step: float = 2,
        icons: list | None = None,
    ) -> None: ...
