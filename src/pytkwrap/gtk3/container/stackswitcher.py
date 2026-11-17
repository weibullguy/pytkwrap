"""The pytkwrap GTK3StackSwitcher module.

Convenience wrapper for working with Gtk.StackSwitcher.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _StackSwitcherHost


class GTK3StackSwitcherMixin(GTK3BoxMixin):
    """Mixin class for GTK3StackSwitcher."""

    _GTK3_STACKSWITCHER_PROPERTIES = GTK3WidgetProperties(
        icon_size=1,
        stack=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3StackSwitcher mixin."""
        super().__init__(**kwargs)

        # Initialize the property dictionary.
        self.dic_properties.update(self._GTK3_STACKSWITCHER_PROPERTIES)

    def do_set_properties(
        self: _StackSwitcherHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3StackSwitcher-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3StackSwitcher.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_stack(self.dic_properties["stack"])
        self.set_property("icon-size", self.dic_properties["icon_size"])


class GTK3StackSwitcher(Gtk.StackSwitcher, GTK3StackSwitcherMixin):
    """Wrapper for version 3.0 Gtk.StackSwitcher."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3StackSwitcher."""
        Gtk.StackSwitcher.__init__(self)
        GTK3StackSwitcherMixin.__init__(self)
