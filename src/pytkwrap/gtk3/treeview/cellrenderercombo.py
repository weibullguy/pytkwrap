"""The pytkwrap GTK3CellRenderer module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderertext import GTK3CellRendererText


class GTK3CellRendererCombo(Gtk.CellRendererCombo, GTK3CellRendererText):
    """Wrapper for version 3.0 Gtk.CellRendererCombo."""

    _GTK3_CELLRENDERERCOMBO_PROPERTIES = GTK3WidgetProperties(
        has_entry=True,
        model=None,
        text_column=-1,
    )
    _GTK3_CELLRENDERERCOMBO_SIGNALS = [
        "changed",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererCombo."""
        Gtk.CellRendererCombo.__init__(self)
        GTK3CellRendererText.__init__(self)

        self.dic_properties.update(self._GTK3_CELLRENDERERCOMBO_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CELLRENDERERCOMBO_SIGNALS}
        )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererCombo-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererCombo.
        """
        # Update the property dictionary.
        self.dic_properties |= properties

        for _property in [
            "has_entry",
            "model",
            "text_column",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
