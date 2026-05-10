"""The pytkwrap GTK3 Calendar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3Calendar(Gtk.Calendar, GTK3Widget):
    """Wrapper for Gtk.Calendar."""

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

    def __init__(self) -> None:
        Gtk.Calendar.__init__(self)
        GTK3Widget.__init__(self)

        self.dic_properties.update(self._GTK3_CALENDAR_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CALENDAR_SIGNALS}
        )

    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
        """
        if property_name in self._GTK3_CALENDAR_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

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
        """Set the properties of the GTK3Calendar.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict, preferred, non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3Adjustment.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_detail_height_rows(self.dic_properties["detail_height_rows"])
        self.set_detail_width_chars(self.dic_properties["detail_width_chars"])

        if self.dic_properties["show_heading"]:
            self.set_display_options(Gtk.CalendarDisplayOptions(1))
        if self.dic_properties["show_day_names"]:
            self.set_display_options(Gtk.CalendarDisplayOptions(2))
        if self.dic_properties["show_details"]:
            self.set_display_options(Gtk.CalendarDisplayOptions(32))
        if self.dic_properties["no_month_change"]:
            self.set_display_options(Gtk.CalendarDisplayOptions(4))
        if self.dic_properties["show_week_numbers"]:
            self.set_display_options(Gtk.CalendarDisplayOptions(8))

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
        """Set the value of the GTK3Calendar.

        Parameters
        ----------
        value : date
            The datetime.date to set the value of the GTK3Calendar.
        """
        if not isinstance(value, (date, tuple)):
            super().do_set_value(value)
            return

        if isinstance(value, tuple):
            value = date(*value)

        if value.month > 0:
            self.select_month(value.month - 1, value.year)

        if value.day > 0:
            self.select_day(value.day)
