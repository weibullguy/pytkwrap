"""The pytkwrap GTK3RadioMenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.menu.checkmenuitem import GTK3CheckMenuItemMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3RadioMenuItemMixin(GTK3CheckMenuItemMixin):
    """Mixin class for GTK3RadioMenuItem."""

    _GTK3_RADIOMENUITEM_PROPERTIES = GTK3WidgetProperties(
        group=None,
    )
    _GTK3_RADIOMENUITEM_SIGNALS = [
        "group-changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3RadioMenuItem mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_RADIOMENUITEM_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_RADIOMENUITEM_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3RadioMenuItem-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3RadioMenuItem.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_group(self.dic_properties["group"])


class GTK3RadioMenuItem(Gtk.RadioMenuItem, GTK3RadioMenuItemMixin):
    """Wrapper for version 3.0 Gtk.RadioMenuItem."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3RadioMenuItem."""
        Gtk.RadioMenuItem.__init__(self)
        GTK3RadioMenuItemMixin.__init__(self)
