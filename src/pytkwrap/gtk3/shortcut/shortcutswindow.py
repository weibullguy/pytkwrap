"""The pytkwrap GTK3ShortcutsWindow module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window.window import GTK3Window


class GTK3ShortcutsWindow(Gtk.ShortcutsWindow, GTK3Window):
    """Wrapper for version 3.0 Gtk.ShortcutsWindow."""

    _GTK3_SHORTCUTSWINDOW_PROPERTIES = GTK3WidgetProperties(
        section_name="internal-search",
        view_name=None,
    )
    _GTK3_SHORTCUTSWINDOW_SIGNALS = [
        "close",
        "search",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ShortcutsWindow."""
        Gtk.ShortcutsWindow.__init__(self)
        GTK3Window.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SHORTCUTSWINDOW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SHORTCUTSWINDOW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Window-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Window.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_accept_focus(self.dic_properties["accept_focus"])
        self.set_application(self.dic_properties["application"])
        self.set_attached_to(self.dic_properties["attached_to"])
        self.set_decorated(self.dic_properties["decorated"])
        self.set_deletable(self.dic_properties["deletable"])
        self.set_destroy_with_parent(self.dic_properties["destroy_with_parent"])
        self.set_focus_on_map(self.dic_properties["focus_on_map"])
        self.set_focus_visible(self.dic_properties["focus_visible"])
        self.set_gravity(self.dic_properties["gravity"])
        self.set_hide_titlebar_when_maximized(
            self.dic_properties["hide_titlebar_when_maximized"]
        )
        self.set_icon(self.dic_properties["icon"])
        self.set_icon_name(self.dic_properties["icon_name"])
        self.set_mnemonics_visible(self.dic_properties["mnemonics_visible"])
        self.set_modal(self.dic_properties["modal"])
        self.set_resizable(self.dic_properties["resizable"])

        if self.dic_properties["role"] is not None:
            self.set_role(self.dic_properties["role"])

        self.set_skip_taskbar_hint(self.dic_properties["skip_taskbar_hint"])

        if self.dic_properties["startup_id"] is not None:
            self.set_startup_id(self.dic_properties["startup_id"])

        self.set_title(self.dic_properties["title"])
        self.set_transient_for(self.dic_properties["transient_for"])
        self.set_type_hint(self.dic_properties["type_hint"])
        self.set_urgency_hint(self.dic_properties["urgency_hint"])
        self.set_position(self.dic_properties["window_position"])

        for _property in ["default_height", "default_width"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
