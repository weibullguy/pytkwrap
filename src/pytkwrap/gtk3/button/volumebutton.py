"""The pytkwrap GTK3VolumeButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.scalebutton import GTK3ScaleButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _VolumeButtonHost


class GTK3VolumeButtonMixin(GTK3ScaleButtonMixin):
    """Mixin for GTK3VolumeButton.

    Notes
    -----
    GTK3VolumeButton passes a Gtk.Image to its callback function.
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
    _GTK3_VOLUME_BUTTON_PROPERTIES = GTK3WidgetProperties(
        use_symbolic=True,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3VolumeButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_VOLUME_BUTTON_PROPERTIES)

    def do_set_properties(
        self: _VolumeButtonHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3VolumeButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3VolumeButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_property("use-symbolic", self.dic_properties["use_symbolic"])


class GTK3VolumeButton(Gtk.VolumeButton, GTK3VolumeButtonMixin):
    """Wrapper for version 3.0 Gtk.VolumeButton."""

    def __init__(self, size: Gtk.IconSize = Gtk.IconSize.BUTTON) -> None:
        """Initialize an instance of the GTK3VolumeButton widget.

        Parameters
        ----------
        size : Gtk.IconSize
            A stock icon size.  The default is Gtk.IconSize.BUTTON.
        """
        Gtk.VolumeButton.__init__(self, size=size)
        GTK3VolumeButtonMixin.__init__(self)

        self.dic_properties["size"] = size
