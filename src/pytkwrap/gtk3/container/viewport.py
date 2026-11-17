"""The pytkwrap GTK3Viewport module.

Convenience wrapper for working with Gtk.Viewport.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ViewportHost


class GTK3ViewportMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Viewport."""

    _GTK3_VIEWPORT_PROPERTIES = GTK3WidgetProperties(
        shadow_type=Gtk.ShadowType.IN,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Viewport mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_VIEWPORT_PROPERTIES)

    def do_set_properties(
        self: _ViewportHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3Viewport-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Viewport.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.props.hadjustment = self.dic_properties["hadjustment"]  # type: ignore[attr-defined] # ty: ignore[unresolved-attribute] # pylint: disable=line-too-long
        self.set_shadow_type(self.dic_properties["shadow_type"])
        self.props.vadjustment = self.dic_properties["vadjustment"]  # type: ignore[attr-defined] # ty: ignore[unresolved-attribute] # pylint: disable=line-too-long

    @property
    def bin_window(self: _ViewportHost) -> Gdk.Window | None:
        """Get the bin window of the GTK3Viewport.

        Returns
        -------
        Gdk.Window | None
            The GTK3Viewport's bin window or None if there isn't one.
        """
        return self.get_bin_window()

    @property
    def view_window(self: _ViewportHost) -> Gdk.Window | None:
        """Get the view window of the GTK3Viewport.

        Returns
        -------
        Gdk.Window | None
            The GTK3Viewport's view window or None if there isn't one.
        """
        return self.get_view_window()


class GTK3Viewport(Gtk.Viewport, GTK3ViewportMixin):
    """Wrapper for version 3.0 Gtk.Viewport."""

    def __init__(
        self,
        hadjustment: Gtk.Adjustment | None = None,
        vadjustment: Gtk.Adjustment | None = None,
    ) -> None:
        """Initialize an instance of the GTK3Viewport.

        Arguments
        ---------
        hadjustment : Gtk.Adjustment, optional
            The adjustment to use for the viewport's horizontal adjustment.
        vadjustment : Gtk.Adjustment, optional
            The adjustment to use for the viewport's vertical adjustment.
        """
        Gtk.Viewport.__init__(self, hadjustment=hadjustment, vadjustment=vadjustment)
        GTK3ViewportMixin.__init__(self)

        self.dic_properties["hadjustment"] = hadjustment
        self.dic_properties["vadjustment"] = vadjustment
