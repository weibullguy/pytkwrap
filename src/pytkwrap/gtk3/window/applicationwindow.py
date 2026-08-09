"""The pytkwrap GTK3ApplicationWindow module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3WindowMixin


class GTK3ApplicationWindowMixin(GTK3WindowMixin):
    """Mixin class for GTK3ApplicationWindow."""

    _GTK3_APPLICATIONWINDOW_PROPERTIES = GTK3WidgetProperties(
        show_menubar=True,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ApplicationWindow mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_APPLICATIONWINDOW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ApplicationWindow-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ApplicationWindow.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_show_menubar(self.dic_properties["show_menubar"])


class GTK3ApplicationWindow(Gtk.ApplicationWindow, GTK3ApplicationWindowMixin):
    """Wrapper for version 3.0 Gtk.ApplicationWindow."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ApplicationWindow."""
        Gtk.ApplicationWindow.__init__(self)
        GTK3ApplicationWindowMixin.__init__(self)
