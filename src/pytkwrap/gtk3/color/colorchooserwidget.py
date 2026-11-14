"""The pytkwrap GTK3ColorChooserWidget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ColorChooserWidgetHost


class GTK3ColorChooserWidgetMixin(GTK3BoxMixin):
    """Mixin class for GTK3ColorChooserWidget."""

    _GTK3_COLORCHOOSERWIDGET_PROPERTIES = GTK3WidgetProperties(
        show_editor=False,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ColorChooserWidget mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_COLORCHOOSERWIDGET_PROPERTIES)

    def do_set_properties(
        self: _ColorChooserWidgetHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ColorChooserWidget-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ColorChooserWidget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_property("show-editor", self.dic_properties["show_editor"])


class GTK3ColorChooserWidget(Gtk.ColorChooserWidget, GTK3ColorChooserWidgetMixin):
    """Wrapper for version 3.0 Gtk.ColorChooserWidget."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorChooserWidget."""
        Gtk.ColorChooserWidget.__init__(self)
        GTK3ColorChooserWidgetMixin.__init__(self)
