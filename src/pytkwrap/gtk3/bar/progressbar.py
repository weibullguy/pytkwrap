"""The pytkwrap GTK3ProgressBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget
from pytkwrap.utilities import none_to_default


class GTK3ProgressBar(Gtk.ProgressBar, GTK3Widget):
    """Wrapper for version 3.0 Gtk.ProgressBar."""

    _GTK3_PROGRESSBAR_ATTRIBUTES = GTK3WidgetAttributes(
        default_value=0.0,
        data_type=float,
    )
    _GTK3_PROGRESSBAR_PROPERTIES = GTK3WidgetProperties(
        ellipsize=Pango.EllipsizeMode.NONE,
        fraction=0.0,
        inverted=False,
        pulse_step=0.1,
        show_text=False,
        text=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ProgressBar."""
        Gtk.ProgressBar.__init__(self)
        GTK3Widget.__init__(self)

        self.dic_attributes.update(self._GTK3_PROGRESSBAR_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_PROGRESSBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ProgressBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ProgressBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_ellipsize(self.dic_properties["ellipsize"])
        self.set_fraction(self.dic_properties["fraction"])
        self.set_inverted(self.dic_properties["inverted"])
        self.set_pulse_step(self.dic_properties["pulse_step"])
        self.set_show_text(self.dic_properties["show_text"])
        self.set_text(self.dic_properties["text"])

    def do_get_value(self) -> float | int | str | None:
        """Retrieve the text displayed in the GTK3ProgressBar.

        This method will return the correct datatype (float, int, str) associated with
        the database field associated with the GTK3ProgressBar.

        Returns
        -------
        float | int | str | None
            The text displayed in the GTK3ProgressBar.
        """
        _value: str | None = self.get_fraction()

        return self.dic_attributes["data_type"](_value)

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None:
        """Set the GTK3ProgressBar active progress.

        Parameters
        ----------
        value : bool | date | float | int | str | None
            The progress fraction for the GTK3ProgressBar.  This can be passed as a
            value between 0.0 and 1.0, or as a percentage value between 0 and 100.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)

        _value = self.dic_attributes["data_type"](value)

        if _value > 1.0:
            _value /= 100.0

        self.set_fraction(_value)

    def do_update(
        self,
        package: dict[str, bool | date | float | int | str | None],
    ) -> None:
        """Update the GTK3ProgressBar with new text from the data package.

        Parameters
        ----------
        package : dict
            The data package to use to update the GTK3ProgressBar.
        """
        _index, _value = next(iter(package.items()))
        _value = none_to_default(_value, self.dic_attributes["default_value"])

        if _index != self.dic_attributes["index"]:
            return

        self.do_set_value(_value)
