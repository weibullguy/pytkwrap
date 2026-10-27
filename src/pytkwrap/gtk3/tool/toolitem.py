"""The pytkwrap GTK3ToolItem module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ToolItemMixin(GTK3ContainerMixin):
    """Mixin class for GTK3ToolItem.

    Attributes
    ----------
    _GTK3_TOOLITEM_PROPERTIES : GTK3WidgetProperties
        The GTK3ToolItem-specific properties.
    _GTK3_TOOLITEM_SIGNALS : list[str]
        The GTK3ToolItem-specific signals.
    """

    _GTK3_TOOLITEM_PROPERTIES = GTK3WidgetProperties(
        is_important=False,
        visible_horizontal=True,
        visible_vertical=True,
    )
    _GTK3_TOOLITEM_SIGNALS = ["create-menu-proxy", "toolbar-reconfigured"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ToolItem."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOOLITEM_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TOOLITEM_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ToolItem-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ToolItem.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_is_important(self.dic_properties["is_important"])
        self.set_visible_horizontal(self.dic_properties["visible_horizontal"])
        self.set_visible_vertical(self.dic_properties["visible_vertical"])

    @property
    def ellipsize_mode(self) -> Pango.EllipsizeMode:
        """Get the ellipsize mode of the GTK3ToolItem.

        Returns
        -------
        Pango.EllipsizeMode
            The ellipsize mode of the GTK3ToolItem.
        """
        return self.get_ellipsize_mode()

    @property
    def icon_size(self) -> int:
        """Get the icon size of the GTK3ToolItem.

        Returns
        -------
        int
            The icon size of the GTK3ToolItem.
        """
        return self.get_icon_size()

    @property
    def orientation(self) -> Gtk.Orientation:
        """Get the orientation of the GTK3ToolItem.

        Returns
        -------
        Gtk.Orientation
            The orientation of the GTK3ToolItem.
        """
        return self.get_orientation()

    @property
    def relief_style(self) -> Gtk.ReliefStyle:
        """Get the relief style of the GTK3ToolItem.

        Returns
        -------
        Gtk.ReliefStyle
            The relief style of the GTK3ToolItem.
        """
        return self.get_relief_style()

    @property
    def text_alignment(self) -> float:
        """Get the text alignment of the GTK3ToolItem.

        Returns
        -------
        float
            The text alignment of the GTK3ToolItem.
        """
        return self.get_text_alignment()

    @property
    def text_orientation(self) -> Gtk.Orientation:
        """Get the text orientation of the GTK3ToolItem.

        Returns
        -------
        Gtk.Orientation
            The text orientation of the GTK3ToolItem.
        """
        return self.get_text_orientation()

    @property
    def text_size_group(self) -> Gtk.SizeGroup:
        """Get the text size group of the GTK3ToolItem.

        Returns
        -------
        Gtk.SizeGroup
            The text size group of the GTK3ToolItem.
        """
        return self.get_text_size_group()

    @property
    def toolbar_style(self) -> Gtk.ToolbarStyle:
        """Get the toolbar style of the GTK3ToolItem.

        Returns
        -------
        Gtk.ToolbarStyle
            The toolbar style of the GTK3ToolItem.
        """
        return self.get_toolbar_style()


class GTK3ToolItem(Gtk.ToolItem, GTK3ToolItemMixin):
    """Wrapper for version 3.0 Gtk.ToolItem."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ToolItem."""
        Gtk.ToolItem.__init__(self)
        GTK3ToolItemMixin.__init__(self)
