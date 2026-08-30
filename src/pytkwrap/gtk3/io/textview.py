"""The pytkwrap GTK3TextView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.text import GTK3TextBuffer


class GTK3TextViewMixin(GTK3ContainerMixin):
    """Mixin class for GTK3TextView.

    Notes
    -----
    GTK3TextView passes no widgets to its callback function.
    """

    _GTK3_TEXTVIEW_ATTRIBUTES = GTK3WidgetAttributes(
        default_value="",
    )
    _GTK3_TEXTVIEW_PROPERTIES = GTK3WidgetProperties(
        accepts_tab=True,
        bottom_margin=0,
        buffer=None,
        cursor_visible=True,
        editable=True,
        im_module=None,
        indent=0,
        input_hints=Gtk.InputHints.NONE,  # pylint: disable=no-member
        input_purpose=Gtk.InputPurpose.FREE_FORM,
        justification=Gtk.Justification.LEFT,
        left_margin=0,
        monospace=False,
        overwrite=False,
        pixels_above_lines=0,
        pixels_below_lines=0,
        pixels_inside_wrap=0,
        populate_all=False,
        right_margin=0,
        tabs=None,
        top_margin=0,
        wrap_mode=Gtk.WrapMode.NONE,
    )
    _GTK3_TEXTVIEW_SIGNALS = [
        "backspace",
        "copy-clipboard",
        "cut-clipboard",
        "delete-from-cursor",
        "extend-selection",
        "insert-at-cursor",
        "insert-emoji",
        "move-cursor",
        "move-viewport",
        "paste-clipboard",
        "populate-popup",
        "preedit-changed",
        "select-all",
        "set-anchor",
        "toggle-cursor-visible",
        "toggle-overwrite",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3TextView mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_TEXTVIEW_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TEXTVIEW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TEXTVIEW_PROPERTIES)

    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
            The value of the requested attribute.
        """
        if attribute in self._GTK3_TEXTVIEW_ATTRIBUTES:
            return self.dic_attributes[attribute]
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: Mapping[str, object]) -> None:
        """Set the values of the GTK3TextView-specific attributes.

        Parameters
        ----------
        attributes : GTK3WidgetAttributes
            The typed dict (preferred) or non-typed dict with the attribute values to
            set for the GTK3TextView.
        """
        # Update the attribute dictionary.
        super().do_set_attributes(attributes)

        for _attr in ["default_value", "edit_signal"]:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3TextView-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3TextView.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_accepts_tab(self.dic_properties["accepts_tab"])
        self.set_bottom_margin(self.dic_properties["bottom_margin"])
        self.set_buffer(self.dic_properties["buffer"])
        self.set_cursor_visible(self.dic_properties["cursor_visible"])
        self.set_editable(self.dic_properties["editable"])
        self.set_indent(self.dic_properties["indent"])
        self.set_input_hints(self.dic_properties["input_hints"])
        self.set_input_purpose(self.dic_properties["input_purpose"])
        self.set_justification(self.dic_properties["justification"])
        self.set_left_margin(self.dic_properties["left_margin"])
        self.set_monospace(self.dic_properties["monospace"])
        self.set_overwrite(self.dic_properties["overwrite"])
        self.set_pixels_above_lines(self.dic_properties["pixels_above_lines"])
        self.set_pixels_below_lines(self.dic_properties["pixels_below_lines"])
        self.set_pixels_inside_wrap(self.dic_properties["pixels_inside_wrap"])
        self.set_right_margin(self.dic_properties["right_margin"])

        if self.dic_properties["tabs"] is not None:
            self.set_tabs(self.dic_properties["tabs"])

        self.set_top_margin(self.dic_properties["top_margin"])
        self.set_wrap_mode(self.dic_properties["wrap_mode"])

        for _property in ["populate_all"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_get_value(self) -> str:
        """Return the value displayed in the GTK3TextView text buffer.

        Returns
        -------
        _value : str
        """
        if self.dic_properties["buffer"] is not None:
            _start = self.dic_properties["buffer"].get_start_iter()
            _end = self.dic_properties["buffer"].get_end_iter()

            return self.dic_properties["buffer"].get_text(_start, _end, True)
        return self.dic_attributes["default_value"]

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3TextView displayed information.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The information to display for the GTK3TextView.
        """
        if not isinstance(value, (float, int, str)) or isinstance(value, bool):
            super().do_set_value(value)

        if self.dic_properties["buffer"] is not None:
            self.dic_properties["buffer"].set_text(str(value))


class GTK3TextView(Gtk.TextView, GTK3TextViewMixin):
    """Wrapper for version 3.0 Gtk.TextView."""

    def __init__(self, buffer: GTK3TextBuffer | None = None) -> None:
        """Initialize an instance of the GTK3TextView.

        Parameters
        ----------
        buffer : GTK3TextBuffer, optional
            The text buffer to use with this instance of the GTK3TextView.  The
            default is None.
        """
        Gtk.TextView.__init__(self, buffer=buffer)
        GTK3TextViewMixin.__init__(self)

        self.dic_properties["buffer"] = buffer
        self.do_set_properties(self.dic_properties)
