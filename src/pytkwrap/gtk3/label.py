#
#       pytkwrap.gtk3.label.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 Label module."""

# Standard Library Imports
from datetime import date

# pytkwrap Package Imports
from pytkwrap.common import DataWidgetAttributes
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseWidget, GTK3WidgetProperties


class GTK3Label(Gtk.Label, GTK3BaseWidget):
    """The GTK3Label class."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 25
    _DEFAULT_WIDTH = 200
    _GTK3_LABEL_ATTRIBUTES = DataWidgetAttributes(
        font_allow_breaks="false",
        font_bgalpha="100%",
        font_bgcolor="white",
        font_family="",
        font_features="",
        font_fgalpha="100%",
        font_fgcolor="black",
        font_gravity="auto",
        font_gravity_hint="natural",
        font_insert_hyphens="false",
        font_lang="en_US",
        font_letter_spacing="",
        font_overline="false",
        font_overline_color="black",
        font_rise="0pt",
        font_scale="",
        font_size="12pt",
        font_stretch="normal",
        font_strikethrough="false",
        font_strikethrough_color="black",
        font_style="normal",
        font_underline="false",
        font_underline_color="black",
        font_variant="normal",
        font_variations="",
        font_weight="normal",
    )
    _GTK3_LABEL_PROPERTIES = GTK3WidgetProperties(
        angle=0.0,
        attributes=None,
        cursor_position=0,
        ellipsize=Pango.EllipsizeMode.NONE,
        justify=Gtk.Justification.LEFT,
        label="",
        lines=-1,
        max_width_chars=-1,
        mnemonic_widget=None,
        pattern="",
        selectable=False,
        single_line_mode=False,
        track_visited_links=True,
        use_markup=False,
        use_underline=False,
        width_chars=-1,
        wrap=False,
        wrap_mode=Pango.WrapMode.WORD,
        xalign=0.05,
        yalign=0.0,
    )
    _GTK3_LABEL_SIGNALS = [
        "activate-current-link",
        "activate-link",
        "copy-clipboard",
        "move-cursor",
        "populate-popup",
    ]

    def __init__(self, text: str) -> None:
        """Initialize an instance of the GTK3Label widget.

        Parameters
        ----------
        text : str
            The text to display in the GTK3Label.
        """
        Gtk.Label.__init__(self)
        GTK3BaseWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_LABEL_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_LABEL_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_LABEL_SIGNALS}
        )

        self.default = "..."
        self.font_allow_breaks: str = "false"
        self.font_bgalpha: str = "100%"
        self.font_bgcolor: str = "white"
        self.font_description = ""
        self.font_family: str = "Sans, Serif, Monospace"
        self.font_features: str = ""
        self.font_fgalpha: str = "100%"
        self.font_fgcolor: str = "black"
        self.font_gravity: str = "auto"
        self.font_gravity_hint: str = "natural"
        self.font_insert_hyphens: str = "true"
        self.font_lang: str = "en_US"
        self.font_letter_spacing: str = ""
        self.font_overline: str = "false"
        self.font_overline_color: str = "black"
        self.font_rise: str = "0pt"
        self.font_scale: str = ""
        self.font_size: str = "12pt"
        self.font_stretch: str = "normal"
        self.font_strikethrough: str = "false"
        self.font_strikethrough_color: str = "black"
        self.font_style: str = "normal"
        self.font_underline: str = "false"
        self.font_underline_color: str = "black"
        self.font_variant: str = "normal"
        self.font_weight: str = "normal"

        self.set_markup(text)
        self.show()

    # ----- ----- Standard widget methods. ----- ----- #
    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | str | None:
        """Get the value of the requested GTK3Label attribute.

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
        try:
            return super().do_get_attribute(attribute)
        except KeyError as exc:
            _valid = {
                "font_allow_breaks",
                "font_bgalpha",
                "font_bgcolor",
                "font_description",
                "font_family",
                "font_features",
                "font_fgalpha",
                "font_fgcolor",
                "font_gravity",
                "font_gravity_hint",
                "font_insert_hyphens",
                "font_lang",
                "font_letter_spacing",
                "font_overline",
                "font_overline_color",
                "font_rise",
                "font_scale",
                "font_size",
                "font_stretch",
                "font_strikethrough",
                "font_strikethrough_color",
                "font_style",
                "font_underline",
                "font_underline_color",
                "font_variant",
                "font_weight",
            }
            if attribute not in _valid:
                raise KeyError(
                    f"Label.do_get_attribute(): Unknown attribute {attribute}."
                ) from exc
            return getattr(self, attribute)

    def do_set_attributes(self, attributes: GTK3DataWidgetAttributes) -> None:  # type: ignore[override]
        """Set the attributes of the GTK3Label.

        Parameters
        ----------
        attributes : GTK3DataWidgetAttributes
            The typed dict with the attribute values to set for the GTK3Label.
        """
        super().do_set_attributes(attributes)

        self.font_allow_breaks = attributes.get("font_allow_breaks", "false")
        self.font_bgalpha = attributes.get("font_bgalpha", "100%")
        self.font_bgcolor = attributes.get("font_bgcolor", "white")
        self.font_family = attributes.get("font_family", "Sans, Serif, Monospace")
        self.font_features = attributes.get("font_features", "")
        self.font_fgalpha = attributes.get("font_fgalpha", "100%")
        self.font_fgcolor = attributes.get("font_fgcolor", "black")
        self.font_gravity = attributes.get("font_gravity", "auto")
        self.font_gravity_hint = attributes.get("font_gravity_hint", "natural")
        self.font_insert_hyphens = attributes.get("font_insert_hyphens", "true")
        self.font_lang = attributes.get("font_lang", "en_US")
        self.font_letter_spacing = attributes.get("font_letter_spacing", "")
        self.font_overline = attributes.get("font_overline", "false")
        self.font_overline_color = attributes.get("font_overline_color", "black")
        self.font_rise = attributes.get("font_rise", "0pt")
        self.font_scale = attributes.get("font_scale", "")
        self.font_size = attributes.get("font_size", "12pt")
        self.font_stretch = attributes.get("font_stretch", "normal")
        self.font_strikethrough = attributes.get("font_strikethrough", "false")
        self.font_strikethrough_color = attributes.get(
            "font_strikethrough_color",
            "black",
        )
        self.font_style = attributes.get("font_style", "normal")
        self.font_underline = attributes.get("font_underline", "false")
        self.font_underline_color = attributes.get("font_underline_color", "black")
        self.font_variant = attributes.get("font_variant", "normal")
        self.font_weight = attributes.get("font_weight", "normal")

    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3Label.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3Label.
        """
        super().do_set_properties(properties)

        self.set_angle(self.dic_properties["angle"])
        self.set_attributes(self.dic_properties["attributes"])
        self.set_ellipsize(self.dic_properties["ellipsize"])
        self.set_justify(self.dic_properties["justify"])
        self.set_label(self.dic_properties["label"])
        self.set_line_wrap(self.dic_properties["wrap"])
        self.set_line_wrap_mode(self.dic_properties["wrap_mode"])
        self.set_lines(self.dic_properties["lines"])
        self.set_markup(self.dic_properties["label"])
        self.set_markup_with_mnemonic(self.dic_properties["label"])
        self.set_max_width_chars(self.dic_properties["max_width_chars"])
        self.set_mnemonic_widget(self.dic_properties["mnemonic_widget"])
        self.set_pattern(self.dic_properties["pattern"])
        self.set_selectable(self.dic_properties["selectable"])
        self.set_single_line_mode(self.dic_properties["single_line_mode"])
        self.set_text(self.dic_properties["label"])
        self.set_text_with_mnemonic(self.dic_properties["label"])
        self.set_track_visited_links(self.dic_properties["track_visited_links"])
        self.set_use_markup(self.dic_properties["use_markup"])
        self.set_use_underline(self.dic_properties["use_underline"])
        self.set_width_chars(self.dic_properties["width_chars"])
        self.set_xalign(self.dic_properties["xalign"])
        self.set_yalign(self.dic_properties["yalign"])

        if self.dic_properties["justify"] == Gtk.Justification.CENTER:
            self.set_xalign(0.5)
        elif self.dic_properties["justify"] == Gtk.Justification.LEFT:
            self.set_xalign(0.05)
        else:
            self.set_xalign(0.95)

    def do_update(
        self,
        package: dict[str, bool | date | float | int | str | None],
    ) -> None:
        """Update the GTK3Label to a new value.

        Parameters
        ----------
        package : dict
            The data package to use to update the GTK3Label.
        """
        _field, _raw_value = next(iter(package.items()))
        _value = str(_raw_value)

        if _field != self.field or _value == "None":
            return

        if self.dic_properties["use_markup"]:
            self.dic_properties["label"] = f"{self.font_description}{_value}</span>"
            if self.dic_properties["use_underline"]:
                self.set_markup_with_mnemonic(_value)
                return

            self.set_markup(_value)
            return

        if self.dic_properties["use_underline"]:
            self.set_text_with_mnemonic(_value)
            return

        # Setting the text will overwrite any text in the label, clear any mnemonic
        # accelerators, set use_markup=False, and set use_underline=False.
        self.set_text(_value)

    # ----- ----- Label specific methods. ----- ----- #
    def do_set_font_description(self) -> None:
        """Set the font description for the GTK3Label."""
        # TODO: Fix this so existing font description is updated/overwritten even if
        #  it's not blank.
        if not self.font_description:
            self.font_description = (
                f"<span allow_breaks={self.font_allow_breaks} "
                f"bgalpha={self.font_bgalpha} bgcolor={self.font_bgcolor} "
                f"face={self.font_family} font_features={self.font_features} "
                f"fgalpha={self.font_fgalpha} fgcolor={self.font_fgcolor} "
                f"gravity={self.font_gravity} gravity_hint={self.font_gravity_hint} "
                f"insert_hyphen={self.font_insert_hyphens} lang={self.font_lang} "
                f"letter_spacing={self.font_letter_spacing} "
                f"overline={self.font_overline} "
                f"overline_color={self.font_overline_color} rise={self.font_rise} "
                f"font_scale={self.font_scale} size={self.font_size} "
                f"stretch={self.font_stretch} strikethrough={self.font_strikethrough} "
                f"strikethrough_color={self.font_strikethrough_color} "
                f"style={self.font_style} underline={self.font_underline} "
                f"underline_color={self.font_underline_color} "
                f"variant={self.font_variant} weight={self.font_weight}"
            )


def do_make_label_group(
    label_text: list[str],
) -> tuple[int, list[GTK3Label]]:
    """Make and place a group of Labels.

    The width of each label is set using a natural request.  This ensures the label
    doesn't cut off letters.  The maximum size of the labels is determined and used to
    set the left position of widget displaying the data described by the label.  This
    ensures everything lines up.  It also returns a list of y-coordinates indicating the
    placement of each label that is used to place the corresponding widget.

    Parameters
    ----------
    label_text : list
        List of the text strings for each label.

    Returns
    -------
    (_max_x, _lst_labels) : tuple
        The width of the label with the longest text and a list of the GTK3Label
        instances.
    """
    _lst_labels = []
    _max_x = 0

    _char_width = max(len(_label_text) for _label_text in label_text)

    for _label_text in label_text:
        _label = GTK3Label(_label_text)
        _label.set_width_chars(_char_width)
        _max_x = max(_max_x, _label.get_preferred_size()[0].width)
        _lst_labels.append(_label)

    return _max_x, _lst_labels
