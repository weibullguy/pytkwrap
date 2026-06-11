"""The pytkwrap GTK3CellRenderer module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer


class GTK3CellRendererToggle(Gtk.CellRendererToggle, GTK3CellRenderer):
    """Wrapper for version 3.0 Gtk.CellRendererToggle."""

    _GTK3_CELLRENDERERTOGGLE_PROPERTIES = GTK3WidgetProperties(
        activatable=True,
        active=False,
        inconsistent=False,
        radio=False,
    )
    _GTK3_CELLRENDERERTOGGLE_SIGNALS = [
        "toggled",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererToggle."""
        Gtk.CellRendererToggle.__init__(self)
        GTK3CellRenderer.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERERTOGGLE_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CELLRENDERERTOGGLE_SIGNALS}
        )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererToggle-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererToggle.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        self.set_activatable(self.dic_properties["activatable"])
        self.set_active(self.dic_properties["active"])
        self.set_radio(self.dic_properties["radio"])

        for _property in [
            "inconsistent",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
