"""The pytkwrap GTK3VolumeButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.scalebutton import GTK3ScaleButton
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3VolumeButton(Gtk.VolumeButton, GTK3ScaleButton):
    """Wrapper for version 3.0 Gtk.VolumeButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 60
    _GTK3_VOLUME_BUTTON_PROPERTIES = GTK3WidgetProperties(
        use_symbolic=True,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3VolumeButton widget."""
        Gtk.VolumeButton.__init__(self)
        GTK3ScaleButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_VOLUME_BUTTON_PROPERTIES)
