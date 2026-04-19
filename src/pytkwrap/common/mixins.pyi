# Standard Library Imports
from datetime import date
from typing import TypedDict

# Third Party Imports
from _typeshed import Incomplete
from matplotlib.axes import Axes
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure

# pytkwrap Package Imports
from pytkwrap.utilities import FontDescription as FontDescription

class WidgetAttributes(TypedDict, total=False):
    label_text: str | None
    n_columns: int
    n_rows: int
    x_pos: float | int
    y_pos: float | int

class DataWidgetAttributes(WidgetAttributes, total=False):
    datatype: bool | date | float | int | str | None
    default: bool | date | float | int | str | None
    edit_signal: str
    field: str
    font_description: FontDescription | None
    format: str
    index: int
    listen_topic: str | None
    parent_id: int
    record_id: int
    send_topic: str | None

class PlotWidgetAttributes(DataWidgetAttributes, total=False):
    axis: Axes | None
    canvas: FigureCanvasBase | None
    figure: Figure | None

class WidgetMixin:
    _WIDGET_ATTRIBUTES: Incomplete
    _DEFAULT_HEIGHT: int
    _DEFAULT_WIDTH: int
    dic_attributes: Incomplete
    dic_error_message: dict[str, str]
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

class DataWidgetMixin(WidgetMixin):
    _DATA_WIDGET_ATTRIBUTES: DataWidgetAttributes
    _DEFAULT_EDIT_SIGNAL: str
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

class WidgetConfig(TypedDict):
    widget: WidgetMixin
    attributes: WidgetAttributes
    properties: dict

class PlotWidgetMixin(DataWidgetMixin):
    _PLOT_WIDGET_ATTRIBUTES: Incomplete
    axis: Axes | None
    canvas: FigureCanvasBase | None
    figure: Figure | None
    def __init__(self) -> None: ...
    def do_get_attribute(self, attribute: str) -> object | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

def make_widget_config(
    widget: WidgetMixin, attributes: WidgetAttributes, properties: dict
) -> WidgetConfig: ...
def set_widget_sensitivity(widgets: list, sensitive: bool = True) -> None: ...
