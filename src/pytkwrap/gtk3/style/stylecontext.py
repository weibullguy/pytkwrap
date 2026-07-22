"""The pytkwrap GTK3StyleContext module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3StyleContext(Gtk.StyleContext, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.StyleContext."""

    _GTK3_STYLECONTEXT_PROPERTIES = GTK3WidgetProperties(
        paint_clock=None,
        parent=None,
        screen=None,
    )
    _GTK3_STYLECONTEXT_SIGNALS = [
        "changed",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3StyleContext."""
        Gtk.StyleContext.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_STYLECONTEXT_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_STYLECONTEXT_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3StyleContext-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3StyleContext.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_parent(self.dic_properties["parent"])

        if self.dic_properties["paint_clock"] is not None:
            self.set_frame_clock(self.dic_properties["paint_clock"])

        if self.dic_properties["screen"] is not None:
            self.set_screen(self.dic_properties["screen"])
