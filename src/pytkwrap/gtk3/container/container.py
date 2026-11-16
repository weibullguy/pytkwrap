"""The pytkwrap GTK3Container module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ContainerHost


class GTK3ContainerMixin(GTK3WidgetMixin):
    """Mixin class for GTK3Container.

    Notes
    -----
    The following Gtk.Button methods are not wrapped in a convenience layer, but may be
    called directly:

        * add(widget)
        * check_resize()
        * child_get(child, *prop_names)
        * child_get_property(child, property_name, value=None)
        * child_notify(child, child_property)
        * child_notify_by_pspec(child, pspec)
        * child_set(child, **kwargs)
        * child_set_property(child, property_name, value)
        * child_type()
        * forall(callback, *callback_data)
        * foreach(callback, *callback_data)
        * get_focus_child()
        * get_focus_hadjustment()
        * get_focus_vadjustment()
        * get_path_for_child(child)
        * propagate_draw(child, cr)
        * remove(widget)
        * set_focus_child(child)
        * set_focus_hadjustment(adjustment)
        * set_focus_vadjustment(adjustment)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Container.html for
    details on these methods.
    """

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
        self: _ContainerHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3Container-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Container.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_border_width(self.dic_properties["border_width"])


class GTK3Container(Gtk.Container, GTK3ContainerMixin):
    """Wrapper for version 3.0 Gtk.Container."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Container."""
        Gtk.Container.__init__(self)
        GTK3ContainerMixin.__init__(self)
