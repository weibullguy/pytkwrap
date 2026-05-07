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
from pytkwrap.exceptions import NoValueError as NoValueError
from pytkwrap.exceptions import PytkwrapError as PytkwrapError
from pytkwrap.exceptions import UnkAttributeError as UnkAttributeError
from pytkwrap.exceptions import UnkPropertyError as UnkPropertyError
from pytkwrap.exceptions import WrongTypeError as WrongTypeError
from pytkwrap.utilities import FontDescription as FontDescription

_ = gettext.gettext

class PyTkWrapAttributes(TypedDict, total=False):
    axis: Axes | None
    canvas: FigureCanvasBase | None
    data_type: type | None
    default_value: bool | date | float | int | str | None
    edit_signal: str
    figure: Figure | None
    font_description: FontDescription | None
    format: str
    index: int
    listen_topic: str | None
    n_columns: int
    n_rows: int
    send_topic: str | None
    x_pos: float | int
    y_pos: float | int

class ToolkitMixin:
    _DEFAULT_HEIGHT: int
    _DEFAULT_TOOLTIP: Incomplete
    _DEFAULT_WIDTH: int
    dic_error_message: dict[str, str]
    dic_handler_id: Incomplete
    dic_properties: Incomplete
    def __init__(self) -> None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | float | int | object | str | None: ...
    def do_get_value(self) -> bool | date | float | int | str | None: ...
    def do_set_properties(self, properties: dict | list[list | tuple]) -> None: ...
    def do_set_value(self, value: bool | date | float | int | str | None) -> None: ...

class PyTkWrapMixin:
    _PYTKWRAP_ATTRIBUTES: PyTkWrapAttributes
    dic_attributes: Incomplete
    dic_error_message: Incomplete
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_set_attributes(self, attributes: PyTkWrapAttributes) -> None: ...

class PyTkWrapConfig(TypedDict):
    widget: PyTkWrapMixin
    attributes: PyTkWrapAttributes
    properties: dict

def make_pytkwrap_config(
    widget: PyTkWrapMixin, attributes: PyTkWrapAttributes, properties: dict
) -> PyTkWrapConfig: ...
