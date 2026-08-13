"""The pytkwrap GTK3Box module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3BoxMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Box."""

    _GTK3_BOX_PROPERTIES = GTK3WidgetProperties(
        baseline_position=Gtk.BaselinePosition.CENTER,
        homogeneous=False,
        spacing=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Box mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
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


class GTK3Box(Gtk.Box, GTK3BoxMixin):
    """Wrapper for version 3.0 Gtk.Box."""

    def __init__(
        self,
        orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
        spacing: int = 0,
    ) -> None:
        """Initialize an instance of the GTK3Box.

        Parameters
        ----------
        orientation : Gtk.Orientation
            The orientation of the box.  The default is Gtk.Orientation.HORIZONTAL.
        spacing : int
            The spacing in pixels between the widgets in the box.  The default is 0.
        """
        Gtk.Box.__init__(self, orientation=orientation, spacing=spacing)
        GTK3BoxMixin.__init__(self)

        self.dic_properties["spacing"] = spacing
