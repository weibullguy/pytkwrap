"""The pytkwrap GTK3Calendar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from typing import cast

# pytkwrap Package Imports
from pytkwrap.common.mixins import PyTkWrapAttributes
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin


class GTK3CalendarMixin(GTK3WidgetMixin):
    """MIxin class for GTK3Calendar."""

    _GTK3_CALENDAR_ATTRIBUTES = PyTkWrapAttributes(
        default_value=date.today(),
        edit_signal=[
            "day-selected",
            "month-changed",
            "next-month",
            "next-year",
            "prev-month",
            "prev-year",
        ],
    )
    _GTK3_CALENDAR_PROPERTIES = GTK3WidgetProperties(
        day=0,
        detail_height_rows=0,
        detail_width_chars=0,
        month=0,
        no_month_change=False,
        show_day_names=True,
        show_details=True,
        show_heading=True,
        show_week_numbers=False,
        year=0,
    )
    _GTK3_CALENDAR_SIGNALS = [
        "day-selected",
        "day-selected-double-click",
        "month-changed",
        "next-month",
        "next-year",
        "prev-month",
        "prev-year",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Calendar mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_CALENDAR_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CALENDAR_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_CALENDAR_PROPERTIES)

    def do_get_value(self) -> date:
        """Retrieve a datetime.date representing the selected date in the GTK3Calendar.

        The Gtk.Calendar.get_date() method returns a tuple with the month between 0
        and 11.  We "correct" this by adding 1 to the month value we return.

        Returns
        -------
        date
            A datetime.date containing three integers representing date components
            (e.g., year, month, day).
        """
        _date = self.get_date()
        _year = _date.year
        _month = _date.month + 1
        _day = _date.day

        return date(*(_year, _month, _day))

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Calendar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Calendar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_detail_height_rows(self.dic_properties["detail_height_rows"])
        self.set_detail_width_chars(self.dic_properties["detail_width_chars"])

        _option_map = {
            "show_heading": Gtk.CalendarDisplayOptions.SHOW_HEADING,
            "show_day_names": Gtk.CalendarDisplayOptions.SHOW_DAY_NAMES,
            "show_details": Gtk.CalendarDisplayOptions.SHOW_DETAILS,
            "no_month_change": Gtk.CalendarDisplayOptions.NO_MONTH_CHANGE,
            "show_week_numbers": Gtk.CalendarDisplayOptions.SHOW_WEEK_NUMBERS,
        }
        _display_options = sum(
            (
                flag
                for key, flag in _option_map.items()
                if self.dic_properties.get(key, False)
            ),
            Gtk.CalendarDisplayOptions(0),
        )
        self.set_display_options(_display_options)

        for _property in [
            "day",
            "month",
            "year",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None:
        """Set the current value of the GTK3Calendar.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The value to set for the GTK3Calendar.
        """
        _date: date | None = None

        if isinstance(value, tuple):
            if len(value) == 3 and all(  # noqa: PLR2004
                isinstance(val, int) for val in value
            ):
                _date = date(*cast(tuple[int, int, int], value))
            else:
                super().do_set_value(value)
        elif isinstance(value, date):
            _date = value
        else:
            super().do_set_value(value)

        if _date is None:
            return

        self.select_month(_date.month - 1, _date.year)
        self.select_day(_date.day)


class GTK3Calendar(Gtk.Calendar, GTK3CalendarMixin):
    """Wrapper for version 3.0 Gtk.Calendar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Calendar."""
        Gtk.Calendar.__init__(self)
        GTK3CalendarMixin.__init__(self)
