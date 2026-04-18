# pytkwrap.gtk3.entry.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 Entry module."""

# Standard Library Imports
from datetime import date, datetime

# pytkwrap Package Imports
from pytkwrap.common import WidgetAttributes
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseDataWidget, GTK3WidgetProperties


class GTK3Entry(Gtk.Entry, GTK3BaseDataWidget):  # ty:ignore[inconsistent-mro]
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
    _DEFAULT_EDIT_SIGNAL: str = "changed"
    _DEFAULT_HEIGHT: int = 25
    _DEFAULT_WIDTH: int = 200
    _GTK3_ENTRY_ATTRIBUTES = GTK3DataWidgetAttributes(
        font_description=None,
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
        inner_border=None,
        input_hints=Gtk.InputHints.NONE,  # pylint: disable=no-member
        input_purpose=Gtk.InputPurpose.FREE_FORM,
        invisible_char="*",
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
        primary_icon_storage_type=Gtk.ImageType.EMPTY,
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
        secondary_icon_storage_type=Gtk.ImageType.EMPTY,
        secondary_icon_tooltip_markup=None,
        secondary_icon_tooltip_text=None,
        selection_bound=0,
        shadow_type=Gtk.ShadowType.IN,
        show_emoji_icon=False,
        tabs=None,
        text="",
        text_length=0,
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
        font_description: Pango.FontDescription | str | None = None,
    ) -> None:
        """Initialize an instance of the GTK3Entry widget.

        Parameters
        ----------
        font_description : Pango.FontDescription or str or None
            The font description for the font used by the GTK3Entry.
        """
        Gtk.Entry.__init__(self)
        GTK3BaseDataWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_ENTRY_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_ENTRY_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_ENTRY_SIGNALS
        })

        self.default = ""
        self.font_description = font_description

        self.show()

    # ----- ----- Standard widget methods. ----- ----- #
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
        if attribute in self._GTK3_ENTRY_ATTRIBUTES:
            return getattr(self, attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the attributes of the Entry.

        Parameters
        ----------
        attributes : GTK3DataWidgetAttributes
            The typed dict with the attribute values to set for the GTK3Entry.
        """
        super().do_set_attributes(attributes)

        self.font_description = attributes.get(
            "font_description",
            self.font_description,
        )

        if self.font_description is not None:
            self.override_font(self.font_description)

    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
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
        self.set_inner_border(self.dic_properties["inner_border"])
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
            "shadow_type",
            "show_emoji_icon",
            "truncate_multiline",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    # ----- ----- Entry specific methods. ----- ----- #
    def do_get_value(self) -> float | int | str | None:  # type: ignore[override]
        """Retrieve the text displayed in the GTK3Entry.

        This method will return the correct datatype (float, int, str) associated with
        the database field associated with the GTK3Entry.

        Returns
        -------
        float | int | str | None
            The value displayed in the GTK3Entry.
        """
        _value: float | int | str | None = self.get_text()

        if self.datatype == "gfloat":
            _value = float(_value)
        elif self.datatype == "gint":
            _value = int(_value)
        elif self.datatype == "gchararray":
            _value = str(_value)

        return _value

    # TODO: Consider passing a dict or use **kwargs rather than eight keywords.
    def do_set_font_description(  # pylint: disable=too-many-positional-arguments
        self,
        family: str = "Sans, Serif, Monospace",
        gravity: str = "Not Rotated",
        size: int = 10,
        stretch: str = "",
        style: str = "Normal",
        variant: str = "",
        weight: str = "Regular",
    ) -> None:
        """Set the Pango.FontDescription for the GTK3Entry.

        :param family: comma separated list of fonts.
        :param gravity:
        :param size:
        :param stretch:
        :param style:
        :param variant:
        :param weight:
        """
        _font_description: str = (
            f"{family} {gravity} {stretch} {style} {variant} {weight} {size}"
        )

        self.do_set_attributes(
            GTK3DataWidgetAttributes(
                font_description=Pango.FontDescription(_font_description),
            )
        )

    def do_set_value(self, value: bool | date | float | int | str) -> None:
        """Set the GTK3Entry active value.

        Parameters
        ----------
        value : bool | date | float | int | str
            The data to display in the GTK3Entry.
        """
        if value is None:
            value = ""

        if isinstance(value, date):
            value = datetime.strftime(value, "%Y-%m-%d")

        self.set_text(str(value))
