"""The pytkwrap GTK3ColorChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3Dialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ColorChooserDialog(Gtk.ColorChooserDialog, GTK3Dialog):
    """Wrapper for version 3.0 Gtk.ColorChooserDialog."""

    _GTK3_COLORCHOOSERDIALOG_PROPERTIES = GTK3WidgetProperties(
        show_editor=False,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorChooserDialog."""
        Gtk.ColorChooserDialog.__init__(self)
        GTK3Dialog.__init__(self)

        self.dic_properties.update(self._GTK3_COLORCHOOSERDIALOG_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ColorChooserDialog-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ColorChooserDialog.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["show_editor"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
