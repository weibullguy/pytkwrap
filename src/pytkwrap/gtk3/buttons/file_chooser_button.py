#       pytkwrap.gtk3.buttons.file_chooser_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The GTK3FileChooserButton module."""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.buttons.base_button import GTK3BaseButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties
from pytkwrap.utilities import dir_exists, file_exists, get_home_directory


class GTK3FileChooserButton(
    Gtk.FileChooserButton,
    GTK3BaseButton,
):  # ty:ignore[inconsistent-mro]
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

        Notes
        -----
        The `default` attribute controls the return type of `do_get_value` and the
        input type for `do_set_value`:
            - "path" (default): use absolute path string(s).
            - "uri": use URI string(s).
            - "gio": use Gio.File object(s).
        Set via do_set_attributes(GTK3DataWidgetAttributes(default="path")
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

        self.default = "path"

    # ----- ----- ----- ----- --- Standard widget methods. --- ----- ----- ----- ----- #
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

    # ----- ----- ----- -- File Chooser Button specific methods. -- ----- ----- ----- #
    # pylint: disable-next=line-too-long,too-many-return-statements
    def do_get_value(self) -> str | list[str] | Gio.File | list[Gio.File] | None:  # type: ignore[override] # noqa: PLR0911
        """Retrieve the selected file name(s) from the GTK3FileChooserButton.

        The value(s) will always be returned as absolute paths.

        Returns
        -------
        str | list[str] |  None
            The selected file(s) or folder from the GTK3FileChooserButton.
        """
        _action = self.dic_properties["action"]
        _select_multiple = self.dic_properties["select_multiple"]

        if self.default == "gio":
            return self.get_gio_value()

        if self.default == "uri":
            return self.get_uri_value()

        # Default to absolute path strings.
        if _action in {
            Gtk.FileChooserAction.CREATE_FOLDER,
            Gtk.FileChooserAction.SELECT_FOLDER,
        }:
            return self.get_current_folder()

        if _action == Gtk.FileChooserAction.OPEN:
            if _select_multiple:
                return self.get_filenames()
            return self.get_filename()

        if _action == Gtk.FileChooserAction.SAVE:
            return self.get_filename()

        return None

    # TODO: Handle select_multiple=True case — requires calling select_filename() in a
    #  loop for each file in the list.
    # pylint: disable-next=line-too-long
    def do_set_value(self, value: str | Gio.File | None) -> None:  # type: ignore[override]
        """Set the GTK3FileChooserButton active value.

        Parameters
        ----------
        value : str | None
            The file name for the GTK3FileChooserButton to select.
        """
        _action = self.dic_properties["action"]
        _create_folders = self.dic_properties["create_folders"]

        if self.default == "gio" and value is not None:
            self.set_file(value)
            return

        if self.default == "uri":
            self.set_uri(value or "")
            return

        # Default to absolute path strings.
        if _action in {
            Gtk.FileChooserAction.OPEN,
            Gtk.FileChooserAction.SAVE,
        }:
            if value is not None and file_exists(value):
                self.set_filename(value)
            else:
                self.set_current_name(value or "Untitled")
        elif _action in {
            Gtk.FileChooserAction.SELECT_FOLDER,
            Gtk.FileChooserAction.CREATE_FOLDER,
        }:
            if value is not None and (dir_exists(value) or _create_folders):
                self.set_current_folder(value)
            else:
                self.set_current_folder(get_home_directory())

    def get_gio_value(self) -> Gio.File | list[Gio.File] | None:
        """Retrieve the selected file name(s) selected as Gio.File objects.

        Returns
        -------
        Gio.File | list[Gio.File] |  None
            The selected file(s) or folder from the GTK3FileChooserButton as Gio.File
            object(s).
        """
        _select_multiple = self.dic_properties["select_multiple"]

        if _select_multiple:
            return list(self.get_files())
        return self.get_file()

    def get_uri_value(self) -> str | list[str] | None:
        """Retrieve the file name(s) selected in the GTK3FileChooserButton as URIs.

        Returns
        -------
        str | list[str] |  None
            The selected file(s) or folder from the GTK3FileChooserButton as URIs.
        """
        _select_multiple = self.dic_properties["select_multiple"]

        if _select_multiple:
            return self.get_uris()
        return self.get_uri()
