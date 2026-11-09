"""The pytkwrap GTK3HeaderBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _HeaderBarHost


class GTK3HeaderBarMixin(GTK3ContainerMixin):
    """Mixin for GTK3HeaderBar.

    Attributes
    ----------
    _GTK3_HEADERBAR_PROPERTIES : GTK3WidgetProperties
        GTK3HeaderBar-specific properties.
    """

    _GTK3_HEADERBAR_PROPERTIES = GTK3WidgetProperties(
        custom_title=None,
        decoration_layout=None,
        decoration_layout_set=False,
        has_subtitle=True,
        show_close_button=False,
        spacing=6,
        subtitle=None,
        title=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3HeaderBar mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_HEADERBAR_PROPERTIES)

    def do_set_properties(
        self: _HeaderBarHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3HeaderBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3HeaderBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_custom_title(self.dic_properties["custom_title"])
        self.set_decoration_layout(self.dic_properties["decoration_layout"])
        self.set_has_subtitle(self.dic_properties["has_subtitle"])
        self.set_show_close_button(self.dic_properties["show_close_button"])
        self.set_subtitle(self.dic_properties["subtitle"])
        self.set_title(self.dic_properties["title"])

        self.set_property(
            "decoration-layout-set",
            self.dic_properties["decoration_layout_set"],
        )
        self.set_property(
            "spacing",
            self.dic_properties["spacing"],
        )

    def do_add_child(
        self: _HeaderBarHost, child: GTK3Widget, start: bool = True
    ) -> None:
        """Add a child widget to the GTK3HeaderBar.

        Parameters
        ----------
        child : GTK3Widget
            The GTK3Widget to add as a child to the GTK3HeaderBar.
        start : bool
            Whether to add the child widget at the start (default) or end of the
            GTK3HeaderBar.
        """
        if start:
            return self.pack_start(child)
        return self.pack_end(child)


class GTK3HeaderBar(Gtk.HeaderBar, GTK3HeaderBarMixin):
    """Wrapper for version 3.0 Gtk.HeaderBar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3HeaderBar."""
        Gtk.HeaderBar.__init__(self)
        GTK3HeaderBarMixin.__init__(self)
