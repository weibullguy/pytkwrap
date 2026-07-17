"""The pytkwrap GTK3EntryBuffer module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3EntryBuffer(Gtk.EntryBuffer, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.EntryBuffer."""

    _GTK3_ENTRYBUFFER_PROPERTIES = GTK3WidgetProperties(
        max_length=0,
        text="",
    )
    _GTK3_ENTRYBUFFER_SIGNALS = [
        "deleted-text",
        "inserted-text",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3EntryBuffer."""
        Gtk.EntryBuffer.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ENTRYBUFFER_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_ENTRYBUFFER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3EntryBuffer-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3EntryBuffer.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_max_length(self.dic_properties["max_length"])
        self.set_text(self.dic_properties["text"], len(self.dic_properties["text"]))
