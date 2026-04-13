# -*- coding: utf-8 -*-
#
#       pytkwrap.gtk3.buttons.file_chooser_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The FileChooserButton module."""

from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.widget import GTK3WidgetProperties
from pytkwrap.gtk3.buttons import GTK3BaseButton


class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3BaseButton):
    """The FileChooserButton class."""

    # Define private class attributes.
    _DEFAULT_EDIT_SIGNAL = "file-set"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _FILE_CHOOSER_BUTTON_PROPERTIES = GTK3WidgetProperties(
        action=Gtk.FileChooserAction.OPEN,
        create_folders=True,
        dialog=None,
        do_overwrite_confirmation=False,
        extra_widget=None,
        filter=None,
        local_only=True,
        preview_widget=None,
        preview_widget_active=True,
        select_multiple=False,
        show_hidden=False,
        title="Select a File",
        use_preview_label=True,
        width_chars=-1,
    )
    _FILE_CHOOSER_BUTTON_SIGNALS = [
        "confirm-overwrite",
        "current-folder-changed",
        "file-activated",
        "file-set",
        "selection-changed",
        "update-preview",
    ]

    def __init__(self, label: str = "...") -> None:
        """Initialize an instance of the FileChooserButton widget.

        :param label: the text for the FileChooserButton label.
        """
        Gtk.FileChooserButton.__init__(
            self,
            title="Select a File",
            action=Gtk.FileChooserAction.OPEN,
        )
        GTK3BaseButton.__init__(self, label=label)

        # Initialize public instance attributes.
        self.dic_properties.update(self._FILE_CHOOSER_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._FILE_CHOOSER_BUTTON_SIGNALS}
        )

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the FileChooserButton.

        :param properties: the WidgetProperties dict with the property values to set for
            the FileChooserButton.
        """
        super().do_set_properties(properties)

        self.dic_properties["action"] = properties.get(
            "action", Gtk.FileChooserAction.OPEN
        )
        self.dic_properties["create_folders"] = properties.get("create_folders", True)
        self.dic_properties["do_overwrite_confirmation"] = properties.get(
            "do_overwrite_confirmation", False
        )
        self.dic_properties["extra_widget"] = properties.get("extra_widget", None)
        self.dic_properties["filter"] = properties.get("filter", None)
        self.dic_properties["local_only"] = properties.get("local_only", True)
        self.dic_properties["preview_widget"] = properties.get("preview_widget", None)
        self.dic_properties["preview_widget_active"] = properties.get(
            "preview_widget_active", True
        )
        self.dic_properties["select_multiple"] = properties.get(
            "select_multiple", False
        )
        self.dic_properties["show_hidden"] = properties.get("show_hidden", False)
        self.dic_properties["title"] = properties.get("title", "Select a File")
        self.dic_properties["use_preview_label"] = properties.get(
            "use_preview_label", True
        )
        self.dic_properties["width_chars"] = properties.get("width_chars", -1)

        self.set_action(self.dic_properties["action"])
        self.set_create_folders(self.dic_properties["create_folders"])
        self.set_do_overwrite_confirmation(
            self.dic_properties["do_overwrite_confirmation"]
        )
        self.set_extra_widget(self.dic_properties["extra_widget"])
        self.set_filter(self.dic_properties["filter"])
        self.set_local_only(self.dic_properties["local_only"])
        self.set_preview_widget(self.dic_properties["preview_widget"])
        self.set_preview_widget_active(self.dic_properties["preview_widget_active"])
        self.set_select_multiple(self.dic_properties["select_multiple"])
        self.set_show_hidden(self.dic_properties["show_hidden"])
        self.set_title(self.dic_properties["title"])
        self.set_use_preview_label(self.dic_properties["use_preview_label"])
        self.set_width_chars(self.dic_properties["width_chars"])
