"""The pytkwrap GTK3Assistant module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3Window


class GTK3Assistant(Gtk.Assistant, GTK3Window):
    """Wrapper for version 3.0 Gtk.Assistant."""

    _GTK3_ASSISTANT_PROPERTIES = GTK3WidgetProperties(
        use_header_bar=-1,
    )
    _GTK3_ASSISTANT_SIGNALS = [
        "apply",
        "cancel",
        "close",
        "escape",
        "prepare",
    ]

    def __init__(self, use_header_bar: bool = False) -> None:
        """Initialize an instance of the GTK3Assistant.

        Parameters
        ----------
        use_header_bar : bool, optional
            Whether to use the header-bar for action buttons.
        """
        Gtk.Assistant.__init__(self, use_header_bar=use_header_bar)
        GTK3Window.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ASSISTANT_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_ASSISTANT_PROPERTIES)
