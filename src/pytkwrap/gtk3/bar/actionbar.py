"""The pytkwrap GTK3ActionBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.widget import GTK3Widget, GTK3WidgetMixin, GTK3WidgetProperties


class GTK3ActionBarMixin(GTK3WidgetMixin):
    """Mixin for GTK3ActionBar.

    Attributes
    ----------
    _GTK3_ACTIONBAR_PROPERTIES : GTK3WidgetProperties
        GTK3ActionBar-specific properties.
    """

    _GTK3_ACTIONBAR_PROPERTIES = GTK3WidgetProperties(center_widget=None)

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ActionBar mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_ACTIONBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ActionBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3HeaderBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_center_widget(self.dic_properties["center_widget"])

    def do_add_child(self, child: GTK3Widget, start: bool = True) -> None:
        """Add a child widget to the GTK3ActionBar.

        Parameters
        ----------
        child : GTK3Widget
            The GTK3Widget to add as a child to the GTK3ActionBar.
        start : bool
            Whether to add the child widget at the start (default) or end of the
            GTK3HeaderBar.
        """
        if start:
            return self.pack_start(child)
        return self.pack_end(child)


class GTK3ActionBar(Gtk.ActionBar, GTK3ActionBarMixin):
    """Wrapper for version 3.0 Gtk.ActionBar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ActionBar."""
        Gtk.ActionBar.__init__(self)
        GTK3ActionBarMixin.__init__(self)
