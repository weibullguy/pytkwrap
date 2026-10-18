"""The pytkwrap GTK3PageSetup module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GLib, Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3PageSetupMixin(GTK3GObjectMixin):
    """Mixin class for GTK3PageSetup.

    Notes
    -----
    GTK3PageSetup passes no widget to its callback functions.
    """

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3PageSetupMixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.file_name: str | None = None
        self.group_name: str | None = None
        self.key_file: GLib.KeyFile | None = None

    def do_save_page_setup(self) -> None:
        """Save page setup options to a file.

        This method is called when the user clicks the "Apply" button in the page setup
        dialog. It saves the current page setup to a file.
        """
        if self.file_name is not None:
            if self.key_file is not None:
                self.to_key_file(self.key_file, self.group_name)
            else:
                self.to_file(self.file_name)


class GTK3PageSetup(Gtk.PageSetup, GTK3PageSetupMixin):
    """Wrapper for version 3.0 Gtk.PageSetup."""

    def __init__(
        self,
        file_name: str | None = None,
        group_name: str | None = None,
    ) -> None:
        """Initialize an instance of the GTK3PageSetup.

        Parameters
        ----------
        file_name : str | None, optional
            The name of the file to load the page setup from. If None, a new
            page setup is created. Defaults to None.
        group_name : str | None, optional
            The name of the group in the file to load the page setup from. If
            None, the default group is used. Defaults to None.
        """
        Gtk.PageSetup.__init__(self)
        GTK3PageSetupMixin.__init__(self)

        if file_name is not None:
            self.file_name = file_name
            if group_name is not None:
                self.group_name = group_name
                self.key_file = GLib.KeyFile()
                self.key_file.load_from_file(  # pylint: disable=no-member
                    self.file_name,
                    GLib.KeyFileFlags.KEEP_COMMENTS
                    | GLib.KeyFileFlags.KEEP_TRANSLATIONS,
                )
                self.load_key_file(self.key_file, self.group_name)
            else:
                self.load_file(self.file_name)
