"""The pytkwrap GTK3EntryCompletion module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3EntryCompletion(Gtk.EntryCompletion, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.EntryCompletion."""

    _GTK3_ENTRYCOMPLETION_PROPERTIES = GTK3WidgetProperties(
        cell_area=None,
        inline_completion=False,
        inline_selection=False,
        minimum_key_length=1,
        model=None,
        popup_completion=True,
        popup_set_width=True,
        popup_single_match=True,
        text_column=-1,
    )
    _GTK3_ENTRYCOMPLETION_SIGNALS = [
        "action-activated",
        "cursor-on-match",
        "insert-prefix",
        "match-selected",
        "no-matches",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3EntryCompletion."""
        Gtk.EntryCompletion.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ENTRYCOMPLETION_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_ENTRYCOMPLETION_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3EntryCompletion-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3EntryCompletion.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_inline_completion(self.dic_properties["inline_completion"])
        self.set_inline_selection(self.dic_properties["inline_selection"])
        self.set_minimum_key_length(self.dic_properties["minimum_key_length"])
        self.set_model(self.dic_properties["model"])
        self.set_popup_completion(self.dic_properties["popup_completion"])
        self.set_popup_set_width(self.dic_properties["popup_set_width"])
        self.set_popup_single_match(self.dic_properties["popup_single_match"])
        self.set_text_column(self.dic_properties["text_column"])
