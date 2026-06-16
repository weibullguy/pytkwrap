"""The pytkwrap GTK3AboutDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3AboutDialog(Gtk.AboutDialog, GTK3Dialog):
    """Wrapper for version 3.0 Gtk.AboutDialog."""

    _GTK3_ABOUTDIALOG_PROPERTIES = GTK3WidgetProperties(
        artists=[],
        authors=[],
        comments=None,
        copyright=None,
        documenters=[],
        license=None,
        license_type=Gtk.License.UNKNOWN,
        logo=None,
        logo_icon_name="image-missing",
        program_name=None,
        translator_credits=None,
        version=None,
        website=None,
        website_label=None,
        wrap_license=False,
    )
    _GTK3_ABOUTDIALOG_SIGNALS = [
        "activate-link",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3AboutDialog."""
        Gtk.AboutDialog.__init__(self)
        GTK3Dialog.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ABOUTDIALOG_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_ABOUTDIALOG_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3AboutDialog-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3AboutDialog.
        """
        super().do_set_properties(properties)

        self.set_artists(self.dic_properties["artists"])
        self.set_authors(self.dic_properties["authors"])
        self.set_comments(self.dic_properties["comments"])
        self.set_copyright(self.dic_properties["copyright"])
        self.set_documenters(self.dic_properties["documenters"])
        self.set_license(self.dic_properties["license"])
        self.set_license_type(self.dic_properties["license_type"])
        self.set_logo(self.dic_properties["logo"])
        self.set_logo_icon_name(self.dic_properties["logo_icon_name"])

        if self.dic_properties["program_name"] is not None:
            self.set_program_name(self.dic_properties["program_name"])

        self.set_translator_credits(self.dic_properties["translator_credits"])
        self.set_version(self.dic_properties["version"])
        self.set_website(self.dic_properties["website"])

        if self.dic_properties["website_label"] is not None:
            self.set_website_label(self.dic_properties["website_label"])

        self.set_wrap_license(self.dic_properties["wrap_license"])
