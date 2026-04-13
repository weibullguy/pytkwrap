# -*- coding: utf-8 -*-
#
#       pytkwrap.gtk3.buttons.color_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The ColorButton module."""

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, Gtk, _
from pytkwrap.gtk3.buttons import GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3BaseWidget, GTK3WidgetProperties


class GTK3ColorButton(Gtk.ColorButton, GTK3BaseButton):
    """The ColorButton class."""

    # Define private class attributes.
    _COLOR_BUTTON_PROPERTIES = GTK3WidgetProperties(
        alpha=65535,
        rgba=None,
        show_editor=False,
        title="Pick a Color",
        use_alpha=True,
    )
    _COLOR_BUTTON_SIGNALS = [
        "color-activated",
        "color-set",
    ]
    _DEFAULT_EDIT_SIGNAL = "color-set"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60

    def __init__(self) -> None:
        """Initialize an instance of the ColorButton widget."""
        Gtk.ColorButton.__init__(self)
        BaseButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._COLOR_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._COLOR_BUTTON_SIGNALS}
        )

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the ColorButton.

        :param properties: the WidgetProperties dict with the property values to set for
            the ColorButton.
        """
        super().do_set_properties(properties)

        self.dic_properties["rgba"] = properties.get(
            "rgba",
            Gdk.RGBA(red=1.0, green=1.0, blue=1.0, alpha=1.0),
        )
        self.dic_properties["show_editor"] = properties.get("show_editor", False)
        self.dic_properties["title"] = properties.get("title", _("Pick a Color"))
        self.dic_properties["use_alpha"] = properties.get("use_alpha", True)

        self.set_rgba(self.dic_properties["rgba"])
        self.set_title(self.dic_properties["title"])
        self.set_use_alpha(self.dic_properties["use_alpha"])

        for _property in [
            "show_editor",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_update(self, package: dict[str, Gdk.RGBA]) -> None:
        """Update the ColorButton with a new value.

        :param package: the date package to use to update the ColorButton.
        """
        _field, _value = next(iter(package.items()))

        if _field != self.field:
            return

        if _value is None:
            _value = Gdk.RGBA(1.0, 1.0, 1.0, 1.0)

        try:
            _hid = self.dic_handler_id.get(self.edit_signal, -1)
            with self.handler_block(_hid):
                self.set_rgba(_value)
        except (KeyError, OverflowError) as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                "ColorButton.do_update()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def on_changed(self, __colorbutton: GTK3BaseWidget) -> None:
        """Retrieve the data package for the ColorButton on value changes.

        This method also sends a PyPubSub message along with the data package for
        listeners to update with the new value.

        :param __colorbutton: the ColorButton whose signal called this method. Unused
            but required to satisfy the Gtk.ColorButton() callback method structure.
        """
        _package = {self.field: self.get_rgba()}
        try:
            _hid = self.dic_handler_id[self.edit_signal]
            with self.handler_block(_hid):
                pub.sendMessage(
                    self.send_topic,
                    node_id=self.record_id,
                    package=_package,
                )
        except KeyError as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                "ColorButton.on_changed()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc
