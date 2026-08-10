"""The pytkwrap GTK3ScrollBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.range import GTK3RangeMixin


class GTK3ScrollBar(Gtk.Scrollbar, GTK3RangeMixin):
    """Wrapper for version 3.0 Gtk.Scrollbar."""

    def __init__(
        self,
        orientation: Gtk.Orientation = Gtk.Orientation.VERTICAL,
        adjustment: Gtk.Adjustment | None = None,
    ) -> None:
        """Initialize an instance of the GTK3ScrollBar."""
        Gtk.Scrollbar.__init__(self, orientation=orientation, adjustment=adjustment)
        GTK3RangeMixin.__init__(self)
