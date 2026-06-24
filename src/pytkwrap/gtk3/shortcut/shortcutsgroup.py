"""The pytkwrap GTK3ShortcutsGroup module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ShortcutsGroup(Gtk.ShortcutsGroup, GTK3Box):
    """Wrapper for version 3.0 Gtk.ShortcutsGroup."""

    _GTK3_SHORTCUTSGROUP_PROPERTIES = GTK3WidgetProperties(
        accel_size_group=None,
        title="",
        title_size_group=None,
        view=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ShortcutsGroup."""
        Gtk.ShortcutsGroup.__init__(self)
        GTK3Box.__init__(self)

        self.dic_properties.update(self._GTK3_SHORTCUTSGROUP_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ShortcutsGroup-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ShortcutsGroup.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["accel_size_group", "title", "title_size_group", "view"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
