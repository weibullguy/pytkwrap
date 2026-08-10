"""The pytkwrap GTK3PlacesSidebar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window.scrolledwindow import GTK3ScrolledWindowMixin


class GTK3PlacesSidebarMixin(GTK3ScrolledWindowMixin):
    """Mixin for GTK3PlacesSidebar.

    Notes
    -----
    GTK3PlacesSidebar passes a Gtk.Viewport to it's callback function.
    """

    _GTK3_PLACESSIDEBAR_PROPERTIES = GTK3WidgetProperties(
        local_only=False,
        location=None,
        open_flags=Gtk.PlacesOpenFlags.NORMAL,
        populate_all=False,
        show_desktop=True,
        show_enter_location=False,
        show_other_locations=False,
        show_recent=True,
        show_starred_location=False,
        show_trash=True,
    )
    _GTK3_PLACESSIDEBAR_SIGNALS = [
        "drag-action-ask",
        "drag-action-requested",
        "drag-perform-drop",
        "mount",
        "open-location",
        "populate-popup",
        "show-connect-to-server",
        "show-enter-location",
        "show-error-message",
        "show-other-locations",
        "show-other-locations-with-flags",
        "show-starred-location",
        "unmount",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3PlacesSidebar mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_PLACESSIDEBAR_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_PLACESSIDEBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3PlacesSidebar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3PlacesSidebar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_local_only(self.dic_properties["local_only"])

        if self.dic_properties["location"] is not None:
            self.set_location(self.dic_properties["location"])

        self.set_open_flags(self.dic_properties["open_flags"])
        self.set_show_desktop(self.dic_properties["show_desktop"])
        self.set_show_enter_location(self.dic_properties["show_enter_location"])
        self.set_show_other_locations(self.dic_properties["show_other_locations"])
        self.set_show_recent(self.dic_properties["show_recent"])
        self.set_show_starred_location(self.dic_properties["show_starred_location"])
        self.set_show_trash(self.dic_properties["show_trash"])

        for _property in ["populate_all"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )


class GTK3PlacesSidebar(Gtk.PlacesSidebar, GTK3PlacesSidebarMixin):
    """The GTK3PlacesSidebar class."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3PlacesSidebar."""
        Gtk.PlacesSidebar.__init__(self)
        GTK3PlacesSidebarMixin.__init__(self)
