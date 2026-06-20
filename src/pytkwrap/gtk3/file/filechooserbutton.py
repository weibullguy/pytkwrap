"""The pytkwrap GTK3FileChooserButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3Box):
    """Wrapper for version 3.0 Gtk.FileChooserButton."""

    _GTK3_FILECHOOSERBUTTON_PROPERTIES = GTK3WidgetProperties(
        dialog=None,
        title="Select a File",
        width_chars=-1,
    )
    _GTK3_FILECHOOSERBUTTON_SIGNALS = ["file-set"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FileChooserButton."""
        Gtk.FileChooserButton.__init__(self)
        GTK3Box.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_FILECHOOSERBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_FILECHOOSERBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3FileChooserButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3FileChooserButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_title(self.dic_properties["title"])
        self.set_width_chars(self.dic_properties["width_chars"])
