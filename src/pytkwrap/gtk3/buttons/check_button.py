# -*- coding: utf-8 -*-
#
#       pytkwrap.gtk3.buttons.check_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 CheckButton module."""

# Standard Library Imports
from typing import Dict

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3.widget import GTK3BaseWidget, GTK3WidgetProperties
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3BaseButton


class GTK3CheckButton(Gtk.CheckButton, GTK3BaseButton):
    """The CheckButton class."""

    # Define private class attributes.
    _CHECK_BUTTON_PROPERTIES = GTK3WidgetProperties(
        active=False,
        draw_indicator=False,
        inconsistent=False,
    )
    _CHECK_BUTTON_SIGNALS = ["toggled"]
    _DEFAULT_EDIT_SIGNAL = "toggled"
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200

    def __init__(self, label: str = "") -> None:
        """Initialize an instance of the CheckButton widget.

        :param label: the text to display with the Gtk.CheckButton. Default is an empty
            string.
        """
        Gtk.CheckButton.__init__(self)
        GTK3BaseButton.__init__(self, label=label)

        # Initialize public instance attributes.
        self.dic_properties.update(self._CHECK_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._CHECK_BUTTON_SIGNALS}
        )

        self.default = False

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the CheckButton.

        :param properties: the WidgetProperties dict with the property values to set for
            the CheckButton.
        """
        super().do_set_properties(properties)

        self.dic_properties["active"] = properties.get("active", False)
        self.dic_properties["draw_indicator"] = properties.get("draw_indicator", False)
        self.dic_properties["inconsistent"] = properties.get("inconsistent", False)

        self.set_active(self.dic_properties["active"])
        self.set_inconsistent(self.dic_properties["inconsistent"])

        for _property in [
            "draw_indicator",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_update(self, package: Dict[str, bool]) -> None:
        """Update the CheckButton with a new value.

        :param package: the date package to use to update the CheckButton.
        """
        _field, _value = next(iter(package.items()))

        if _field != self.field:
            return

        if _value is None:
            self.set_active(False)
            return

        try:
            _hid = self.dic_handler_id.get(self.edit_signal, -1)
            with self.handler_block(_hid):
                self.set_active(_value)
        except (KeyError, OverflowError) as exc:
            _error_msg = self.dic_error_message["unk_signal"].format(
                "CheckButton.do_update()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc

    def on_changed(self, __checkbutton: GTK3BaseWidget) -> None:
        """Retrieve the data package for the CheckButton on value changes.

        This method also sends a PyPubSub message along with the data package for
        listeners to update with the new value.

        :param __checkbutton: the CheckButton whose signal called this method. Unused
            but required to satisfy the Gtk.CheckButton() callback method structure.
        """
        _package = {self.field: self.get_active()}
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
                "CheckButton.on_changed()",
                self.edit_signal,
            )
            pub.sendMessage(
                "do_log_error",
                message=_error_msg,
            )
            raise UnkSignalError(_error_msg) from exc
