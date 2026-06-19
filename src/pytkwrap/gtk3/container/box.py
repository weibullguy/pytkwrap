"""The pytkwrap GTK3Box module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Box(Gtk.Box, GTK3Container):
    """Wrapper for version 3.0 Gtk.Box."""

    _GTK3_BOX_PROPERTIES = GTK3WidgetProperties(
        baseline_position=Gtk.BaselinePosition.CENTER,
        homogeneous=False,
        spacing=0,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Box."""
        Gtk.Box.__init__(self)
        GTK3Container.__init__(self)

        self.dic_properties.update(self._GTK3_BOX_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Box-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Box.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_baseline_position(self.dic_properties["baseline_position"])
        self.set_homogeneous(self.dic_properties["homogeneous"])
        self.set_spacing(self.dic_properties["spacing"])
