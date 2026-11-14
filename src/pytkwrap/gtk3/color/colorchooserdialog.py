"""The pytkwrap GTK3ColorChooserDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ColorChooserDialogHost


class GTK3ColorChooserDialogMixin(GTK3DialogMixin):
    """Mixin class for GTK3ColorChooserDialog."""

    _GTK3_COLORCHOOSERDIALOG_PROPERTIES = GTK3WidgetProperties(
        show_editor=False,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ColorChooserDialog mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_COLORCHOOSERDIALOG_PROPERTIES)

    def do_set_properties(
        self: _ColorChooserDialogHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ColorChooserDialog-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ColorChooserDialog.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_property("show-editor", self.dic_properties["show_editor"])


class GTK3ColorChooserDialog(Gtk.ColorChooserDialog, GTK3ColorChooserDialogMixin):
    """Wrapper for version 3.0 Gtk.ColorChooserDialog."""

    def __init__(
        self,
        title: str = "",
        transient_for: Gtk.Window | None = None,
    ) -> None:
        """Initialize an instance of the GTK3ColorChooserDialog.

        title: str | None
            The title of the dialog or None.
        parent: Gtk.Window | None
            Transient parent of the dialog or None.
        """
        Gtk.ColorChooserDialog.__init__(self, title=title, transient_for=transient_for)
        GTK3ColorChooserDialogMixin.__init__(self)

        self.dic_properties["title"] = title
        self.dic_properties["transient_for"] = transient_for
