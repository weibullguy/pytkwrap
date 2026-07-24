"""The pytkwrap GTK3TextBuffer module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3TextBuffer(Gtk.TextBuffer, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.TextBuffer."""

    _GTK3_TEXTBUFFER_PROPERTIES = GTK3WidgetProperties(
        tag_table=None,
        text="",
    )
    _GTK3_TEXTBUFFER_SIGNALS = [
        "apply-tag",
        "begin-user-action",
        "changed",
        "delete-range",
        "end-user-action",
        "insert-child-anchor",
        "insert-pixbuf",
        "insert-text",
        "mark-deleted",
        "mark-set",
        "modified-changed",
        "paste-done",
        "remove-tag",
    ]

    def __init__(self, table: Gtk.TextTagTable | None = None) -> None:
        """Initialize an instance of the GTK3TextBuffer.

        Parameters
        ----------
        table : Gtk.TextTagTable | None
        """
        Gtk.TextBuffer.__init__(self, tag_table=table)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TEXTBUFFER_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_TEXTBUFFER_PROPERTIES)
        self.dic_properties["tag_table"] = table

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3TextBuffer-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3TextBuffer.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_text(self.dic_properties["text"])
