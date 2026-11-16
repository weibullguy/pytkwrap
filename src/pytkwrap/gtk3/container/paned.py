"""The pytkwrap GTK3Paned module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _PanedHost

TOPLEFT = 1
BOTTOMRIGHT = 2


class GTK3PanedMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Paned.

    Notes
    -----
    The following Gtk.Button methods are not wrapped in a convenience layer, but may be
    called directly:

        * add1(child)
        * add2(child)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Paned.html for details
    on these methods.
    """

    _GTK3_PANED_ATTRIBUTES = GTK3WidgetAttributes(
        orientation=Gtk.Orientation.HORIZONTAL
    )
    _GTK3_PANED_PROPERTIES = GTK3WidgetProperties(
        position=0,
        position_set=False,
        wide_handle=False,
    )
    _GTK3_PANED_SIGNALS = [
        "accept-position",
        "cancel-position",
        "cycle-child-focus",
        "cycle-handle-focus",
        "move-handle",
        "toggle-handle-focus",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Paned mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_PANED_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_PANED_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_PANED_PROPERTIES)

    def do_set_properties(
        self: _PanedHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3Paned-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Paned.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_position(self.dic_properties["position"])
        self.set_wide_handle(self.dic_properties["wide_handle"])

        self.set_property(
            "position-set",
            self.dic_properties["position_set"],
        )

    def do_add_child(
        self: _PanedHost,
        child: Gtk.Widget,
        resize: bool,
        shrink: bool,
        position: int = 1,
    ) -> None:
        """Add a child widget to the GTK3Paned.

        Parameters
        ----------
        child : Gtk.Widget
            The widget to add to the GTK3Paned.
        resize : bool
            Whether this child should resize when the GTK3Paned is resized.
        shrink : bool
            Whether this child can be made smaller than its requisition.
        position : int
            Which position to place this child in the GTK3Paned.  1 = top or left
            pane (default), 2 = bottom or right pane.

        Notes
        -----
        * do_add_child(child, False, True) is equivalent to add1(child).
        * do_add_child(child, True, True, 2) is equivalent to add2(child).
        """
        if position == TOPLEFT:
            self.pack1(child, resize, shrink)
        elif position == BOTTOMRIGHT:
            self.pack2(child, resize, shrink)

    @property
    def children(self: _PanedHost) -> tuple[Gtk.Widget, Gtk.Widget]:
        """Get a tuple of the child widgets in the GTK3Paned.

        Returns
        -------
        tuple[Gtk.Widget, Gtk.Widget]
            The tuple of child widgets in the GTK3Paned.
        """
        return (self.get_child1(), self.get_child2())

    @property
    def handle_window(self: _PanedHost) -> Gdk.Window:
        """Get the Gdk.Window of the handle.

        Returns
        -------
        Gdk.Window
            The Gdk.Window of the handle.
        """
        return self.get_handle_window()


class GTK3Paned(Gtk.Paned, GTK3PanedMixin):
    """Wrapper for version 3.0 Gtk.Paned.

    Arguments
    ---------
    orientation : Gtk.Orientation
        The orientation of the paned widget.  The default is Gtk.Orientation.HORIZONTAL.
    """

    def __init__(
        self,
        orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
    ) -> None:
        """Initialize an instance of the GTK3Paned.

        Parameters
        ----------
        orientation : Gtk.Orientation
            The orientation of the paned widget.  The default is
            Gtk.Orientation.HORIZONTAL.
        """
        Gtk.Paned.__init__(self, orientation=orientation)
        GTK3PanedMixin.__init__(self)

        self.dic_attributes["orientation"] = orientation
