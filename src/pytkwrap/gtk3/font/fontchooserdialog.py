"""The pytkwrap GTK3FontChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin


class GTK3FontChooserDialog(Gtk.FontChooserDialog, GTK3DialogMixin):
    """Wrapper for version 3.0 Gtk.FontChooserDialog."""

    def __init__(
        self,
        title: str | None = "Choose a Font",
        transient_for: Gtk.Window | None = None,
    ) -> None:
        """Initialize an instance of the GTK3FontChooserDialog."""
        Gtk.FontChooserDialog.__init__(self, title=title, transient_for=transient_for)
        GTK3DialogMixin.__init__(self)

        self.dic_properties["title"] = title
        self.dic_properties["transient_for"] = transient_for

        self.do_set_properties(self.dic_properties)
