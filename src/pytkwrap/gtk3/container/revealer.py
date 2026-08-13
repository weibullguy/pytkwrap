"""The pytkwrap GTK3Revealer module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3RevealerMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Revealer."""

    _GTK3_REVEALER_PROPERTIES = GTK3WidgetProperties(
        reveal_child=False,
        transition_duration=250,
        transition_type=Gtk.RevealerTransitionType.SLIDE_DOWN,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Revealer mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_REVEALER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Revealer-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Revealer.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_reveal_child(self.dic_properties["reveal_child"])
        self.set_transition_duration(self.dic_properties["transition_duration"])
        self.set_transition_type(self.dic_properties["transition_type"])


class GTK3Revealer(Gtk.Revealer, GTK3RevealerMixin):
    """Wrapper for version 3.0 Gtk.Revealer."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Revealer."""
        Gtk.Revealer.__init__(self)
        GTK3RevealerMixin.__init__(self)
