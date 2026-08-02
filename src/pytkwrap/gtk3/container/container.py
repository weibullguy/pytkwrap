"""The pytkwrap GTK3Container module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin


class GTK3ContainerMixin(GTK3WidgetMixin):
    """Mixin class for GTK3Container."""

    _GTK3_CONTAINER_PROPERTIES = GTK3WidgetProperties(
        border_width=0,
    )
    _GTK3_CONTAINER_SIGNALS = [
        "add",
        "check-resize",
        "remove",
        "set-focus-child",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Container."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CONTAINER_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_CONTAINER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Container-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Container.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_border_width(self.dic_properties["border_width"])


class GTK3Container(Gtk.Container, GTK3ContainerMixin):
    """Wrapper for version 3.0 Gtk.Container."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Container."""
        # GTK3Container does not initialize when calling super().__init__().
        Gtk.Container.__init__(self)
        GTK3ContainerMixin.__init__(self)
