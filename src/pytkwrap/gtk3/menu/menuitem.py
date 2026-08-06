"""The pytkwrap GTK3MenuItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3BinMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MenuItemMixin(GTK3BinMixin):
    """Mixin class for GTK3MenuItem."""

    _GTK3_MENUITEM_PROPERTIES = GTK3WidgetProperties(
        accel_path=None,
        label="",
        submenu=None,
        use_underline=False,
    )
    _GTK3_MENUITEM_SIGNALS = [
        "activate",
        "activate-item",
        "deselect",
        "select",
        "toggle-size-allocate",
        "toggle-size-request",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3MenuItem mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_MENUITEM_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_MENUITEM_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MenuItem-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MenuItem.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_accel_path(self.dic_properties["accel_path"])
        self.set_label(self.dic_properties["label"])
        self.set_submenu(self.dic_properties["submenu"])
        self.set_use_underline(self.dic_properties["use_underline"])


class GTK3MenuItem(Gtk.MenuItem, GTK3MenuItemMixin):
    """Wrapper for version 3.0 Gtk.MenuItem."""

    def __init__(self, label: str = "") -> None:
        """Initialize an instance of the GTK3MenuItem."""
        Gtk.MenuItem.__init__(self, label=label)
        GTK3MenuItemMixin.__init__(self)

        self.dic_properties["label"] = label
        self.do_set_properties(self.dic_properties)
