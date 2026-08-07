"""The pytkwrap GTK3ShortcutsWindow module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3WindowMixin


class GTK3ShortcutsWindowMixin(GTK3WindowMixin):
    """Mixin class for GTK3ShortcutsWindow."""

    _GTK3_SHORTCUTSWINDOW_PROPERTIES = GTK3WidgetProperties(
        section_name="internal-search",
        view_name=None,
    )
    _GTK3_SHORTCUTSWINDOW_SIGNALS = [
        "close",
        "search",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ShortcutsWindow mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SHORTCUTSWINDOW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SHORTCUTSWINDOW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Window-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Window.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["section_name", "view_name"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )


class GTK3ShortcutsWindow(Gtk.ShortcutsWindow, GTK3ShortcutsWindowMixin):
    """Wrapper for version 3.0 Gtk.ShortcutsWindow."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ShortcutsWindow."""
        Gtk.ShortcutsWindow.__init__(self)
        GTK3ShortcutsWindowMixin.__init__(self)
