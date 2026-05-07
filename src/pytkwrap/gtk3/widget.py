"""The pytkwrap GTK3 Widget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Future Imports
from __future__ import annotations

# Standard Library Imports
from datetime import date

# Third Party Imports
from pubsub import pub  # type: ignore[import-not-found]

# pytkwrap Package Imports
from pytkwrap.common import PyTkWrapMixin
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties
from pytkwrap.utilities import none_to_default


class GTK3Widget(Gtk.Widget, GTK3GObjectMixin, PyTkWrapMixin):
    """Adds GTK3-specific widget attributes."""

    _GTK3_WIDGET_PROPERTIES = GTK3WidgetProperties(
        can_default=False,
        can_focus=False,
        focus_on_click=True,
        halign=Gtk.Align.FILL,
        has_default=False,
        has_focus=False,
        has_tooltip=False,
        height_request=-1,
        hexpand=False,
        hexpand_set=False,
        is_focus=False,
        margin=0,
        margin_bottom=0,
        margin_end=0,
        margin_start=0,
        margin_top=0,
        name="pytkwrap GTK3 widget",
        opacity=1.0,
        parent=None,
        receives_default=False,
        scale_factor=1,
        sensitive=True,
        tooltip_markup="",
        tooltip_text="",
        valign=Gtk.Align.FILL,
        vexpand=False,
        vexpand_set=False,
        visible=False,
        width_request=-1,
        window=None,
    )
    _GTK3_WIDGET_SIGNALS = [
        "destroy",
        "direction-changed",
        "hide",
        "keynav-failed",
        "map",
        "mnemonic-activate",
        "move-focus",
        "query-tooltip",
        "realize",
        "show",
        "state-flags-changed",
        "unmap",
        "unrealize",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3WidgetMixin."""
        Gtk.Widget.__init__(self)
        GTK3GObjectMixin.__init__(self)
        PyTkWrapMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_error_message.update(GTK3GObjectMixin().dic_error_message)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_WIDGET_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_WIDGET_PROPERTIES)
        self.dic_properties["tooltip_markup"] = self._DEFAULT_TOOLTIP
        self.dic_properties["tooltip_text"] = self._DEFAULT_TOOLTIP

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
        if property_name in self._GTK3_WIDGET_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: dict | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | list[list | tuple]
            The typed dict (preferred) or list of lists or list of tuples with the
            property values to set for the GTK3Widget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["height_request"] == 0:
            self.dic_properties["height_request"] = self._DEFAULT_HEIGHT

        if self.dic_properties["width_request"] == 0:
            self.dic_properties["width_request"] = self._DEFAULT_WIDTH

        # We want the tooltip markup and the tooltip text to be the same value.
        if (
            self.dic_properties["tooltip_markup"] == self._DEFAULT_TOOLTIP
            and self.dic_properties["tooltip_text"] != self._DEFAULT_TOOLTIP
        ):
            self.dic_properties["tooltip_markup"] = self.dic_properties["tooltip_text"]

        if (
            self.dic_properties["tooltip_text"] == self._DEFAULT_TOOLTIP
            and self.dic_properties["tooltip_markup"] != self._DEFAULT_TOOLTIP
        ):
            self.dic_properties["tooltip_text"] = self.dic_properties["tooltip_markup"]

        # Set the value of each of the mixin properties.
        self.set_can_default(self.dic_properties["can_default"])
        self.set_can_focus(self.dic_properties["can_focus"])
        self.set_focus_on_click(self.dic_properties["focus_on_click"])
        self.set_halign(self.dic_properties["halign"])  # type: ignore[arg-type]
        self.set_has_tooltip(self.dic_properties["has_tooltip"])
        self.set_hexpand(self.dic_properties["hexpand"])
        self.set_hexpand_set(self.dic_properties["hexpand_set"])
        self.set_margin_bottom(self.dic_properties["margin_bottom"])
        self.set_margin_end(self.dic_properties["margin_end"])
        self.set_margin_start(self.dic_properties["margin_start"])
        self.set_margin_top(self.dic_properties["margin_top"])
        self.set_name(self.dic_properties["name"])
        self.set_opacity(self.dic_properties["opacity"])
        self.set_receives_default(self.dic_properties["receives_default"])
        self.set_sensitive(self.dic_properties["sensitive"])
        self.set_size_request(
            self.dic_properties["width_request"],
            self.dic_properties["height_request"],
        )
        self.set_tooltip_markup(self.dic_properties["tooltip_markup"])
        self.set_tooltip_text(self.dic_properties["tooltip_text"])
        self.set_valign(self.dic_properties["valign"])  # type: ignore[arg-type]
        self.set_vexpand(self.dic_properties["vexpand"])
        self.set_vexpand_set(self.dic_properties["vexpand_set"])
        self.set_visible(self.dic_properties["visible"])

        for _property in ["parent"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_update(
        self,
        package: dict[str, bool | date | float | int | str | None],
    ) -> None:
        """Update the widget with a new value.

        Parameters
        ----------
        package : dict
            The data package to use to update the widget.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for the widget.
        """
        _field, _value = next(iter(package.items()))
        _value = none_to_default(_value, self.dic_attributes["default_value"])

        if _field != self.dic_attributes["field"]:
            return

        try:
            _hid = self.dic_handler_id[self.dic_attributes["edit_signal"]]
            with self._get_signal_owner().handler_block(_hid):
                self.do_set_value(_value)
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.do_update()",
                self.dic_attributes["edit_signal"],
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def on_changed(self, __widget: GTK3Widget) -> None:
        """Retrieve the data package for the widget on value changes.

        This method also sends a PyPubSub message along with the data package for
        listeners to update with the new value.

        Parameters
        ----------
        __widget : GTK3Widget
            The widget that was changed. Unused but required to satisfy the Gtk.Widget()
            callback method structure.

        Raises
        ------
        UnkSignalError
            If the signal name is not valid for this widget.
        """
        _package = {self.dic_attributes["field"]: self.do_get_value()}
        try:
            _hid = self.dic_handler_id[self.dic_attributes["edit_signal"]]
            with self._get_signal_owner().handler_block(_hid):
                pub.sendMessage(
                    self.dic_attributes["send_topic"],
                    node_id=self.dic_attributes["record_id"],
                    package=_package,
                )
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                f"{type(self).__name__}.on_changed()",
                self.dic_attributes["edit_signal"],
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def _get_signal_owner(self) -> GTK3Widget:
        """Return the object whose signal handler should be blocked.

        Override in subclasses where the signal is owned by a child object rather than
        the widget itself (e.g. GTK3TextView's TextBuffer).

        Returns
        -------
        GTK3Widget
        """
        return self
