"""The pytkwrap common mixins module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import gettext
from datetime import date
from typing import TypedDict

# Third Party Imports
from matplotlib.axes import Axes  # type: ignore[import-not-found]
from matplotlib.backend_bases import FigureCanvasBase  # type: ignore[import-not-found]
from matplotlib.figure import Figure  # type: ignore[import-not-found]

# pytkwrap Package Imports
from pytkwrap.utilities import FontDescription

_ = gettext.gettext


class WidgetAttributes(TypedDict, total=False):
    """Type for widget structural attributes."""

    n_columns: int
    n_rows: int
    x_pos: float | int
    y_pos: float | int


class DataWidgetAttributes(WidgetAttributes, total=False):
    """Type for widget data display attributes."""

    data_type: type | None  # e.g. bool, date, float, int, str
    default_value: bool | date | float | int | str | None
    edit_signal: str
    font_description: FontDescription | None
    format: str
    index: int
    listen_topic: str | None
    send_topic: str | None


class PlotWidgetAttributes(DataWidgetAttributes, total=False):
    """Type for widget plotting attributes."""

    axis: Axes | None
    canvas: FigureCanvasBase | None
    figure: Figure | None


class BaseMixin:  # pylint: disable=[too-few-public-methods]
    """Mixin that provides the base for all other mixins."""

    def __init__(self):
        """Initialize an instance of the BaseMixin."""
        self.dic_attributes: dict[str, str] = {}
        self.dic_error_message: dict[str, str] = {
            "unk_function": "{}: No such function {} exists.",
            "unk_signal": "{}: Unknown signal name '{}'.",
        }


class WidgetMixin(BaseMixin):
    """Mixin to be used with all widgets."""

    _DEFAULT_HEIGHT = -1
    _DEFAULT_TOOLTIP = _("Missing tooltip, please file an issue to have one added.")
    _DEFAULT_WIDTH = -1
    _WIDGET_ATTRIBUTES = WidgetAttributes(
        n_columns=0,
        n_rows=0,
        x_pos=0,
        y_pos=0,
    )

    def __init__(self) -> None:
        """Initialize an instance of the WidgetMixin.

        Notes
        -----
        Implements requirements:
            - PTW-SR-W-003.

        Fixes issues:
            - None
        """
        BaseMixin.__init__(self)

        self.dic_attributes.update(self._WIDGET_ATTRIBUTES)

    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested WidgetMixin attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool | date | float | int | str | None
            The value of the requested attribute.

        Raises
        ------
        KeyError
            If the requested attribute does not exist.
        """
        if attribute not in self._WIDGET_ATTRIBUTES:
            raise KeyError(
                f"{type(self).__name__}.do_get_attribute(): Unknown attribute "
                f"'{attribute}'."
            )
        return self.dic_attributes.get(attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the WidgetMixin attributes.

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
            self.dic_attributes[_attr] = int(
                attributes.get(
                    _attr,
                    self.dic_attributes[_attr],
                )
            )

        for _attr in _str_attrs:
            self.dic_attributes[_attr] = str(
                attributes.get(
                    _attr,
                    self.dic_attributes[_attr],
                )
            )


class DataWidgetMixin(WidgetMixin):
    """Mixin to use with widgets that display and/or manipulate data."""

    _DATA_WIDGET_ATTRIBUTES: DataWidgetAttributes = DataWidgetAttributes(
        data_type=None,
        default_value=None,
        edit_signal="",
        font_description=None,
        format="{}",
        index=-1,
        listen_topic="listen_topic",
        send_topic="send_topic",
    )
    _DEFAULT_EDIT_SIGNAL: str = ""
    _DEFAULT_VALUE: bool | date | float | int | str | None = None

    def __init__(self) -> None:
        """Initialize an instance of the DataWidgetMixin."""
        super().__init__()

        # Initialize public instance attributes.
        self.dic_attributes.update(self._DATA_WIDGET_ATTRIBUTES)
        self.dic_attributes["edit_signal"] = self._DEFAULT_EDIT_SIGNAL
        self.dic_attributes["default_value"] = self._DEFAULT_VALUE

    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested DataWidgetMixin attribute.

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
            return self.dic_attributes.get(attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the DatawidgetMixin attributes.

        Parameters
        ----------
        attributes : DataWidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        super().do_set_attributes(attributes)

        _int_attrs = {
            "index",
        }
        _obj_attrs = {
            "data_type",
            "default_value",
            "font_description",
        }
        _str_attrs = set(self._DATA_WIDGET_ATTRIBUTES.keys()) - _int_attrs - _obj_attrs

        for _attr in _int_attrs:
            self.dic_attributes[_attr] = int(
                attributes.get(
                    _attr,
                    self.dic_attributes[_attr],
                )
            )

        for _attr in _obj_attrs:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

        for _attr in _str_attrs:
            self.dic_attributes[_attr] = str(
                attributes.get(
                    _attr,
                    self.dic_attributes[_attr],
                )
            )

        if self.dic_attributes["font_description"] is not None and not isinstance(
            self.dic_attributes["font_description"], FontDescription
        ):
            self.dic_attributes["font_description"] = FontDescription()


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

        # Initialize public instance attributes.
        self.dic_attributes.update(self._PLOT_WIDGET_ATTRIBUTES)

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
            return self.dic_attributes.get(attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the PlotWidgetMixin attributes.

        Parameters
        ----------
        attributes : PlotWidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        super().do_set_attributes(attributes)

        for _attr in self._PLOT_WIDGET_ATTRIBUTES:
            setattr(self, _attr, attributes.get(_attr, self.dic_attributes[_attr]))

        self.dic_attributes.update(
            {_attr: getattr(self, _attr) for _attr in self._PLOT_WIDGET_ATTRIBUTES}
        )


class WidgetConfig(TypedDict):
    """Type for widget configuration."""

    widget: WidgetMixin
    attributes: WidgetAttributes
    properties: dict


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
