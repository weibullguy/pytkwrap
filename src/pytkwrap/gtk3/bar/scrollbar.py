"""The pytkwrap GTK3ScrollBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.range import GTK3RangeMixin


class GTK3ScrollBarMixin(GTK3RangeMixin):
    """Mixin for GTK3ScrollBar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ScrollBar mixin."""
        GTK3RangeMixin.__init__(self)


class GTK3ScrollBar(Gtk.Scrollbar, GTK3ScrollBarMixin):
    """Wrapper for version 3.0 Gtk.Scrollbar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ScrollBar."""
        Gtk.Scrollbar.__init__(self)
        GTK3ScrollBarMixin.__init__(self)
