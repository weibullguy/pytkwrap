"""The pytkwrap GTK3Entry module.

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
from pytkwrap.utilities import FontDescription


class GTK3Entry(Gtk.Entry, GTK3Widget):
    """The GTK3Entry class.

    Attributes
    ----------
    _GTK3_ENTRY_ATTRIBUTES : GTK3DataWidgetAttributes
        The typed dict containing GTK3Entry specific attributes and their default
        values.
    _GTK3_ENTRY_PROPERTIES : GTK3WidgetProperties
        The typed dict containing GTK3Entry specific properties and their default
        values.
    _GTK3_ENTRY_SIGNALS : list
        The list of signal names specifically associated with the GTK3Entry.
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT: int = 25
    _DEFAULT_WIDTH: int = 200
    _GTK3_ENTRY_ATTRIBUTES = GTK3WidgetAttributes(
        data_type=str,
        default_value="",
        edit_signal="changed",
        font_description=FontDescription(),
        format=None,
    )
    _GTK3_ENTRY_PROPERTIES = GTK3WidgetProperties(
        activates_default=False,
        attributes=None,
        buffer=None,
        caps_lock_warning=True,
        completion=None,
        editable=True,
        editing_canceled=False,
        enable_emoji_completion=False,
        has_frame=True,
        im_module=None,
        input_hints=Gtk.InputHints.NONE,  # pylint: disable=no-member
        input_purpose=Gtk.InputPurpose.FREE_FORM,
        invisible_char="•",
        invisible_char_set=False,
        max_length=0,
        max_width_chars=-1,
        overwrite_mode=False,
        placeholder_text=None,
        populate_all=False,
        primary_icon_activatable=True,
        primary_icon_gicon=None,
        primary_icon_name=None,
        primary_icon_pixbuf=None,
        primary_icon_sensitive=True,
        primary_icon_tooltip_markup=None,
        primary_icon_tooltip_text=None,
        progress_fraction=0.0,
        progress_pulse_step=0.1,
        scroll_offset=0,
        secondary_icon_activatable=True,
        secondary_icon_gicon=None,
        secondary_icon_name=None,
        secondary_icon_pixbuf=None,
        secondary_icon_sensitive=True,
        secondary_icon_tooltip_markup=None,
        secondary_icon_tooltip_text=None,
        show_emoji_icon=False,
        tabs=None,
        text="",
        truncate_multiline=False,
        visibility=True,
        width_chars=-1,
        xalign=0.0,
    )
    _GTK3_ENTRY_SIGNALS: list[str] = [
        "activate",
        "backspace",
        "changed",
        "copy-clipboard",
        "cut-clipboard",
        "delete-from-cursor",
        "delete-text",
        "editing-done",
        "icon-press",
        "icon-release",
        "insert-at-cursor",
        "insert-emoji",
        "insert-text",
        "move-cursor",
        "paste-clipboard",
        "populate-popup",
        "preedit-changed",
        "remove-widget",
        "toggle-direction",
        "toggle-overwrite",
    ]

    def __init__(
        self,
        font: FontDescription | None = None,
    ) -> None:
        """Initialize an instance of the GTK3Entry widget.

        Parameters
        ----------
        font : FontDescription | None
            The font description for the font used by the GTK3Entry.
        """
        Gtk.Entry.__init__(self)
        GTK3Widget.__init__(self)

        self.dic_attributes.update(self._GTK3_ENTRY_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ENTRY_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_ENTRY_PROPERTIES)

        self.do_set_font_description(font)

        self.show()

    def do_set_attributes(self, attributes: Mapping[str, object]) -> None:
        """Set the attributes of the Entry.

        Parameters
        ----------
        attributes : GTK3WidgetAttributes
            The typed dict with the attribute values to set for the GTK3Entry.
        """
        super().do_set_attributes(attributes)

        self.do_set_font_description(self.dic_attributes["font_description"])

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3Entry.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3Entry.
        """
        super().do_set_properties(properties)

        self.set_activates_default(self.dic_properties["activates_default"])
        self.set_alignment(self.dic_properties["xalign"])
        if self.dic_properties["attributes"] is not None:
            self.set_attributes(self.dic_properties["attributes"])
        if self.dic_properties["buffer"] is not None:
            self.set_buffer(self.dic_properties["buffer"])
        self.set_completion(self.dic_properties["completion"])
        self.set_editable(self.dic_properties["editable"])
        self.set_has_frame(self.dic_properties["has_frame"])
        self.set_input_hints(self.dic_properties["input_hints"])
        self.set_input_purpose(self.dic_properties["input_purpose"])
        self.set_invisible_char(self.dic_properties["invisible_char"])
        self.set_max_length(self.dic_properties["max_length"])
        self.set_max_width_chars(self.dic_properties["max_width_chars"])
        self.set_overwrite_mode(self.dic_properties["overwrite_mode"])
        self.set_placeholder_text(self.dic_properties["placeholder_text"])
        self.set_progress_fraction(self.dic_properties["progress_fraction"])
        self.set_progress_pulse_step(self.dic_properties["progress_pulse_step"])
        if self.dic_properties["tabs"] is not None:
            self.set_tabs(self.dic_properties["tabs"])
        self.set_text(self.dic_properties["text"])
        self.set_visibility(self.dic_properties["visibility"])
        self.set_width_chars(self.dic_properties["width_chars"])

        for _property in [
            "caps_lock_warning",
            "enable_emoji_completion",
            "im_module",
            "invisible_char_set",
            "populate_all",
            "primary_icon_activatable",
            "primary_icon_gicon",
            "primary_icon_name",
            "primary_icon_pixbuf",
            "primary_icon_sensitive",
            "primary_icon_tooltip_markup",
            "primary_icon_tooltip_text",
            "secondary_icon_activatable",
            "secondary_icon_gicon",
            "secondary_icon_name",
            "secondary_icon_pixbuf",
            "secondary_icon_sensitive",
            "secondary_icon_tooltip_markup",
            "secondary_icon_tooltip_text",
            "show_emoji_icon",
            "truncate_multiline",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_get_value(self) -> float | int | str | None:
        """Retrieve the text displayed in the GTK3Entry.

        This method will return the correct datatype (float, int, str) associated with
        the database field associated with the GTK3Entry.

        Returns
        -------
        float | int | str | None
            The value displayed in the GTK3Entry.
        """
        _value: str | None = self.get_text()

        return self.dic_attributes["datatype"](_value)

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None = None
    ) -> None:
        """Set the GTK3Entry active value.

        Parameters
        ----------
        value : bool | date | float | int | str | None
            The data to display in the GTK3Entry.
        """
        if isinstance(value, tuple) or value is None:
            super().do_set_value(value)

        if isinstance(value, date):
            value = datetime.strftime(value, "%Y-%m-%d")

        self.set_text(str(value))

    def do_set_font_description(
        self,
        font: FontDescription | None = None,
    ) -> None:
        """Set the Pango.FontDescription for the GTK3Entry.

        Parameters
        ----------
        font : FontDescription | None
            The font description to apply. If None, the default FontDescription is used.
        """
        _font = font or FontDescription()

        self.dic_attributes["font_description"] = _font
        self.override_font(Pango.FontDescription(_font.to_string()))
