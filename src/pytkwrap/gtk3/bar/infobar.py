"""The pytkwrap GTK3InfoBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3InfoBar(Gtk.InfoBar, GTK3Box):
    """Wrapper for version 3.0 Gtk.InfoBar."""

    _GTK3_INFOBAR_PROPERTIES = GTK3WidgetProperties(
        message_type=Gtk.MessageType.INFO,
        revealed=True,
        show_close_button=False,
    )
    _GTK3_INFOBAR_SIGNALS = ["close", "response"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3InfoBar."""
        Gtk.InfoBar.__init__(self)
        GTK3Box.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_INFOBAR_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_INFOBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3InfoBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3InfoBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_message_type(self.dic_properties["message_type"])
        self.set_revealed(self.dic_properties["revealed"])
        self.set_show_close_button(self.dic_properties["show_close_button"])
