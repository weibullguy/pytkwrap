"""The pytkwrap GTK3AppChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3AppChooserDialogMixin(GTK3DialogMixin):
    """Mixin class for GTK3AppChooserDialog.

    Notes
    -----
    GTK3AppChooserDialog passes no widgets to its callback function.
    """

    _GTK3_APPCHOOSERDIALOG_PROPERTIES = GTK3WidgetProperties(
        gfile=None,
        heading=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3AppChooserDialog mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_APPCHOOSERDIALOG_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3AppChoosertDialog-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3AppChooserDialog.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["heading"] is not None:
            self.set_heading(self.dic_properties["heading"])


class GTK3AppChooserDialog(Gtk.AppChooserDialog, GTK3AppChooserDialogMixin):
    """Wrapper for version 3.0 Gtk.AppChooserDialog."""

    def __init__(
        self,
        transient_for: Gtk.Window | None,
        flags: Gtk.DialogFlags,
        gfile: Gio.File = None,
    ) -> None:
        """Initialize an instance of the GTK3AppChooserDialog.

        Parameter
        ---------
        transient_for : Gtk.Window | None
            The parent window for the Gtk.AppChooserDialog.
        flags : Gtk.DialogFlags
            THe flags to use for the Gtk.AppChooserDialog.
        gfile : Gio.File | None
            The Gio.File to be used by the Gtk.AppChooserDialog.
        """
        Gtk.AppChooserDialog.__init__(
            self,
            transient_for=transient_for,
            flags=flags,
            gfile=gfile,
        )
        GTK3AppChooserDialogMixin.__init__(self)

        self.dic_properties["gfile"] = gfile
