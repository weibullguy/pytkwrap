#       pytkwrap.gtk3.textview.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3TextView module."""

# Standard Library Imports
from datetime import date

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.scrolledwindow import GTK3ScrolledWindow
from pytkwrap.gtk3.widget import GTK3BaseDataWidget, GTK3WidgetProperties


class GTK3TextView(Gtk.TextView, GTK3BaseDataWidget):
    """The GTK3TextView class."""

    # Define private class attributes.
    _DEFAULT_EDIT_SIGNAL: str = "changed"
    _DEFAULT_HEIGHT: int = 100
    _DEFAULT_WIDTH: int = 200
    _GTK3_TEXTVIEW_PROPERTIES = GTK3WidgetProperties(
        accepts_tab=True,
        border_width=0,
        bottom_margin=0,
        buffer=None,
        cursor_visible=True,
        editable=True,
        hadjustment=None,
        hscroll_policy=Gtk.ScrollablePolicy.MINIMUM,
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
        vadjustment=None,
        vscroll_policy=Gtk.ScrollablePolicy.MINIMUM,
        wrap_mode=Gtk.WrapMode.NONE,
    )
    _GTK3_TEXTVIEW_SIGNALS: list[str] = [
        "backspace",
        "copy-clipboard",
        "cut-clipboard",
        "delete-from-cursor",
        "extend-selection",
        "insert-at-cursor",
        "insert-emoji",
        "move-cursor",
        "move-focus-out",
        "paste-clipboard",
        "populate-popup",
        "preedit-changed",
        "select-all",
        "set-anchor",
        "toggle-cursor-visible",
        "toggle-overwrite",
    ]

    def __init__(self, txtbuffer: Gtk.TextBuffer) -> None:
        """Initialize an instance of the GTK3TextView widget.

        Parameters
        ----------
        txtbuffer : Gtk.TextBuffer
            The Gtk.TextBuffer to associate with the GTK3TextView.
        """
        Gtk.TextView.__init__(self)
        GTK3BaseDataWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_TEXTVIEW_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_TEXTVIEW_SIGNALS
        })

        self.default = ""
        self.dic_properties["buffer"] = txtbuffer
        self.tag_bold = self.dic_properties["buffer"].create_tag(
            "bold", weight=Pango.Weight.BOLD
        )
        self.set_buffer(self.dic_properties["buffer"])

        self.scrollwindow = GTK3ScrolledWindow()
        self.scrollwindow.add(self)

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3TextView.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3TextView.
        """
        super().do_set_properties(properties)

        self.set_accepts_tab(self.dic_properties["accepts_tab"])
        self.set_border_width(self.dic_properties["border_width"])
        self.set_bottom_margin(self.dic_properties["bottom_margin"])
        self.set_buffer(self.dic_properties["buffer"])
        self.set_cursor_visible(self.dic_properties["cursor_visible"])
        self.set_editable(self.dic_properties["editable"])
        self.set_hadjustment(self.dic_properties["hadjustment"])
        self.set_hscroll_policy(self.dic_properties["hscroll_policy"])
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
        self.set_vadjustment(self.dic_properties["vadjustment"])
        self.set_vscroll_policy(self.dic_properties["vscroll_policy"])
        self.set_wrap_mode(self.dic_properties["wrap_mode"])

        for _property in [
            "im_module",
            "populate_all",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_update(self, package: dict[str, str]) -> None:
        """Update the GTK3TextView with a new value.

        Parameters
        ----------
        package : dict
            The date package to use to update the GTK3TextView.

        Raises
        ------
        UnkSignalError
            If the signal name is not in the handler_id dict.
        """
        try:
            super().do_update(package)
        except OverflowError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.do_update()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def on_changed(self, __buffer: Gtk.TextBuffer) -> None:
        """Retrieve the data package for the GTK3TextView on value changes.

        This method also sends a PyPubSub message along with the data package for
        listeners to update with the new value.

        Parameters
        ----------
        __buffer : Gtk.TextBuffer
            The Gtk.Buffer whose signal called this method. Unused but required to
            satisfy the Gtk.Widget() callback method structure.

        Raises
        ------
        UnkSignalError
            If the signal name is not in the handler_id dict.
        """
        _package = {self.field: self.do_get_value()}
        try:
            _hid = self.dic_handler_id[self.edit_signal]
            with self.dic_properties["buffer"].handler_block(_hid):
                pub.sendMessage(
                    self.send_topic,
                    node_id=self.record_id,
                    package=_package,
                )
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.on_changed()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def do_get_value(self) -> str:
        """Retrieve the text from the embedded Gtk.TextBuffer.

        Returns
        -------
        text : str
            The text in the Gtk.TextBuffer.
        """
        return self.dic_properties["buffer"].get_text(
            *self.dic_properties["buffer"].get_bounds(), True
        )

    def do_set_value(self, value: bool | date | float | int | str) -> None:
        """Set the GTK3TextView active value.

        Parameters
        ----------
        value : bool | date | float | int | str
            The data to display in the GTK3TextView.
        """
        if value is None:
            value = ""

        self.dic_properties["buffer"].set_text(str(value))

    def _get_signal_owner(self) -> Gtk.TextBuffer:
        """Return the object whose signal handler should be blocked.

        Override in subclasses where the signal is owned by a child object rather than
        the widget itself (e.g. GTK3TextView's TextBuffer).

        Returns
        -------
        object : Gtk.TextBuffer
            The Gtk.TextBuffer associated with the GTK3TextView.
        """
        return self.dic_properties["buffer"]
