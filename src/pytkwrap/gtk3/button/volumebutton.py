"""The pytkwrap GTK3VolumeButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

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
        GTK3ScaleButton.__init__(self, 4)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_VOLUME_BUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3VolumeButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3VolumeButton.
        """
        super().do_set_properties(properties)

        self.set_property("use-symbolic", self.dic_properties["use_symbolic"])
