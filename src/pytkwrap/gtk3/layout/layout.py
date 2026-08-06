"""The pytkwrap GTK3Layout module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3LayoutMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Layout."""

    _GTK3_LAYOUT_PROPERTIES = GTK3WidgetProperties(
        height=100,
        width=100,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Layout mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_LAYOUT_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Layout-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Layout.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_size(self.dic_properties["width"], self.dic_properties["height"])


class GTK3Layout(Gtk.Layout, GTK3LayoutMixin):
    """Wrapper for version 3.0 Gtk.Layout."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Layout."""
        Gtk.Layout.__init__(self)
        GTK3LayoutMixin.__init__(self)
