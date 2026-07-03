"""The pytkwrap GTK3TextView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from types import FunctionType

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class GTK3TextView(Gtk.TextView, GTK3Container):
    """Wrapper for version 3.0 Gtk.TextView."""

    _GTK3_TEXTVIEW_ATTRIBUTES = GTK3WidgetAttributes(
        default_value="",
        edit_signal="changed",
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

    def __init__(self, buffer: Gtk.TextBuffer | None = None) -> None:
        """Initialize an instance of the GTK3TextView."""
        Gtk.TextView.__init__(self, buffer=buffer)
        GTK3Container.__init__(self)

        self.dic_attributes.update(self._GTK3_TEXTVIEW_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TEXTVIEW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TEXTVIEW_PROPERTIES)

        self.buffer = buffer

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
        super().do_set_attributes(attributes)

        for _attr in ["default_value", "edit_signal"]:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

    def do_set_callbacks(
        self,
        signal: list[str] | str,
        callback: FunctionType,
        after: bool = False,
    ) -> None:
        """Set the callback method for the GTK3TextView.

        Parameters
        ----------
        signal : list[str] | str
            The name of the signal to connect the callback to.
        callback : FunctionType
            The callback function or method to connect to the signal.
        after : bool
            Indicates whether the handler is added to the signal handler list before
            (default) or after the default class signal handler.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for this widget.
        """
        if not isinstance(signal, list):
            signal = [signal]

        # TODO: Change this once the wrapper for Gtk.TextBuffer() is complete.
        # self.buffer.do_set_callbacks(signal)
        # Then remove all below.
        for _signal in signal:
            try:
                super().do_set_callbacks(signal, callback, after=after)
            except UnkSignalError:
                try:
                    if after and self.buffer is not None:
                        self.dic_handler_id[_signal] = self.buffer.connect_after(
                            _signal,
                            callback,
                        )
                    elif self.buffer is not None:
                        self.dic_handler_id[_signal] = self.buffer.connect(
                            _signal,
                            callback,
                        )
                except TypeError as exc:
                    _error_msg = self.dic_error_message["unk_signal"].format(
                        f"{type(self).__name__}.do_set_callbacks()",
                        _signal,
                    )
                    pub.sendMessage(
                        "do_log_error",
                        message=_error_msg,
                    )
                    raise UnkSignalError(_error_msg) from exc

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
        if self.buffer is not None:
            _start = self.buffer.get_start_iter()
            _end = self.buffer.get_end_iter()

            return self.buffer.get_text(_start, _end, True)
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

        if self.buffer is not None:
            self.buffer.set_text(str(value))
