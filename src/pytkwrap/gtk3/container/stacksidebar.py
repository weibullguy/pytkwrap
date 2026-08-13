"""The pytkwrap GTK3StackSidebar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3StackSidebarMixin(GTK3ContainerMixin):
    """Mixin class for GTK3StackSidebar."""

    _GTK3_STACKSIDEBAR_PROPERTIES = GTK3WidgetProperties(
        stack=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3StackSidebar mixin."""
        super().__init__(**kwargs)

        # Initialize the property dictionary.
        self.dic_properties.update(self._GTK3_STACKSIDEBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3StackSidebar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3StackSidebar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["stack"] is not None:
            self.set_stack(self.dic_properties["stack"])


class GTK3StackSidebar(Gtk.StackSidebar, GTK3StackSidebarMixin):
    """Wrapper for version 3.0 Gtk.StackSidebar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3StackSidebar."""
        Gtk.StackSidebar.__init__(self)
        GTK3StackSidebarMixin.__init__(self)
