from _typeshed import Incomplete
from pytkwrap.common import DataWidgetAttributes as DataWidgetAttributes, DataWidgetMixin as DataWidgetMixin
from pytkwrap.gtk3._libs import GObject as GObject, Pango as Pango
from types import EllipsisType

class GTK3DataWidgetAttributes(DataWidgetAttributes, total=False):
    column_types: list[EllipsisType] | list[GObject.GType] | None
    font_description: Pango.FontDescription | str | None

class GTK3DataWidgetMixin(DataWidgetMixin):
    _GTK3_DATA_WIDGET_ATTRIBUTES: Incomplete
    column_types: list[EllipsisType] | list[GObject.GType] | None
    edit_signal: str
    font_description: Pango.FontDescription | str | None
    def __init__(self) -> None: ...
