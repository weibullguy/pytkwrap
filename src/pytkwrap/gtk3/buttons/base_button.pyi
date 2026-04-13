from _typeshed import Incomplete
from pytkwrap.gtk3._libs import GdkPixbuf as GdkPixbuf, Gtk as Gtk
from pytkwrap.gtk3.widget import BaseWidget as BaseWidget, WidgetProperties as WidgetProperties
from typing import Any, Callable

def do_make_buttonbox(icons: list[str], tooltips: list[str], callbacks: list[Callable], **kwargs: Any) -> Gtk.HButtonBox | Gtk.VButtonBox: ...

class BaseButton(Gtk.Button, BaseWidget):
    _BUTTON_PROPERTIES: Incomplete
    _BUTTON_SIGNALS: Incomplete
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    def __init__(self, label: str = '...') -> None: ...
    def do_set_properties(self, properties: WidgetProperties) -> None: ...
