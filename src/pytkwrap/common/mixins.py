"""The pytkwrap common mixins module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import gettext
from collections.abc import Mapping
from datetime import date
from typing import TypedDict

# Third Party Imports
from matplotlib.axes import Axes  # type: ignore[import-not-found]
from matplotlib.backend_bases import FigureCanvasBase  # type: ignore[import-not-found]
from matplotlib.figure import Figure  # type: ignore[import-not-found]
from pubsub import pub  # type: ignore[import-not-found]

# pytkwrap Package Imports
from pytkwrap.exceptions import (
    NoValueError,
    PytkwrapError,
    UnkAttributeError,
    UnkPropertyError,
    WrongTypeError,
)
from pytkwrap.utilities import FontDescription

_ = gettext.gettext


class PyTkWrapAttributes(TypedDict, total=False):
    """Type for pytkwrap convenience layer attributes."""

    axis: Axes | None
    canvas: FigureCanvasBase | None
    data_type: type | None  # e.g. bool, date, float, int, str
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
    """Mixin that provides the base layer for exposing the underlying toolkit."""

    _DEFAULT_HEIGHT = -1
    _DEFAULT_TOOLTIP = _("Missing tooltip, please file an issue to have one added.")
    _DEFAULT_WIDTH = -1

    def __init__(self):
        """Initialize an instance of the ToolkitMixin."""
        self.dic_error_message: dict[str, str] = {
            "no_value": "{}: No value set or no method to retrieve value.",
            "unk_function": "{}: Unknown function '{}'.",
            "unk_property": "{}: Unknown property '{}'.",
            "unk_signal": "{}: Unknown signal '{}'.",
            "wrong_type": "{}: Wrong type for value '{}': {}.",
        }
        self.dic_handler_id = {}
        self.dic_properties = {}

    def do_get_property(
        self, property_name: str
    ) -> bool | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property whose value is to be retrieved..

        Raises
        ------
        UnkPropertyError
            If the property is not in the properties dictionary.
        """
        _error_msg = self.dic_error_message["unk_property"].format(
            f"{type(self).__name__}.do_get_property()",
            property_name,
        )
        pub.sendMessage(
            "do_log_error",
            message=_error_msg,
        )
        raise UnkPropertyError(_error_msg)

    def do_get_value(self) -> bool | date | float | int | object | str | tuple | None:
        """Return the current value of the widget.

        Raises
        ------
        NoValueError
            If the widget does not have a value or a method to retrieve the value.
        """
        _error_msg = self.dic_error_message["no_value"].format(
            f"{type(self).__name__}.do_get_value()"
        )
        pub.sendMessage(
            "do_log_error",
            message=_error_msg,
        )
        raise NoValueError(_error_msg)

    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None:
        """Set the properties to the values in the passed dictionary.

        Parameters
        ----------
        properties : dict | list
            The TypedDict (preferred) containing the properties to set. and their
            values.  It is also possible to pass a list of lists or tuples with each
            inner list or tuple containing the [key, value] or (key, value) pairs.

        Raises
        ------
        PytkwrapError
            If properties is None, a non-iterable object, or not a valid key-value
            pairs.
        """
        try:
            self.dic_properties.update(properties)
        except TypeError as exc:
            _error_msg = (
                f"{type(self).__name__}.do_set_properties(): Properties are None or a "
                f"non-iterable object: '{properties}'."
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise PytkwrapError(_error_msg) from exc
        except ValueError as exc:
            _error_msg = (
                f"{type(self).__name__}.do_set_properties(): Properties are not valid "
                f"key-value pairs: '{properties}'."
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise PytkwrapError(_error_msg) from exc

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the current value of the widget.

        Parameters
        ----------
        value : bool | date | float | int | str | None
            The value to set for the widget.

        Raises
        ------
        WrongTypeError
            If the value passed is not of the correct type.
        """
        _error_msg = self.dic_error_message["wrong_type"].format(
            f"{type(self).__name__}.do_set_value()",
            value,
            type(value),
            "bool or float or int or str",
        )
        pub.sendMessage(
            "do_log_error",
            message=_error_msg,
        )
        raise WrongTypeError(_error_msg)


class PyTkWrapMixin:
    """Mixin that provides the base for providing the pytkwrap convenience layer."""

    _PYTKWRAP_ATTRIBUTES: PyTkWrapAttributes = PyTkWrapAttributes(
        index=-1,
        x_pos=0,
        y_pos=0,
    )

    def __init__(self) -> None:
        """Initialize an instance of the PyTkWrapMixin.

        Notes
        -----
        Implements requirements:
            - PTW-SR-W-003.

        Fixes issues:
            - None
        """
        self.dic_attributes = dict(self._PYTKWRAP_ATTRIBUTES)
        self.dic_error_message = {"unk_attribute": "{}: Unknown attribute '{}'."}

    def do_get_attribute(
        self, attribute: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested PyTkWrapMixin attribute.

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
        UnkAttributeError
            If the requested attribute does not exist.
        """
        if attribute in self._PYTKWRAP_ATTRIBUTES:
            return self.dic_attributes.get(attribute)

        _error_msg = self.dic_error_message["unk_attribute"].format(
            f"{type(self).__name__}.do_get_attribute()",
            attribute,
        )
        pub.sendMessage(
            "do_log_error",
            message=_error_msg,
        )

        raise UnkAttributeError(_error_msg)

    def do_set_attributes(self, attributes: PyTkWrapAttributes) -> None:
        """Set the PyTkWrapMixin attributes.

        Parameters
        ----------
        attributes : PyTkWrapAttributes
            Typed dict with the attribute values to set for the widget.
        """
        for _attr in ("index", "x_pos", "y_pos"):
            self.dic_attributes[_attr] = int(
                attributes.get(
                    _attr,
                    self.dic_attributes[_attr],
                )
            )


class PyTkWrapConfig(TypedDict):
    """Type for widget configuration."""

    widget: PyTkWrapMixin
    attributes: PyTkWrapAttributes
    properties: dict


def make_pytkwrap_config(
    widget: PyTkWrapMixin,
    attributes: PyTkWrapAttributes,
    properties: dict,
) -> PyTkWrapConfig:
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
