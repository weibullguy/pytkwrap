"""The pytkwrap GTK3WindowGroup module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3WindowGroupMixin(GTK3GObjectMixin):
    """Mixin class for GTK3WindowGroup."""

    @property
    def current_grab(self) -> Gtk.Widget:
        """Get the current grab widget of the group.

        Returns
        -------
        Gtk.Widget
            The current grab widget.
        """
        return self.get_current_grab()

    @property
    def windows(self) -> list[Gtk.Window]:
        """Get the list of windows in the window group.

        Returns
        -------
        list[Gtk.Window]
            The list of windows in the window group.
        """
        return self.list_windows()


class GTK3WindowGroup(Gtk.WindowGroup, GTK3WindowGroupMixin):
    """Wrapper for version 3.0 Gtk.WindowGroup."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3WindowGroup."""
        Gtk.WindowGroup.__init__(self)
        GTK3WindowGroupMixin.__init__(self)
