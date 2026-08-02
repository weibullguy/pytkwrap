"""The pytkwrap GTK3Dialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3WindowMixin


class GTK3DialogMixin(GTK3WindowMixin):
    """Mixin class for GTK3Dialog."""

    _GTK3_DIALOG_PROPERTIES = GTK3WidgetProperties(
        use_header_bar=-1,
    )
    _GTK3_DIALOG_SIGNALS = [
        "close",
        "response",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Dialog mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_DIALOG_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_DIALOG_PROPERTIES)


class GTK3Dialog(Gtk.Dialog, GTK3DialogMixin):
    """Wrapper for version 3.0 Gtk.Dialog."""

    def __init__(self, use_header_bar: bool = False) -> None:
        """Initialize an instance of the GTK3Dialog.

        Parameters
        ----------
        use_header_bar : bool, optional
            Whether to use the header bar for action buttons.
        """
        super().__init__(use_header_bar=use_header_bar)
        GTK3DialogMixin.__init__(self)
