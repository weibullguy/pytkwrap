#       pytkwrap.common.mixins.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap mixins module."""

# Standard Library Imports
from datetime import date
from typing import TypedDict

# Third Party Imports
from matplotlib.axes import Axes
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure


class WidgetAttributes(TypedDict, total=False):
    """Type for widget structural attributes."""

    label_text: str | None
    n_columns: int
    n_rows: int
    x_pos: float | int
    y_pos: float | int


class DataWidgetAttributes(WidgetAttributes, total=False):
    """Type for widget data display attributes."""

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
    """Type for widget plotting attributes."""

    axis: Axes | None
    canvas: FigureCanvasBase | None
    figure: Figure | None


class WidgetMixin:
    """Mixin to be used with all widgets."""

    _WIDGET_ATTRIBUTES = WidgetAttributes(
        label_text="",
        n_columns=0,
        n_rows=0,
        x_pos=0,
        y_pos=0,
    )
    _DEFAULT_HEIGHT = -1
    _DEFAULT_WIDTH = -1

    def __init__(self) -> None:
        """Initialize an instance of the WidgetMixin."""
        self.dic_attributes = dict(self._WIDGET_ATTRIBUTES)
        self.dic_error_message: dict[str, str] = {
            "unk_function": "{}: No such function {} exists.",
            "unk_signal": "{}: Unknown signal name '{}'.",
        }
        self.label_text: str = ""
        self.n_columns: int = 0
        self.n_rows: int = 0
        self.x_pos: int = 0
        self.y_pos: int = 0

    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | str | None:
        """Get the value of the requested attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool or date or float or int or str or None
            The value of the requested attribute.

        Raises
        ------
        KeyError
            If the requested attribute does not exist.
        """
        if attribute not in self._WIDGET_ATTRIBUTES:
            raise KeyError(
                f"{type(self).__name__}.do_get_attribute(): Unknown attribute"
                f" {attribute}."
            )
        return getattr(self, attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the widget attributes.

        Parameters
        ----------
        attributes : WidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        _int_attrs = {
            "n_columns",
            "n_rows",
            "x_pos",
            "y_pos",
        }
        _str_attrs = set(self._WIDGET_ATTRIBUTES.keys()) - _int_attrs

        for _attr in _int_attrs:
            setattr(self, _attr, int(attributes.get(_attr, self.dic_attributes[_attr])))

        for _attr in _str_attrs:
            setattr(self, _attr, str(attributes.get(_attr, self.dic_attributes[_attr])))

        self.dic_attributes.update({
            _attr: getattr(self, _attr) for _attr in _int_attrs | _str_attrs
        })


class DataWidgetMixin(WidgetMixin):  # pylint: disable=too-many-instance-attributes
    """Mixin to use with widgets that display and/or manipulate data."""

    _DATA_WIDGET_ATTRIBUTES: DataWidgetAttributes = DataWidgetAttributes(
        datatype=None,
        default=None,
        edit_signal="",
        field="",
        font_allow_breaks="",
        font_bgalpha="",
        font_bgcolor="",
        font_family="",
        font_features="",
        font_fgalpha="",
        font_fgcolor="",
        font_gravity="",
        font_gravity_hint="",
        font_insert_hyphens="",
        font_lang="",
        font_letter_spacing="",
        font_overline="",
        font_overline_color="",
        font_rise="",
        font_scale="",
        font_size="",
        font_stretch="",
        font_strikethrough="",
        font_strikethrough_color="",
        font_style="",
        font_underline="",
        font_underline_color="",
        font_variant="",
        font_variations="",
        font_weight="",
        format="{}",
        index=-1,
        listen_topic="listen_topic",
        parent_id=-1,
        record_id=-1,
        send_topic="send_topic",
    )
    _DEFAULT_EDIT_SIGNAL: str = ""

    def __init__(self) -> None:
        """Initialize an instance of the DataWidgetMixin."""
        super().__init__()

        # Initialize public instance attributes.
        self.dic_attributes.update(self._DATA_WIDGET_ATTRIBUTES)

        self.datatype: bool | date | float | int | str | None = None
        self.default: bool | date | float | int | str | None = None
        self.edit_signal: str = ""
        self.field: str = ""
        self.font_allow_breaks: str = ""
        self.font_bgalpha: str = ""
        self.font_bgcolor: str = ""
        self.font_family: str = ""
        self.font_features: str = ""
        self.font_fgalpha: str = ""
        self.font_fgcolor: str = ""
        self.font_gravity: str = ""
        self.font_gravity_hint: str = ""
        self.font_insert_hyphens: str = ""
        self.font_lang: str = ""
        self.font_letter_spacing: str = ""
        self.font_overline: str = ""
        self.font_overline_color: str = ""
        self.font_rise: str = ""
        self.font_scale: str = ""
        self.font_size: str = ""
        self.font_stretch: str = ""
        self.font_strikethrough: str = ""
        self.font_strikethrough_color: str = ""
        self.font_style: str = ""
        self.font_underline: str = ""
        self.font_underline_color: str = ""
        self.font_variant: str = ""
        self.font_variations: str = ""
        self.font_weight: str = ""
        self.format: str = "{}"
        self.index: int = -1
        self.listen_topic: str = "listen_topic"
        self.parent_id: int = -1
        self.record_id: int = -1
        self.send_topic: str = "send_topic"

    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | str | None:
        """Get the value of the requested BaseWidget attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool or date or float or int or str or None
            The value of the requested attribute.
        """
        if attribute in self._DATA_WIDGET_ATTRIBUTES:
            return getattr(self, attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the data display widget attributes.

        Parameters
        ----------
        attributes : DataWidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        super().do_set_attributes(attributes)

        _int_attrs = {
            "index",
            "parent_id",
            "record_id",
        }
        _obj_attrs = {
            "datatype",
            "default",
        }
        _str_attrs = set(self._DATA_WIDGET_ATTRIBUTES.keys()) - _int_attrs - _obj_attrs

        for _attr in _int_attrs:
            setattr(self, _attr, int(attributes.get(_attr, self.dic_attributes[_attr])))

        for _attr in _obj_attrs:
            setattr(self, _attr, attributes.get(_attr, self.dic_attributes[_attr]))

        for _attr in _str_attrs:
            setattr(self, _attr, str(attributes.get(_attr, self.dic_attributes[_attr])))

        self.dic_attributes.update({
            _attr: getattr(self, _attr)
            for _attr in _int_attrs | _obj_attrs | _str_attrs
        })


class WidgetConfig(TypedDict):
    """Type for widget configuration."""

    widget: WidgetMixin
    attributes: WidgetAttributes
    properties: dict


class PlotWidgetMixin(DataWidgetMixin):
    """Mixin for widgets that display matplotlib plots."""

    _PLOT_WIDGET_ATTRIBUTES = PlotWidgetAttributes(
        axis=None,
        canvas=None,
        figure=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of PlotWidgetMixin."""
        super().__init__()

        self.dic_attributes.update(self._PLOT_WIDGET_ATTRIBUTES)

        self.axis: Axes | None = None
        self.canvas: FigureCanvasBase | None = None
        self.figure: Figure | None = None

    def do_get_attribute(
        self,
        attribute: str,
    ) -> object | None:
        """Get the value of the requested plotting widget attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        object or None
            The value of the requested attribute.
        """
        if attribute in self._PLOT_WIDGET_ATTRIBUTES:
            return getattr(self, attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: PlotWidgetAttributes) -> None:
        """Set the widget attributes.

        Parameters
        ----------
        attributes : PlotWidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        for _attr in self._PLOT_WIDGET_ATTRIBUTES:
            setattr(self, _attr, attributes.get(_attr, self.dic_attributes[_attr]))

        self.dic_attributes.update({
            _attr: getattr(self, _attr) for _attr in self._PLOT_WIDGET_ATTRIBUTES
        })


def make_widget_config(
    widget: WidgetMixin,
    attributes: WidgetAttributes,
    properties: dict,
) -> WidgetConfig:
    """Create a widget configuration dictionary.

    This is a helper function used to ensure type-safety.

    Returns
    -------
    dict
        The widget configuration dictionary.
    """
    return {
        "widget": widget,
        "attributes": attributes,
        "properties": properties,
    }


def set_widget_sensitivity(widgets: list, sensitive: bool = True) -> None:
    """Set the sensitivity for a list of widgets.

    Parameters
    ----------
    widgets : list
        The list of widget objects.
    sensitive : bool
        Whether to make the widgets in the list sensitive or not.
    """
    for _widget in widgets:
        _widget.set_sensitive(sensitive)
