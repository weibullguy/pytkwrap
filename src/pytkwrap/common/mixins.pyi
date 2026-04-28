# Standard Library Imports
import gettext
from datetime import date
from typing import TypedDict

# Third Party Imports
from _typeshed import Incomplete
from matplotlib.axes import Axes
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure

# pytkwrap Package Imports
from pytkwrap.utilities import FontDescription as FontDescription

_ = gettext.gettext

class WidgetAttributes(TypedDict, total=False):
    n_columns: int
    n_rows: int
    x_pos: float | int
    y_pos: float | int

class DataWidgetAttributes(WidgetAttributes, total=False):
    data_type: type | None
    default_value: bool | date | float | int | str | None
    edit_signal: str
    font_description: FontDescription | None
    format: str
    index: int
    listen_topic: str | None
    send_topic: str | None

class PlotWidgetAttributes(DataWidgetAttributes, total=False):
    axis: Axes | None
    canvas: FigureCanvasBase | None
    figure: Figure | None

class BaseMixin:
    dic_attributes: dict[str, str]
    dic_error_message: dict[str, str]
    def __init__(self) -> None: ...

class WidgetMixin(BaseMixin):
    _DEFAULT_HEIGHT: int
    _DEFAULT_TOOLTIP: Incomplete
    _DEFAULT_WIDTH: int
    _WIDGET_ATTRIBUTES: Incomplete
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

class DataWidgetMixin(WidgetMixin):
    _DATA_WIDGET_ATTRIBUTES: DataWidgetAttributes
    _DEFAULT_EDIT_SIGNAL: str
    _DEFAULT_VALUE: bool | date | float | int | str | None
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

class PlotWidgetMixin(DataWidgetMixin):
    _PLOT_WIDGET_ATTRIBUTES: Incomplete
    def __init__(self) -> None: ...
    def do_get_attribute(self, attribute: str) -> object | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

class WidgetConfig(TypedDict):
    widget: WidgetMixin
    attributes: WidgetAttributes
    properties: dict

def make_widget_config(
    widget: WidgetMixin, attributes: WidgetAttributes, properties: dict
) -> WidgetConfig: ...
