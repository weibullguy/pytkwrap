"""The pytkwrap GTK3FileChooserWidget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FileChooserWidget(Gtk.FileChooserWidget, GTK3Box):
    """Wrapper for version 3.0 Gtk.FileChooserWidget."""

    _GTK3_FILECHOOSERWIDGET_PROPERTIES = GTK3WidgetProperties(
        search_mode=False,
    )
    _GTK3_FILECHOOSERWIDGET_SIGNALS = [
        "desktop-folder",
        "down-folder",
        "home-folder",
        "location-popup",
        "location-popup-on-paste",
        "location-toggle-popup",
        "places-shortcut",
        "quick-bookmark",
        "recent-shortcut",
        "search-shortcut",
        "show-hidden",
        "up-folder",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FileChooserWidget."""
        Gtk.FileChooserWidget.__init__(self)
        GTK3Box.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_FILECHOOSERWIDGET_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_FILECHOOSERWIDGET_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3FileChooserWidget-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTKFileChooserWidget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["search_mode"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
