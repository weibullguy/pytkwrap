from _typeshed import Incomplete
from datetime import date
from matplotlib.axes import Axes
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure
from typing import TypedDict

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
    font_allow_breaks: str
    font_bgalpha: str
    font_bgcolor: str
    font_family: str
    font_features: str
    font_fgalpha: str
    font_fgcolor: str
    font_gravity: str
    font_gravity_hint: str
    font_insert_hyphens: str
    font_lang: str
    font_letter_spacing: str
    font_overline: str
    font_overline_color: str
    font_rise: str
    font_scale: str
    font_size: str
    font_stretch: str
    font_strikethrough: str
    font_strikethrough_color: str
    font_style: str
    font_underline: str
    font_underline_color: str
    font_variant: str
    font_variations: str
    font_weight: str
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
    label_text: str
    n_columns: int
    n_rows: int
    x_pos: int
    y_pos: int
    def __init__(self) -> None: ...
    def do_get_attribute(self, attribute: str) -> bool | date | float | int | str | None: ...
    def do_set_attributes(self, attributes: WidgetAttributes) -> None: ...

class DataWidgetMixin(WidgetMixin):
    _DATA_WIDGET_ATTRIBUTES: DataWidgetAttributes
    _DEFAULT_EDIT_SIGNAL: str
    datatype: bool | date | float | int | str | None
    default: bool | date | float | int | str | None
    edit_signal: str
    field: str
    font_allow_breaks: str
    font_bgalpha: str
    font_bgcolor: str
    font_family: str
    font_features: str
    font_fgalpha: str
    font_fgcolor: str
    font_gravity: str
    font_gravity_hint: str
    font_insert_hyphens: str
    font_lang: str
    font_letter_spacing: str
    font_overline: str
    font_overline_color: str
    font_rise: str
    font_scale: str
    font_size: str
    font_stretch: str
    font_strikethrough: str
    font_strikethrough_color: str
    font_style: str
    font_underline: str
    font_underline_color: str
    font_variant: str
    font_variations: str
    font_weight: str
    format: str
    index: int
    listen_topic: str
    parent_id: int
    record_id: int
    send_topic: str
    def __init__(self) -> None: ...
    def do_get_attribute(self, attribute: str) -> bool | date | float | int | str | None: ...
    def do_set_attributes(self, attributes: DataWidgetAttributes) -> None: ...

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
    def do_set_attributes(self, attributes: PlotWidgetAttributes) -> None: ...

def make_widget_config(widget: WidgetMixin, attributes: WidgetAttributes, properties: dict) -> WidgetConfig: ...
def set_widget_sensitivity(widgets: list, sensitive: bool = True) -> None: ...
