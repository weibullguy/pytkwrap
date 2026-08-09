"""The pytkwrap GTK3Plug module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.window.window import GTK3WindowMixin


class GTK3PlugMixin(GTK3WindowMixin):
    """Mixin class for GTK3Plug."""

    _GTK3_PLUG_SIGNALS = [
        "embedded",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Plug mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update({_signal: -1 for _signal in self._GTK3_PLUG_SIGNALS})


class GTK3Plug(Gtk.Plug, GTK3PlugMixin):
    """Wrapper for version 3.0 Gtk.Plug."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Plug."""
        Gtk.Plug.__init__(self)
        GTK3PlugMixin.__init__(self)
