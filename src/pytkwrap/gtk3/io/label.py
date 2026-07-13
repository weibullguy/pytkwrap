"""The pytkwrap GTK3Label module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date, datetime

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget
from pytkwrap.utilities import none_to_default


class GTK3Label(Gtk.Label, GTK3Widget):
    """Wrapper for version 3.0 Gtk.Label."""

    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_LABEL_ATTRIBUTES = GTK3WidgetAttributes(
        data_type=str,
        default_value="...",
    )
    _GTK3_LABEL_PROPERTIES = GTK3WidgetProperties(
        angle=0.0,
        attributes=None,
        ellipsize=Pango.EllipsizeMode.NONE,
        justify=Gtk.Justification.LEFT,
        label="",
        lines=-1,
        max_width_chars=-1,
        mnemonic_widget=None,
        pattern=None,
        selectable=False,
        single_line_mode=False,
        track_visited_links=True,
        use_markup=False,
        use_underline=False,
        width_chars=-1,
        wrap=False,
        wrap_mode=Pango.WrapMode.WORD,
    )
    _GTK3_LABEL_SIGNALS = [
        "activate-current-link",
        "activate-link",
        "copy-clipboard",
        "move-cursor",
        "populate-popup",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Label."""
        Gtk.Label.__init__(self)
        GTK3Widget.__init__(self)

        self.dic_attributes.update(self._GTK3_LABEL_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_LABEL_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_LABEL_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Label-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Label.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_angle(self.dic_properties["angle"])
        self.set_attributes(self.dic_properties["attributes"])
        self.set_ellipsize(self.dic_properties["ellipsize"])
        self.set_justify(self.dic_properties["justify"])
        self.set_label(self.dic_properties["label"])
        self.set_line_wrap(self.dic_properties["wrap"])
        self.set_line_wrap_mode(self.dic_properties["wrap_mode"])
        self.set_lines(self.dic_properties["lines"])
        self.set_max_width_chars(self.dic_properties["max_width_chars"])
        self.set_mnemonic_widget(self.dic_properties["mnemonic_widget"])

        if self.dic_properties["pattern"] is not None:
            self.set_pattern(self.dic_properties["pattern"])

        self.set_selectable(self.dic_properties["selectable"])
        self.set_single_line_mode(self.dic_properties["single_line_mode"])
        self.set_track_visited_links(self.dic_properties["track_visited_links"])
        self.set_use_markup(self.dic_properties["use_markup"])
        self.set_use_underline(self.dic_properties["use_underline"])
        self.set_width_chars(self.dic_properties["width_chars"])
        # self.set_xalign(self.xalign)
        # self.set_yalign(self.yalign)

    def do_get_value(self) -> float | int | str | None:
        """Retrieve the text displayed in the GTK3Label.

        This method will return the correct datatype (float, int, str) associated with
        the database field associated with the GTK3Label.

        Returns
        -------
        float | int | str | None
            The text displayed in the GTK3Label.
        """
        _value: str | None = self.get_label()

        return self.dic_attributes["data_type"](_value)

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None:
        """Set the GTK3Label active text.

        Parameters
        ----------
        value : bool | date | float | int | str | None
            The data to display in the GTK3Label.
        """
        if isinstance(value, tuple) or value is None:
            super().do_set_value(value)

        if isinstance(value, date):
            value = datetime.strftime(value, "%Y-%m-%d")

        if self.dic_properties["use_markup"]:
            if self.dic_properties["use_underline"]:
                self.set_markup_with_mnemonic(str(value))
            else:
                self.set_markup(str(value))
        elif self.dic_properties["use_underline"]:
            self.set_text_with_mnemonic(str(value))
        else:
            self.set_text(str(value))

    def do_update(
        self,
        package: dict[str, bool | date | float | int | str | None],
    ) -> None:
        """Update the GTK3Label with new text from the data package.

        Parameters
        ----------
        package : dict
            The data package to use to update the GTK3Label.
        """
        _index, _value = next(iter(package.items()))
        _value = none_to_default(_value, self.dic_attributes["default_value"])

        if _index != self.dic_attributes["index"]:
            return

        self.do_set_value(_value)
