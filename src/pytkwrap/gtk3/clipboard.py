"""The pytkwrap GTK3Clipboard module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3ClipboardMixin(GTK3GObjectMixin):
    """Mixin class for GTK3Clipboard.

    Attributes
    ----------
    _GTK3_CLIPBOARD_SIGNALS : list[str]
        Signals unique to the GTK3Clipboard class.
    """

    _GTK3_CLIPBOARD_SIGNALS = [
        "owner-change",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Clipboard mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CLIPBOARD_SIGNALS}
        )

    @property
    def display(self) -> Gdk.Display | None:
        """Get the display associated with the clipboard.

        Returns
        -------
        Gdk.Display | None
            The display associated with the clipboard.
        """
        return self.get_display()

    @property
    def owner(self) -> GObject.GObject | None:
        """Get the owner of the clipboard.

        Returns
        -------
        GObject.GObject | None
            The owner of the clipboard, or None if there is no owner.
        """
        return self.get_owner()

    @property
    def selection(self) -> Gdk.Atom:
        """Get the selection associated with the clipboard.

        Returns
        -------
        Gdk.Atom
            The selection data from the clipboard.
        """
        return self.get_selection()


class GTK3Clipboard(Gtk.Clipboard, GTK3ClipboardMixin):
    """Wrapper for version 3.0 Gtk.Clipboard."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Clipboard."""
        Gtk.Clipboard.__init__(self)
        GTK3ClipboardMixin.__init__(self)
