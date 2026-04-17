#       pytkwrap.gtk3.buttons.file_chooser_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The GTK3FileChooserButton module."""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3BaseButton):
    """The GTK3FileChooserButton class."""

    # Define private class attributes.
    _DEFAULT_EDIT_SIGNAL = "file-set"
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_FILE_CHOOSER_BUTTON_PROPERTIES = GTK3WidgetProperties(
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
    _GTK3_FILE_CHOOSER_BUTTON_SIGNALS = [
        "confirm-overwrite",
        "current-folder-changed",
        "file-activated",
        "file-set",
        "selection-changed",
        "update-preview",
    ]

    def __init__(self, label: str = "...") -> None:
        """Initialize an instance of the GTK3FileChooserButton widget.

        Parameters
        ----------
        label : str
            The text for the GTK3FileChooserButton label.
        """
        Gtk.FileChooserButton.__init__(
            self,
            title="Select a File",
            action=Gtk.FileChooserAction.OPEN,
        )
        GTK3BaseButton.__init__(self, label=label)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_FILE_CHOOSER_BUTTON_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_FILE_CHOOSER_BUTTON_SIGNALS
        })

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the GTK3FileChooserButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the
            GTK3FileChooserButton.
        """
        super().do_set_properties(properties)

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

    # ----- ----- File Chooser Button specific methods. ----- ----- #
    # TODO: Make this use one of get_current_folder(), get_current_folder_file(),
    #  get_current_folder_uri(), get_current_name(), get_file(), get_filename(),
    #  get_filenames(), get_files(), get_uri(), or get_uris()depending on the value of
    #  action, create_folder, local_only and select_multiple properties.
    def do_get_value(self) -> str | None:  # type: ignore[override]
        """Retrieve the file name selected in the GTK3FileChooserButton.

        Returns
        -------
        str | None
            The file name selected in the GTK3FileChooserButton as an absolute path.
        """
        # if self.do_get_attribute("action") == Gtk.FileChooserAction.OPEN:
        # if self.do_get_attribute("select_multiple"):
        # Here we can use get_filenames() -> [str], get_files() -> [Gio.File], or
        # get_uris() -> [str].
        # else:
        # Here we can use get_current_name() -> str, get_file() -> Gio.File,
        # get_filename() -> str,
        # if self.do_get_attribute("action") == Gtk.FileChooserAction.SELECT_FOLDER:
        # Here we can use get_current_folder() -> str, get_current_folder_file()
        # -> Gio.File, or get_current_folder_uri() -> str.
        return self.get_filename()

    # TODO: Make this use one of set_current_folder_file(), set_current_name(),
    #  set_file(), set_filename(), or set_uri() depending on the value of action and
    #  create_folder properties.
    def do_set_value(self, value: str | None) -> None:
        """Set the GTK3FileChooserButton active value.

        Parameters
        ----------
        value : str | None
            The file name for the GTK3FileChooserButton to select.
        """
        if value is None:
            value = "Untitled"

        # if self.do_get_attribute("action") == Gtk.FileChooserAction.OPEN:
        # if file_exists(value):
        # Here we can use set_current_name(str), set_file(Gio.File), or set_filenane(
        # str)
        # else:
        # Here we can use set_current_name("Untitled").
        # if self.do_get_attribute("action") == Gtk.FileChooserAction.SAVE:
        # if file_exists(value):
        # Here we can use set_file(Gio.File), set_filename(str), or set_uri(str).
        # else:
        # self.set_current_name(value)
        # if self.do_get_attribute("action") == Gtk.FileChooserAction.SELECT_FOLDER:
        # Here we can use set_current_folder_file(Gio.File).
        # if self.do_get_attribute("action") == Gtk.FileChooserAction.CREATE_FOLDER:
        # if self.get_property("create_folders"):
        # Here we can use set_current_folder_file(Gio.File).
        self.set_filename(value)
