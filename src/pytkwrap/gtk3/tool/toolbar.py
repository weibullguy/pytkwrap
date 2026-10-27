"""The pytkwrap GTK3Toolbar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolbutton import GTK3ToolButton
from pytkwrap.gtk3.tool.toolitem import GTK3ToolItem


class GTK3ToolbarMixin(GTK3ContainerMixin):
    """Wrapper for version 3.0 Gtk.Toolbar."""

    _GTK3_TOOLBAR_PROPERTIES = GTK3WidgetProperties(
        icon_size=Gtk.IconSize.LARGE_TOOLBAR,
        icon_size_set=False,
        show_arrow=True,
        toolbar_style=Gtk.ToolbarStyle.BOTH_HORIZ,
    )
    _GTK3_TOOLBAR_SIGNALS = [
        "focus-home-or-end",
        "orientation-changed",
        "popup-context-menu",
        "style-changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Toolbar mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOOLBAR_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TOOLBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Toolbar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Toolbar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_icon_size(self.dic_properties["icon_size"])
        self.set_show_arrow(self.dic_properties["show_arrow"])
        self.set_style(self.dic_properties["toolbar_style"])

    def do_build_toolbar(
        self,
        children: (
            list[list[GTK3ToolButton | GTK3ToolItem | int]]
            | list[tuple[GTK3ToolButton | GTK3ToolItem, int]]
            | tuple[list[GTK3ToolButton | GTK3ToolItem | int]]
            | tuple[tuple[GTK3ToolButton | GTK3ToolItem, int]]
        ),
    ):
        """Build the toolbar.

        Parameters
        ----------
        children : list[list[GTK3ToolButton | GTK3ToolItem | int]] |
                   list[tuple[GTK3ToolButton | GTK3ToolItem | int]] |
                   tuple[list[GTK3ToolButton | GTK3ToolItem | int]] |
                   tuple[tuple[GTK3ToolButton | GTK3ToolItem | int]]
            The list of lists, list of tuples, tuple of lists, or tuple of tuples
            containing the children to add to the toolbar.  Each inner list or tuple
            contains the GTK3ToolButton or GTK3ToolItem to add to the toolbar at
            index 0 and the position to add it at index 1.
        """
        for _child in children:
            self.insert(_child[0], _child[1])

    @property
    def n_items(self) -> int:
        """Return the number of items in the toolbar."""
        return self.get_n_items()

    @property
    def relief_style(self) -> Gtk.ReliefStyle:
        """Return the value of the 'relief_style' property."""
        return self.get_relief_style()


class GTK3Toolbar(Gtk.Toolbar, GTK3ToolbarMixin):
    """Wrapper for version 3.0 Gtk.Toolbar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Toolbar."""
        Gtk.Toolbar.__init__(self)
        GTK3ToolbarMixin.__init__(self)
