"""The pytkwrap GTK3Revealer module.

Convenience wrapper for working with Gtk.Revealer.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _RevealerHost


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
        self: _RevealerHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3Revealer-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Revealer.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_reveal_child(self.dic_properties["reveal_child"])
        self.set_transition_duration(self.dic_properties["transition_duration"])

        if isinstance(
            self.dic_properties["transition_type"], Gtk.RevealerTransitionType
        ):
            self.set_transition_type(self.dic_properties["transition_type"])

    @property
    def child_revealed(self: _RevealerHost) -> bool:
        """Get whether the child is fully revealed.

        Returns
        -------
        bool
            True if the child is fully revealed.  False otherwise.
        """
        return self.get_child_revealed()


class GTK3Revealer(Gtk.Revealer, GTK3RevealerMixin):
    """Wrapper for version 3.0 Gtk.Revealer."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Revealer."""
        Gtk.Revealer.__init__(self)
        GTK3RevealerMixin.__init__(self)
