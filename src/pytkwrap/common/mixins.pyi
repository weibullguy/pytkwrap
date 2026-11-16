# Standard Library Imports
import gettext
from collections.abc import Mapping, Sequence
from datetime import date
from typing import Generic, TypedDict, TypeVar

# Third Party Imports
from _typeshed import Incomplete
from matplotlib.axes import Axes
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure

# pytkwrap Package Imports
from pytkwrap.utilities import FontDescription as FontDescription

_ = gettext.gettext
A = TypeVar("A", bound=Mapping[str, object | None])

class PyTkWrapAttributes(TypedDict, total=False):
    axis: Axes | None
    canvas: FigureCanvasBase | None
    data_type: type
    default_value: bool | date | float | int | str | None
    edit_signal: list[str] | str | None
    figure: Figure | None
    font_description: FontDescription | None
    format: str | None
    index: int | None
    listen_topic: str | None
    n_columns: int | None
    n_rows: int | None
    send_topic: str | None
    x_pos: float | int | None
    y_pos: float | int | None

class PyTkWrapMixin(Generic[A]):
    _DEFAULT_HEIGHT: int
    _DEFAULT_TOOLTIP: Incomplete
    _DEFAULT_WIDTH: int
    _PYTKWRAP_ATTRIBUTES: Incomplete
    dic_attributes: Incomplete
    dic_error_message: dict[str, str]
    dic_handler_id: dict[str, int]
    dic_properties: (
        Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
    )
    def __init__(self) -> None: ...
    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None: ...
    def do_get_property(
        self, property_name: str
    ) -> bool | float | int | object | str | None: ...
    def do_get_value(
        self,
    ) -> bool | date | float | int | object | str | tuple | None: ...
    def do_set_attributes(self, attributes: A) -> None: ...
    def do_set_properties(
        self,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None: ...
    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None: ...

class PyTkWrapConfig(TypedDict):
    widget: PyTkWrapMixin
    attributes: PyTkWrapAttributes
    properties: dict

def make_pytkwrap_config(
    widget: PyTkWrapMixin, attributes: PyTkWrapAttributes, properties: dict
) -> PyTkWrapConfig: ...
