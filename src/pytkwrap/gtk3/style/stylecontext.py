"""The pytkwrap GTK3StyleContext module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties
from pytkwrap.gtk3.style import GTK3CssProvider


class GTK3StyleContextMixin(GTK3GObjectMixin):
    """Mixin class for GTK3StyleContext.

    Notes
    -----
    GTK3StyleContext passes no widgets to its callback functions.
    """

    _GTK3_STYLECONTEXT_PROPERTIES = GTK3WidgetProperties(
        frame_clock=None,
        parent=None,
        path=None,
        scale=1,
        screen=None,
        sides=None,
        state=None,
    )
    _GTK3_STYLECONTEXT_SIGNALS = [
        "changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3StyleContext mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_STYLECONTEXT_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_STYLECONTEXT_PROPERTIES)

        self.dic_providers: dict[GTK3CssProvider, int] = {}

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3StyleContext-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3StyleContext.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_parent(self.dic_properties["parent"])
        self.set_scale(self.dic_properties["scale"])

        if self.dic_properties["frame_clock"] is not None:
            self.set_frame_clock(self.dic_properties["frame_clock"])

        if self.dic_properties["path"] is not None:
            self.set_path(self.dic_properties["path"])

        if self.dic_properties["screen"] is not None:
            self.set_screen(self.dic_properties["screen"])

        if self.dic_properties["sides"] is not None:
            self.set_junction_sides(self.dic_properties["sides"])

        if self.dic_properties["state"] is not None:
            self.set_state(self.dic_properties["state"])

    def do_add_style_provider(
        self,
        provider: GTK3CssProvider,
        priority: int,
        screen: Gdk.Screen | None = None,
    ) -> None:
        """Add provider to GTK3StyleContext.

        Parameters
        ----------
        provider : GTK3CssProvider
            A GTK3CssProvider.
        priority : int
            The priority of the provider to add.
        screen : Gdk.Screen
            A Gdk.Screen to add the provider as a global provider.
        """
        self.dic_providers[provider] = priority

        if screen is not None:
            return self.add_provider_for_screen(screen, provider, priority)

        return self.add_provider(provider, priority)

    def do_get_stateful_property(
        self,
        property_name: str,
        state: Gtk.StateFlags,
    ) -> Gtk.Border | Gdk.RGBA | None:
        """Get the value of the requested property for the requested state.

        Parameters
        ----------
        property_name : str
            The name of the property whose value is to be retrieved.
        state : Gtk.StateFlags
            The widget state to retrieve the property for.  Options are NORMAL,
            ACTIVE, VISITED, DIR_LTR, INCONSISTENT, PRELIGHT, CHECKED, DIR_RTL,
            FOCUSED, SELECTED, DROP_ACTIVE, LINK, BACKDROP, or INSENSITIVE.

        Returns
        -------
        Gtk.Border | Gdk.RGBA | None
            The current value of the property.
        """
        if property_name == "border":
            return self.get_border(state)

        if property_name == "color":
            return self.get_color(state)

        if property_name == "margin":
            return self.get_margin(state)

        if property_name == "padding":
            return self.get_padding(state)

        return None

    def do_remove_style_provider(self, provider: GTK3CssProvider) -> None:
        """Remove the requested style provides.

        Parameters
        ----------
        provider : GTK3CssProvider
            The GTK3CssProvider to remove.
        """
        self.remove_provider(provider)
        self.dic_providers.pop(provider)


class GTK3StyleContext(Gtk.StyleContext, GTK3StyleContextMixin):
    """Wrapper for version 3.0 Gtk.StyleContext."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3StyleContext."""
        Gtk.StyleContext.__init__(self)
        GTK3StyleContextMixin.__init__(self)
