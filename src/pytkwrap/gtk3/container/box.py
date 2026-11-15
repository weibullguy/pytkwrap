"""The pytkwrap GTK3Box module.

Convenience wrapper for working with Gtk.Box.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _BoxHost


class GTK3BoxMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Box.

    Notes
    -----
    The following Gtk.Box methods are not wrapped in a convenience layer, but may be
    called directly:

                * query_child_packing(child)
                * reorder_child(child, position)
                * set_child_packing(child, expand, fill, padding, pack_type)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Box.html for details on
    these methods.
    """

    _GTK3_BOX_PROPERTIES = GTK3WidgetProperties(
        baseline_position=Gtk.BaselinePosition.CENTER,
        center_widget=None,
        homogeneous=False,
        spacing=0,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Box mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_BOX_PROPERTIES)

    def do_set_properties(
        self: _BoxHost,
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
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_baseline_position(self.dic_properties["baseline_position"])
        self.set_center_widget(self.dic_properties["center_widget"])
        self.set_homogeneous(self.dic_properties["homogeneous"])
        self.set_spacing(self.dic_properties["spacing"])

    def do_add_child(
        self: _BoxHost,
        child: GTK3Widget,
        expand: bool,
        fill: bool,
        padding: int,
        start: bool = True,
    ) -> None:
        """Add a child widget to the GTK3Box.

        Parameters
        ----------
        child : GTK3Widget
            The GTK3Widget to add as a child to the GTK3Box.
        expand : bool
            Whether to give the new child extra space allocated to GTK3Box.
        fill : bool
            Whether the space given to the new child by expand is actually allocated
            to child rather than just padding it.
        padding : int
            The extra space (in pixels) to put between this child and its neighbors.
        start : bool
            Whether to add the child widget at the start (default) or end of the
            GTK3Box.
        """
        if start:
            return self.pack_start(child, expand, fill, padding)
        return self.pack_end(child, expand, fill, padding)


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
