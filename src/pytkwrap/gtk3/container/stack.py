"""The pytkwrap GTK3Stack module.

Convenience wrapper for working with Gtk.Stack.

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
    from ._protocols import _StackHost


class GTK3StackMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Stack.

    Notes
    -----
    The following Gtk.Stack methods are not wrapped in a convenience layer, but may be
    called directly:

        * get_child_by_name(name)
        * set_visible_child_full(name, transition)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Stack.html for details
    on these methods.
    """

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

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_STACK_PROPERTIES)

    def do_set_properties(
        self: _StackHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3Stack-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Stack.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_hhomogeneous(self.dic_properties["hhomogeneous"])
        self.set_homogeneous(self.dic_properties["homogeneous"])
        self.set_interpolate_size(self.dic_properties["interpolate_size"])
        self.set_transition_duration(self.dic_properties["transition_duration"])
        self.set_vhomogeneous(self.dic_properties["vhomogeneous"])

        if isinstance(self.dic_properties["transition_type"], Gtk.StackTransitionType):
            self.set_transition_type(self.dic_properties["transition_type"])

        if self.dic_properties["visible_child"] is not None:
            self.set_visible_child(self.dic_properties["visible_child"])

        if self.dic_properties["visible_child_name"] is not None:
            self.set_visible_child_name(self.dic_properties["visible_child_name"])

    def do_add_child(
        self: _StackHost,
        child: Gtk.Widget,
        name: str,
        title: str | None = None,
    ) -> None:
        """Add a child widget to the GTK3Stack.

        Parameters
        ----------
        child : Gtk.Widget
            The widget to add to the GTK3Stack.
        name : str
            The name for the child widget.
        title : str | None
            A human-readable tile for the child widget.  The title will be used by
            the GTK3StackSwitcher to represent the child widget in a tab bar,
            so it should be short.
        """
        if title is not None:
            self.add_titled(child, name, title)
        else:
            self.add_named(child, name)

    @property
    def transition_running(self: _StackHost) -> bool:
        """Get whether the GTK3Stack is currently in a transition between pages.

        Returns
        -------
        bool
            Whether the GTK3Stack is currently in transition.
        """
        return self.get_transition_running()


class GTK3Stack(Gtk.Stack, GTK3StackMixin):
    """Wrapper for version 3.0 Gtk.Stack."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Stack."""
        Gtk.Stack.__init__(self)
        GTK3StackMixin.__init__(self)
