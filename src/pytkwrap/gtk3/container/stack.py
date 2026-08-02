"""The pytkwrap GTK3Stack module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3StackMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Stack."""

    _GTK3_STACK_PROPERTIES = GTK3WidgetProperties(
        hhomogeneous=True,
        homogeneous=True,
        interpolate_size=False,
        transition_duration=200,
        transition_type=Gtk.StackTransitionType.NONE,
        vhomogeneous=True,
        visible_child=None,
        visible_child_name=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Stack mixin."""
        super().__init__(**kwargs)

        self.dic_properties.update(self._GTK3_STACK_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Stack-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Stack.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_hhomogeneous(self.dic_properties["hhomogeneous"])
        self.set_homogeneous(self.dic_properties["homogeneous"])
        self.set_interpolate_size(self.dic_properties["interpolate_size"])
        self.set_transition_duration(self.dic_properties["transition_duration"])
        self.set_transition_type(self.dic_properties["transition_type"])
        self.set_vhomogeneous(self.dic_properties["vhomogeneous"])

        if self.dic_properties["visible_child"] is not None:
            self.set_visible_child(self.dic_properties["visible_child"])

        if self.dic_properties["visible_child_name"] is not None:
            self.set_visible_child_name(self.dic_properties["visible_child_name"])


class GTK3Stack(Gtk.Stack, GTK3StackMixin):
    """Wrapper for version 3.0 Gtk.Stack."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Stack."""
        Gtk.Stack.__init__(self)
        GTK3StackMixin.__init__(self)
