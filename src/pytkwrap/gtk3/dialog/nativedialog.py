"""The pytkwrap GTK3NativeDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3NativeDialog(Gtk.NativeDialog, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.NativeDialog."""

    _GTK3_NATIVEDIALOG_PROPERTIES = GTK3WidgetProperties(
        modal=False,
        title=None,
        transient_for=None,
        visible=False,
    )
    _GTK3_NATIVEDIALOG_SIGNALS = [
        "response",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTKNativeDialog."""
        Gtk.NativeDialog.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_NATIVEDIALOG_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_NATIVEDIALOG_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3NativeDialog-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3NativeDialog.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_modal(self.dic_properties["modal"])
        self.set_transient_for(self.dic_properties["transient_for"])

        if self.dic_properties["title"] is not None:
            self.set_title(self.dic_properties["title"])

        if self.dic_properties["visible"]:
            self.show()
