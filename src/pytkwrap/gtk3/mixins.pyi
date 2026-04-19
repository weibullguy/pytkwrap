# Standard Library Imports
from types import EllipsisType

# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.common import DataWidgetAttributes as DataWidgetAttributes
from pytkwrap.common import DataWidgetMixin as DataWidgetMixin
from pytkwrap.common import WidgetAttributes as WidgetAttributes
from pytkwrap.gtk3._libs import GObject as GObject

class GTK3DataWidgetAttributes(DataWidgetAttributes, total=False):
    column_types: list[EllipsisType] | list[GObject.GType] | None

class GTK3DataWidgetMixin(DataWidgetMixin):
    _GTK3_DATA_WIDGET_ATTRIBUTES: Incomplete
    def __init__(self) -> None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...
