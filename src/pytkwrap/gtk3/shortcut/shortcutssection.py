"""The pytkwrap GTK3ShortcutsSection module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ShortcutsSection(Gtk.ShortcutsSection, GTK3Box):
    """Wrapper for version 3.0 Gtk.ShortcutsSection."""

    _GTK3_SHORTCUTSSECTION_PROPERTIES = GTK3WidgetProperties(
        max_height=15,
        section_name=None,
        title=None,
        view_name=None,
    )
    _GTK3_SHORTCUTSSECTION_SIGNALS = ["change-current-page"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ShortcutsSection."""
        Gtk.ShortcutsSection.__init__(self)
        GTK3Box.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SHORTCUTSSECTION_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SHORTCUTSSECTION_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ShortcutsSection-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ShortcutsSection.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["max_height", "section_name", "title", "view_name"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
