#       pytkwrap.utilities.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Utility functions for interacting with the pytkwrap application."""

# Standard Library Imports
import contextlib
import functools
import gettext
import os.path
import sys
import warnings
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any

# Third Party Imports
from dateutil.parser import parse
from pubsub import pub


_ = gettext.gettext


@dataclass
class FontDescription:  # pylint: disable=too-many-instance-attributes
    """Structured font description for use across toolkits.

    Attributes
    ----------
    allow_breaks : str
        Whether to allow line breaks. Default is 'false'.
    bgalpha : str
        Background alpha value. Default is '100%'.
    bgcolor : str
        Background color. Default is 'white'.
    family : str
        Comma separated list of font families. Default is 'Sans, Serif, Monospace'.
    features : str
        Font features. Default is empty string.
    fgalpha : str
        Foreground alpha value. Default is '100%'.
    fgcolor : str
        Foreground color. Default is 'black'.
    gravity : str
        Font gravity. Default is 'south'.  Options are 'south', 'east', 'north', 'west'.
    gravity_hint : str
        Font gravity hint. Default is 'natural'.
    insert_hyphens : str
        Whether to insert hyphens. Default is 'true'.
    lang : str
        Language for the font. Default is 'en_US'.
    letter_spacing : str
        Letter spacing. Default is empty string.
    overline : str
        Whether to overline text. Default is 'none'.  Options are 'none', 'single'.
    overline_color : str
        Overline color. Default is 'black'.
    rise : str
        Vertical rise of the text. Default is '0pt'.
    scale : str
        Font scale. Default is empty string.
    size : int
        Font size in points. Default is 10.
    stretch : str
        Font stretch. Default is empty string.  Options are 'Ultra-Condensed',
        'Extra-Condensed', 'Condensed', 'Semi-Condensed', 'Semi-Expanded',
        'Expanded', 'Extra-Expanded', 'Ultra-Expanded'.
    strikethrough : str
        Whether to strikethrough text. Default is 'false'.
    strikethrough_color : str
        Strikethrough color. Default is 'black'.
    style : str
        Font style. Default is 'Normal'.  Options are 'Normal', 'Roman', 'Oblique',
        'Italic'.
    underline : str
        Whether to underline text. Default is 'none'.  Options are 'none', 'single',
        'double', 'low', 'error', 'single-line', 'double-line', 'error-line'.
    underline_color : str
        Underline color. Default is 'black'.
    variant : str
        Font variant. Default is empty string.  Options are 'Small-Caps',
        'All-Small-Caps', 'Petite-Caps', 'All-Petite-Caps', 'Unicase', 'Title-Caps'.
    weight : str
        Font weight. Default is 'Regular'.  Options are 'Thin', 'Ultra-Light',
        'Extra-Light', 'Light', 'Semi-Light', 'Demi-Light', 'Book', 'Regular',
        'Medium', 'Semi-Bold', 'Demi-Bold', 'Bold', 'Ultra-Bold', 'Extra-Bold',
        'Heavy', 'Black', 'Ultra-Black', 'Extra-Black'.
    """

    allow_breaks: str = "false"
    bgalpha: str = "100%"
    bgcolor: str = "white"
    family: str = "Sans,Serif,Monospace"
    features: str = ""
    fgalpha: str = "100%"
    fgcolor: str = "black"
    gravity: str = "south"
    gravity_hint: str = "natural"
    insert_hyphens: str = "true"
    lang: str = "en_US"
    letter_spacing: str = ""
    overline: str = "none"
    overline_color: str = "black"
    rise: str = "0pt"
    scale: str = ""
    size: int = 10
    stretch: str = ""
    strikethrough: str = "false"
    strikethrough_color: str = "black"
    style: str = "Normal"
    underline: str = "none"
    underline_color: str = "black"
    variant: str = ""
    weight: str = "Regular"

    def to_string(self) -> str:
        """Convert to a toolkit font description string.

        Returns the core font attributes as a space-separated string
        suitable for passing to toolkit font description constructors
        such as Pango.FontDescription() or QFont().

        Returns
        -------
        str
            The font description string.
        """
        return (
            f"{self.family} {self.style} {self.variant} "
            f"{self.weight} {self.stretch} {self.gravity} {self.size}"
        ).strip()

    def to_markup(self) -> str:
        """Convert to a markup span string for rich text formatting.

        Returns an opening span tag with all font attributes set,
        suitable for use in markup-supporting widgets such as GTK3Label.
        The caller is responsible for appending the text and closing
        </span> tag.

        Note
        ----
        Currently produces Pango markup syntax (<span> tags).  Toolkit-specific
        subclasses or overrides may be needed for other markup formats (e.g. Qt rich
        text).

        Returns
        -------
        str
            The opening markup span tag with all font attributes set.
        """
        _parts = [
            f"allow_breaks='{self.allow_breaks}'",
            f"bgalpha='{self.bgalpha}'",
            f"bgcolor='{self.bgcolor}'",
            f"face='{self.family}'",
            f"font_features='{self.features}'",
            f"fgalpha='{self.fgalpha}'",
            f"fgcolor='{self.fgcolor}'",
            f"gravity='{self.gravity}'",
            f"gravity_hint='{self.gravity_hint}'",
            f"insert_hyphens='{self.insert_hyphens}'",
            f"lang='{self.lang}'",
        ]

        if self.letter_spacing:
            _parts.append(f"letter_spacing='{self.letter_spacing}'")

        _parts += [
            f"overline='{self.overline}'",
            f"overline_color='{self.overline_color}'",
            f"rise='{self.rise}'",
        ]

        if self.scale:
            _parts.append(f"font_scale='{self.scale}'")

        _parts += [
            f"size='{self.size}pt'",
            f"stretch='{self.stretch}'" if self.stretch else "",
            f"strikethrough='{self.strikethrough}'",
            f"strikethrough_color='{self.strikethrough_color}'",
            f"style='{self.style}'",
            f"underline='{self.underline}'",
            f"underline_color='{self.underline_color}'",
            f"variant='{self.variant}'" if self.variant else "",
            f"weight='{self.weight}'",
        ]

        _attrs = " ".join(p for p in _parts if p)
        return f"<span {_attrs}>"


def boolean_to_integer(boolean: bool) -> int:
    """Convert boolean representations of TRUE/FALSE to an integer value.

    Parameters
    ----------
    boolean : bool
        The boolean to convert.

    Returns
    -------
    _result : int
        The boolean value represented by a 0/1 integer.
    """
    return 1 if boolean else 0


def clamp(
    value: float | int,
    minimum: float | int,
    maximum: float | int,
) -> float | int:
    """Clamp a value between minimum and maximum values.

    Parameters
    ----------
    value : float | int
        The value to clamp.
    minimum : float | int
        The minimum value to clamp at.
    maximum : float | int
        The maximum value to clamp at.

    Returns
    -------
    _clamped_value : float | int
        The clamped value.
    """
    return max(minimum, min(value, maximum))


def date_to_ordinal(date_string: str) -> int:
    """Convert date strings to ordinal dates for use in the database.

    Parameters
    ----------
    date_string : str
        The date string to convert.

    Returns
    -------
    _ordinal : int
        The ordinal representation of the passed date.
    """
    try:
        return parse(date_string).toordinal()
    except (ValueError, TypeError):
        return parse("01/01/1970").toordinal()


def deprecated(function: Callable) -> Callable:
    """Decorate other functions as deprecated.

    Parameters
    ----------
    function : Callable
        The function to decorate.

    Returns
    -------
    _decorated_function : Callable
        The decorated function.
    """

    @functools.wraps(function)
    def _decorated_func(*args, **kwargs):
        warnings.simplefilter("always", DeprecationWarning)  # turn off filter
        warnings.warn(
            # pylint: disable-next=line-too-long
            f"Call to deprecated function {function.__name__}.",  # ty: ignore[unresolved-attribute]
            category=DeprecationWarning,
            stacklevel=2,
        )
        warnings.simplefilter("default", DeprecationWarning)  # reset filter
        return function(*args, **kwargs)

    return _decorated_func


def dir_exists(directory: str) -> bool:
    """Check if a directory exists.

    Parameters
    ----------
    directory : str
        A string representing the directory path to check for.

    Returns
    -------
    _exists : bool
        Whether the directory exists.
    """
    return os.path.isdir(directory)


def do_subscribe_to_messages(messages: dict[str, Callable]) -> None:
    """Subscribe to PyPubSub messages.

    Parameters
    ----------
    messages : dict
        A dictionary with the PyPubSub message(s) as keys and the handler
        function(s)/method(s) as values.
    """
    for _message, _handler in messages.items():
        pub.subscribe(_handler, _message)


def do_unsubscribe_from_messages(messages: dict[str, Callable]) -> None:
    """Unsubscribe from PyPubSub messages.

    Parameters
    ----------
    messages : dict
        A dictionary with the PyPubSub message(s) as keys and the handler
        function(s)/method(s) as values.
    """
    for _message, _handler in messages.items():
        with contextlib.suppress(pub.TopicNameError):
            pub.unsubscribe(_handler, _message)


def file_exists(_file: str) -> bool:
    """Check if a file exists.

    Parameters
    ----------
    _file : str
        A string representing the filepath to check for.

    Returns
    -------
    _exists : bool
        Whether the file exists.
    """
    return os.path.isfile(_file)


def get_home_directory() -> str:
    """Get the current user's home directory.

    Returns
    -------
    _home_directory : str
        The current user's home directory as an absolute path.
    """
    return os.path.expanduser("~")


def get_install_prefix() -> str:
    """Return the prefix that this code was installed into.

    Returns
    -------
    _install_prefix : str
        The prefix this code was installed into as an absolute path.
    """
    return sys.prefix


def integer_to_boolean(integer: int) -> bool:
    """Convert an integer to boolean value.

    Any value greater than zero is returned as True, all others are returned as False.

    Parameters
    ----------
    integer : int
        The integer to convert.

    Returns
    -------
    _result : bool
        The integer value represented by a boolean.
    """
    return integer > 0


def none_to_default(
    field: bool | date | float | int | str | None,
    default: bool | date | float | int | str | None,
) -> bool | date | float | int | str | None:
    """Convert None values into default values.

    Parameters
    ----------
    field : bool | date | float | int | str | None
        The original value that may be None.
    default : bool | date | float | int | str | None
        The new, default, value.

    Returns
    -------
    field : bool | date | float | int | str | None
        The new value if field is None, the old value otherwise.
    """
    return default if field is None else field


def none_to_string(string: str | None) -> str:
    """Convert None types to an empty string.

    Parameters
    ----------
    string : str | None
        The string to convert.

    Returns
    -------
    string: str
        The converted string if the original was None, the original string otherwise.
    """
    if string is None or string == "None":
        return ""
    return string


def ordinal_to_date(ordinal: int) -> str:
    """Convert ordinal dates to date strings in ISO-8601 format.

    Defaults to the current date if a bad value is passed as the argument.

    Parameters
    ----------
    ordinal : int
        The ordinal date to convert.

    Returns
    -------
    _date : str
        The ISO-8601 date representation of the passed ordinal.
    """
    try:
        return str(datetime.fromordinal(ordinal).strftime("%Y-%m-%d"))
    except TypeError:
        ordinal = datetime.now().toordinal()
        return str(datetime.fromordinal(int(ordinal)).strftime("%Y-%m-%d"))


def string_to_date(date_string: str) -> date:
    """Convert an ISO-8601 date string to a date object.

    Defaults to the current date if date_string can't be converted.

    Parameters
    ----------
    date_string : str
        The ISO-8601 date to convert.

    Returns
    -------
    _date : date
        The date object.
    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return datetime.now().date()


def split_string(string: str, delimiter: str = ":") -> list[str]:
    """Split a delimited string into its constituent parts.

    Parameters
    ----------
    string : str
        The colon delimited string that needs to be split into a list.
    delimiter : str
        The delimiter character to use to split the delimited string.

    Returns
    -------
    _string_list : list[str]
        The constituent parts of the original string.
    """
    return string.rsplit(delimiter)


def sort_dict(
    dictionary: dict[Any, Any],
    by_value: bool = True,
    reverse: bool = False,
) -> (dict)[Any, Any]:
    """Sort a dictionary by value or by key.

    Parameters
    ----------
    dictionary : dict
        The dictionary to sort.
    by_value : bool
        Whether to sort by value (default) or by key.
    reverse : bool
        Whether to sort in ascending order (default) or descending order.

    Returns
    -------
    _sorted_dict : dict
        The dictionary sorted by value or by key.
    """
    if not by_value:
        return dict(sorted(dictionary.items(), reverse=reverse))
    return dict(
        sorted(
            dictionary.items(),
            key=lambda item: item[1],
            reverse=reverse,
        )
    )


def string_to_boolean(string: bool | str) -> bool:
    """Convert string representations of True/False to a boolean value.

    Parameters
    ----------
    string : str
        The string to convert.

    Returns
    -------
    _result : bool
        The boolean representation of the passed string.
    """
    try:
        return string.lower() in {"true", "yes", "t", "y"}  # type: ignore
    except AttributeError:
        return string  # type: ignore
