"""The pytkwrap GTK3Expander module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Expander(Gtk.Expander, GTK3Bin):
    """Wrapper for version 3.0 Gtk.Expander."""

    _GTK_EXPANDER_PROPERTIES = GTK3WidgetProperties(
        expanded=False,
        label=None,
        label_fill=False,
        label_widget=None,
        resize_toplevel=False,
        use_markup=False,
        use_underline=False,
    )
    _GTK3_EXPANDER_SIGNALS = ["activate"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Expander."""
        Gtk.Expander.__init__(self)
        GTK3Bin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_EXPANDER_SIGNALS}
        )
        self.dic_properties.update(self._GTK_EXPANDER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Widget-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Widget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_expanded(self.dic_properties["expanded"])
        self.set_label(self.dic_properties["label"])
        self.set_label_fill(self.dic_properties["label_fill"])
        self.set_label_widget(self.dic_properties["label_widget"])
        self.set_resize_toplevel(self.dic_properties["resize_toplevel"])
        self.set_use_markup(self.dic_properties["use_markup"])
        self.set_use_underline(self.dic_properties["use_underline"])
