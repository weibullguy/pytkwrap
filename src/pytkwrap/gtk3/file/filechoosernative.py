"""The pytkwrap GTK3FileChooserNative module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.nativedialog import GTK3NativeDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FileChooserNative(Gtk.FileChooserNative, GTK3NativeDialog):
    """Wrapper for version 3.0 Gtk.FileChooserNative."""

    _GTK3_FILECHOOSERNATIVE_PROPERTIES = GTK3WidgetProperties(
        accept_label=None,
        cancel_label=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FileChooserNative."""
        Gtk.FileChooserNative.__init__(self)
        GTK3NativeDialog.__init__(self)

        self.dic_properties.update(self._GTK3_FILECHOOSERNATIVE_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3FileChooserNative-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTKFileChooserNative.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_accept_label(self.dic_properties["accept_label"])
        self.set_cancel_label(self.dic_properties["cancel_label"])
